from app.models.lift import Lift
from app.db.session import Session

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/templates')

app = Starlette()

@app.route('/', methods=['GET'])
async def root(request):  
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._asdict() for l in lifts]

  session.close()

  return templates.TemplateResponse('lifts/index.html', {'request': request, 'lifts': lift_dicts})
