from app.models.lift import Lift
from app.models.subscriber import Subscriber
from app.db.session import Session

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, RedirectResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory='app/templates')
routes = [Mount('/static', app=StaticFiles(directory='app/static'), name="static")]
app = Starlette(routes=routes)

@app.route('/', methods=['GET', 'POST'])
async def root(request):  
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._for_html() for l in lifts]

  session.close()

  return templates.TemplateResponse('lifts/index.html', {'request': request, 'lifts': lift_dicts})

@app.route('/api/lifts', methods=['GET'])
async def lifts(request):
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._for_json() for l in lifts]

  session.close()

  return JSONResponse({'lifts': lift_dicts})
