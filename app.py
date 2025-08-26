from flask import Flask
import random

app = Flask(__name__)
# app.config['JSON_AS_ASCII']=False
app.json.ensure_ascii = False

about_me = {
    "name": "Андрей",
    "surname": "Алабин",
    "email": "andreyalabin@vk.com"
}

q = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },
]

d={}

for el in q:
    d[str(el.get('id'))]=[el.get('author'), el.get('text')]

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
   return about_me

@app.route("/quotes/", defaults={'num': None})
@app.route("/quotes/<num>")
def quotes(num):
    if num:
        if d.get(num):
            res = f'Цитата с id={num}: {d.get(num)[1]}'
        else:
            res = f'Quote with id={num} not found, 404'
    else:
        res = q
    return res

@app.route("/quotes/count")
def quotes_count():
    res= \
    {
        "count": len(q),
    }
    return res

@app.route("/quotes/random")
def quotes_random():
    num = random.choice(list(d.keys()))
    print(num)
    return f'Случайная цитата с id={num}: {d.get(num)[1]}'


if __name__ == "__main__":
    app.run(debug=True)
