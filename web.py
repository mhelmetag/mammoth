from app.models.lift import Lift
from app.models.subscriber import Subscriber
from app.db.session import Session

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, RedirectResponse

templates = Jinja2Templates(directory='app/templates')

app = Starlette()

@app.route('/', methods=['GET', 'POST'])
async def root(request):  
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._asdict() for l in lifts]

  session.close()

  return templates.TemplateResponse('lifts/index.html', {'request': request, 'lifts': lift_dicts})

@app.route('/subscribe', methods=['GET'])
async def subscribe(request):  
  return templates.TemplateResponse('subscribers/new.html', {'request': request})

@app.route('/subscribe', methods=['POST'])
async def post_subscribe(request):
  form = await request.form()
  phone_number = form['phone_number']

  session = Session()
  subscriber = Subscriber(phone_number=phone_number)
  session.add(subscriber)
  session.commit()
  session.close()

  return RedirectResponse(url='/')

@app.route('/unsubscribe', methods=['GET'])
async def unsubscribe(request):  
  return templates.TemplateResponse('subscribers/delete.html', {'request': request})

@app.route('/unsubscribe', methods=['POST'])
async def post_unsubscribe(request):
  form = await request.form()
  phone_number = form['phone_number']

  session = Session()
  subscriber = session.query(Subscriber).filter(Subscriber.phone_number == phone_number).one()
  session.delete(subscriber)
  session.commit()
  session.close()

  return RedirectResponse(url='/')


@app.route('/lifts', methods=['GET'])
async def lifts(request):
  session = Session()
  lifts = session.query(Lift).all()
  lift_dicts = [l._asdict() for l in lifts]

  session.close()

  return JSONResponse({'lifts': lift_dicts})
