from flask import Flask

app = Flask(__name__)
# app.config['JSON_AS_ASCII']=False
app.json.ensure_ascii = False

about_me = {
    "name": "Андрей",
    "surname": "Алабин",
    "email": "andreyalabin@vk.com"
}

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
   return about_me

if __name__ == "__main__":
    app.run(debug=True)