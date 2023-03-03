from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

#from flask import jsonifys
from config import DevelomentConfig
from flask_wtf.csrf import CSRFProtect
from models import Alumnos, db

app=Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf= CSRFProtect()

@app.route("/", methods=["GET","POST"])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.email.data)
       #Realizar el insert en la bd
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html',form = create_form)

if __name__ =='__main__':
    csrf.init_app(app) #al iniciar tiene seguridad crsf
    db.init_app(app) #iniciar la conexion a la base de datos 
    with app.app_context(): #verifica si se hizo la conexion y crea las tablas 
        db.create_all()
    app.run(port=3000)

