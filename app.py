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

@app.route("/", methods=['GET','POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.correo.data)
       #Realizar el insert en la bd
        db.session.add(alum)
        db.session.commit()
        
        return redirect(url_for('ABCompleto'))
    return render_template('index.html',form = create_form)

@app.route("/ABCompleto",methods=["GET","POST"])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos ) 

@app.route("/modificar",methods=["GET","POST"])
def modificar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    if request.method=='POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html',form=create_form)


@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    create_form= forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        #select  * from alumns where id == id 
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.correo.data = alum1.correo
    if request.method=='POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data 
        alum.apellidos = create_form.apellidos.data
        alum.correo = create_form.correo.data
        
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html',form=create_form)


if __name__ =='__main__':
    csrf.init_app(app) #al iniciar tiene seguridad crsf
    db.init_app(app) #iniciar la conexion a la base de datos 
    with app.app_context(): #verifica si se hizo la conexion y crea las tablas 
        db.create_all()
    app.run(port=3000)

