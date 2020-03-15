from app.models.lift import Lift
from app.db.session import Session

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse

templates = Jinja2Templates(directory='app/templates')

app = Starlette()

@app.route('/', methods=['GET'])
async def root(request):  
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._asdict() for l in lifts]

  session.close()

  return templates.TemplateResponse('lifts/index.html', {'request': request, 'lifts': lift_dicts})

@app.route('/lifts', methods=['GET'])
async def lifts(request):
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._asdict() for l in lifts]

  session.close()

  return JSONResponse({'lifts': lift_dicts})
