import asyncio
import json
from aiohttp import web
from pathlib import Path
from functools import partial

from .exceptions import ObjectNotFound, UnprocessableEntity
from .worker import predict
from .consts import MODELS_KEY
from .stats import ModelStats, AggStats
from typing import Dict


jsonify = partial(json.dumps, indent=4, sort_keys=True)
json_response = partial(web.json_response, dumps=jsonify)


class SiteHandler:
    def __init__(self, project_root: Path) -> None:
        self._root = project_root
        self._loop = asyncio.get_event_loop()

    @property
    def project_root(self) -> Path:
        return self._root

    async def index(self, request):
        path = str(self._root / 'static' / 'index.html')
        return web.FileResponse(path)


def setup_app_routes(
    app: web.Application, handler: SiteHandler
) -> web.Application:
    r = app.router
    h = handler
    path = str(handler.project_root / 'static')
    r.add_get('/', h.index, name='index')
    r.add_get('/{model_name}', h.index, name='index.model')
    r.add_static('/static/', path=path, name='static')
    return app


class APIHandler:
    def __init__(self, app, executor, project_root, model_desc):
        self._app = app
        self._executor = executor
        self._root = project_root
        self._loop = asyncio.get_event_loop()

        self._models = {m.name: m for m in model_desc}
        self._app[MODELS_KEY] = {m.name: ModelStats() for m in model_desc}

        result = sorted(self._models.values(), key=lambda v: v.name)
        self._models_list = [
            {'name': m.name, 'target': m.target} for m in result
        ]

    def validate_model_name(self, model_name: str) -> str:
        if model_name not in self._models:
            msg = f'Model with name {model_name} not found.'
            raise ObjectNotFound(msg)
        return model_name

    async def model_list(self, request):
        return json_response(self._models_list)

    async def model_detail(self, request):
        model_name = request.match_info['model_name']
        self.validate_model_name(model_name)

        r = self._models[model_name].asdict()
        return json_response(r)

    async def model_predict(self, request):
        model_name = request.match_info['model_name']
        self.validate_model_name(model_name)
        raw_data = await request.read()
        run = self._loop.run_in_executor

        try:
            future = run(self._executor, predict, model_name, raw_data)
            r = await future
        except asyncio.CancelledError:
            raise
        except Exception as e:
            msg = 'Model failed to predict'
            raise UnprocessableEntity(msg, reason=str(e)) from e

        return json_response(r)

    async def model_stats(self, request):
        model_name = request.match_info['model_name']
        stats: ModelStats = request.app[MODELS_KEY][model_name]
        r = stats.formatted()
        return json_response(r)

    async def agg_stats(self, request):
        stats_map: Dict[str, ModelStats] = request.app[MODELS_KEY]
        agg = AggStats.from_models_stats(stats_map)
        return json_response(agg.formatted())


def setup_api_routes(
    api: web.Application, handler: APIHandler
) -> web.Application:
    r = api.router
    h = handler
    r.add_get('/v1/agg_stats', h.agg_stats, name='stats.list')
    r.add_get('/v1/models', h.model_list, name='models.list')
    r.add_get('/v1/models/{model_name}', h.model_detail, name='models.detail')
    r.add_get(
        '/v1/models/{model_name}/stats', h.model_stats, name='models.stats'
    )
    r.add_get(
        '/v1/models/{model_name}/schema', h.model_detail, name='models.schema'
    )
    r.add_post(
        '/v1/models/{model_name}/predict',
        h.model_predict,
        name='models.predict',
    )
    return api
