import os
from bottle import route, run, view
from datetime import datetime as dt
from random import random

@route("/")
@view("predictions")
def index():
  now = dt.now()

  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": [
      "После обеда ожидайте неожиданного праздника.",
      "Днем остерегайтесь неожиданного праздника.",
      "Утром ожидайте гостей из забытого прошлого.",
    ]
  }
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
