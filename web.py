from app.models.lift import Lift
from app.db.session import Session

from dateutil.tz import gettz

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/templates')

app = Starlette()

@app.route('/', methods=['GET'])
async def root(request):
  timezone = gettz('America/Los_Angeles')

  session = Session()
  lifts = session.query(Lift).all()

  return templates.TemplateResponse('lifts/index.html', {'request': request, 'timezone': timezone, 'lifts': lifts})
