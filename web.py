from app.models.lift import Lift
from app.db.session import Session
from app.shared.firebase import init_firebase_admin

import os

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, FileResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
import firebase_admin
from firebase_admin import messaging

APP_ENV = os.getenv('APP_ENV', 'development')

templates = Jinja2Templates(directory='app/templates')
routes = [
    Mount('/static', app=StaticFiles(directory='app/static'), name="static")]
app = Starlette(routes=routes)

init_firebase_admin()


@app.route('/', methods=['GET'])
async def root(request):
    session = Session()
    lifts = session.query(Lift).all()
    lift_dicts = [l._for_html() for l in lifts]

    session.close()

    return templates.TemplateResponse('lifts/index.html', {'request': request, 'lifts': lift_dicts})


@app.route('/register', methods=['POST'])
async def register(request):
    data = await request.json()
    subscriber_id = data['subscriber_id']
    tokens = [subscriber_id]

    messaging.subscribe_to_topic(tokens, 'updates')

    return JSONResponse({'success': True})


@app.route('/firebase-messaging.js', methods=['GET'])
async def messaging_js(request):
    if APP_ENV == 'production':
        return FileResponse('app/dynamic/firebase-messaging.js')
    else:
        return FileResponse('app/dynamic/firebase-messaging-dev.js')


@app.route('/firebase-messaging-sw.js', methods=['GET'])
async def messaging_sw_js(request):
    if APP_ENV == 'production':
        return FileResponse('app/dynamic/firebase-messaging-sw.js')
    else:
        return FileResponse('app/dynamic/firebase-messaging-dev-sw.js')


@app.route('/api/lifts', methods=['GET'])
async def lifts(request):
    session = Session()
    lifts = session.query(Lift).all()
    lift_dicts = [l._for_json() for l in lifts]

    session.close()

    return JSONResponse({'lifts': lift_dicts})
