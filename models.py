#Construir el odelo parqa la tabla de labase de datos 
from flask_sqlalchemy import SQLAlchemy
import datetime 

db = SQLAlchemy()
# crear la clase alumnos 

class Alumnos (db.Model):
    __tablename__ = 'alumnos' #mapear la tabla 
    
    #especificar el tipo de dato atributos de tal tabla
    id = db.Column(db.Integer,primary_key = True)  
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(100))
    correo = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now) #crear un campo para registar la fecha y la hora actual 
