import random
from flask import Flask
app = Flask(__name__)

datos= [
"La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
"El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
"Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
"Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos"]

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/help")
def help():
    return '<h1>Cualquier cosa!</h1>'

@app.route("/profe")
def profe():
    return '<h1>Hola profe</h1>'

@app.route("/dato")
def dato():
    return f'<p>{random.choice(datos)}</p>'


app.run(debug=True)
