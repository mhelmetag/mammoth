import os

from starlette.applications import Starlette
from starlette.responses import JSONResponse

SEASON = os.getenv('SEASON', 'Winter')

app = Starlette()


@app.route('/', methods=['GET'])
async def root(_):
    return JSONResponse(data())


def data():
    with open(fake_filename(), 'r') as file:
        html = file.read()
        return {
            'data': html,
            'success': True,
            'Message': None
        }


def fake_filename():
    if SEASON == 'Winter':
        return 'fake/winter.html'
    else:
        return 'fake/summer.html'
