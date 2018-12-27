from aiohttp import web
import aiohttp_jinja2
import jinja2

from .settings import config
from .db import init_pg, close_pg
from .routes import setup_routes


app = web.Application()
aiohttp_jinja2.setup(app=app, loader=jinja2.PackageLoader('polls', 'templates'))
setup_routes(app)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
