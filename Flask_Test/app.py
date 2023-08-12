from flask import Flask, render_template
import random, datetime
app = Flask(__name__)


@app.route('/')
def index():
    #Pasando Variables al HTML
    nombres = ["Elias","Josh","Will"]    
    fecha_actual = datetime.datetime.now()
    newyear = fecha_actual.month == 1 and fecha_actual.day == 1
    print(fecha_actual)
    return render_template("index.html", nombres=nombres, newyear=newyear)



@app.route('/page1')
def page1():
    return render_template("page1.html")





#@app.route('/<string:nombre>')
#def web(nombre):
#    return "Hola, {}, Desde Web".format(nombre)