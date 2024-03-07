import os
from pathlib import Path
from shiny.express._run import wrap_express_app

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import HTMLResponse

dashboards = [f for f in os.listdir('adhoc') if f.endswith('.py')]
links = [
    f'<li><a href="/adhoc/{f.replace(".py", "")}">{f.replace(".py", "")}</a></li>'
    for f in dashboards
]

async def index(request):
    return HTMLResponse(f'''
    <style>
    body {{ font-family: sans-serif; display: flex; align-items: center; justify-content: center; }}
    </style>
    <div>
        <h1>Shiny Express Apps!</h1>
        <ul>{"".join(links)}</ul>
    </div>
    ''')

routes = []
routes.append(Route('/', index))
routes.extend([
    Mount(f'/adhoc/{f.replace(".py", "")}', wrap_express_app(Path('.') / 'adhoc' / f))
    for f in dashboards
])

print(routes)

app = Starlette(routes=routes)