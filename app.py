from flask import Flask, jsonify, request
from random import choice

def add_author(cit):
    if not a.get(cit.get('author')):  # если ключа ещё нет
        a[cit.get('author')] = [cit.get('id')]
    else:  # если значение в ключе уже есть
        temp = a.get(cit.get('author'))
        temp.append(cit.get('id'))
        a[cit.get('author')] = temp

app = Flask(__name__)

app.json.ensure_ascii = False
# app.config['JSON_AS_ASCII']=False

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
    {
        "id": 12,
        "author": "Любой программист",
        "text": "Работает? Не трогай."
    },
    {
        "id": 1,
        "author": "Bill Gates",
        "text": "640 Кб должно хватить для любых задач."
    },
    {
        "id": 9,
        "author": "Bill Gates",
        "text": "Измерять продуктивность программиста подсчетом строк кода — это так же, как оценивать постройку самолета по его весу."
    }
]

d={}
a={}

for el in q:
    d[el.get('id')]=el
    add_author(el)


print(a)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
   return about_me

@app.route("/quotes/", defaults={'num': None})
@app.route("/quotes/<int:num>")
def quotes(num:int):
    if num:
        if d.get(num):
            return jsonify(d.get(num))
        else:
            return {'Error': f'Quote with id={num} not found'}, 404
    return q

@app.route("/quotes/count")
def quotes_count():
    return jsonify({'count': len(q)})

@app.route("/quotes/random")
def quotes_random():
    if len(q)>0:
        return jsonify(choice(q))
    return {'Message': f"The database of quotes is empty."}, 200

@app.route("/quotes", methods=['POST'])
def create_quote():
    data = request.json
    auth_req = data.get("author")
    txt_req = data.get("text")
    compare = a.get(auth_req)
    if compare:
        for num in compare:
            txt_orig = d[num]
            if txt_req == txt_orig['text']:
                return {'Error': f'This quote is already in the database, id={num}'}, 400
    if len(q)>0:
        num = max(d.keys())+1
    else:
        num = 1
    cit={
        "id": num,
        "author": auth_req,
        "text": txt_req
    }
    q.append(cit)
    d[num] = cit
    add_author(cit)
    print(a)
    return jsonify(cit), 201

@app.route("/quotes/<int:num>", methods=['DELETE'])
def delete_quote(num:int):
    temp = d.get(num)
    if temp:
        temp_author=a.get(temp['author'])
        print(temp_author)
        if len(temp_author)==1:
            del a[temp['author']]
        elif len(temp_author)>1:
            temp_author.remove(num)
            a[temp['author']] = temp_author
        del d[num]
        ind = q.index(temp)
        print(ind)
        del q[ind]
        print(a)
        print(d)
        return {'Message': f"Quote with id={num} was removed."}, 200
    return {'Message': f"Quote with id={num} not found."}, 200

if __name__ == "__main__":
    app.run(debug=True)
