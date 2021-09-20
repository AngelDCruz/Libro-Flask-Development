from flask import Flask, render_template, request, make_response, abort

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
 user_agent = request.headers.get("User-Agent")
 return f'<h1>{user_agent}</h1>'

@app.route("/home")
def home():
 return "Home"

@app.route("/make-response")
def make_res():
 response = make_response("<h1>Bienvenidos</h1>")
 response.set_cookie("token", "ey28328dhahasahsdhadahsdhahsd")
 print(response.headers)
 response.status_code = 203
 return response


@app.route("/usuario/<int:id>")
def usuario(id):
 usuarios = [0, 1, 2]
 if id not in usuarios:
  abort(404)
 index = usuarios.index(id)
 usuario = usuarios[index]
 return f"usuario {usuario}"


@app.route("/platilla-inicio")
def plantilla_inicio():
 return render_template('index.html')

@app.route("/usuario/<nombre>/nombre")
def usuario_nombre(nombre):
 usuarios = ["Ana", "Susana", "Pedro"]
 return render_template("nombre.html", nombre=nombre, usuarios=usuarios)