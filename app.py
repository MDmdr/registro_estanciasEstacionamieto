# -*- coding: utf-8 -*-

import os, sys

from flask import Flask, render_template, json, request
from werkzeug.utils import secure_filename
from flask import send_file 

#-------------------------------------------
import json
#-------------------------------------------
import string
#-------------------------------------------
import codecs

# queries
from queries import functions

app = Flask(__name__)



#--------------------------------------------------------

@app.route('/')
def main():
    print( getDate() )
    print( getHour() )
    
    # setTypeVehicle    
    functions.getTypesVehicles()
    functions.setTypeVehicle()
    return render_template('index.html')

# registerNew
# registerLists   
# registerVehicle
# registerTypeVehicle
# registerPay

@app.route('/registerNew')
def register_New():   
    data={ 'date': getDate() ,
           'hour': getHour() 
          }
    return render_template('registerNew.html', data=data)

@app.route('/registerLists')
def register_Lists():
    # get query all registrer function assignment
    data={ 'date': getDate() ,
           'hour': getHour(),
           'arrayRegistros': "null"
        }
    return render_template('registerLists.html', data=data)

@app.route('/registerVehicle')
def register_Vehicle():
    # get query typeVehicles = data
    data=""
    return render_template('registerVehicle.html', data=data)

@app.route('/registerTypeVehicle')
def register_TypeVehicle():
    return render_template('registerTypeVehicle.html')

@app.route('/registerPay')
def register_Pay():
    return render_template('registerPay.html')


# ---------------------------------------------------------------------------------
@app.route("/saveRegister", methods=['POST'])
def save_Register():
  if request.method == 'POST':
    # texto=request.form.get("texto1")
    texto=request.form.get("numeroPlaca")
    texto="/"+texto+"/"+ request.form.get("hora_E_S")
    texto="/"+texto+"/"+request.form.get("tipoVehiculo") 

  texto="/"+texto+"/"+"[registro guardado]"


  # save registers to dataBase  
  # PROCESO FROM -->RESPOSE
  return texto

@app.route("/saveVehicle", methods=['POST'])
def save_Vehicle():
    # numeroPlaca
    # Marca
    # Propietario 
    # tipoVehiculo
    if request.method == 'POST':
        car_plate=request.form.get("numeroPlaca")
        mark=request.form.get("marca")
        proprietor=request.form.get("propietario")
        type_vehicle=request.form.get("tipoVehiculo")

        # save registers to dataBase
        functions.saveRegisterVehicle( mark, car_plate, proprietor, type_vehicle )

    texto="[registrar vehiculo]"
    return texto

@app.route("/saveTypeVehicle", methods=['POST'])
def save_TypeVehicle():
    if request.method == 'POST':    
        TypeVehicle=request.form.get("tipoVehiculo")
        description=request.form.get("descripcion")

        # save registers to dataBase
        functions.saveRegisterTypeVehicle( TypeVehicle, description )
        # saveRegisterTypeVehicle( TypeVehicle, description ):

    texto="[ Tipo de vehiculo -> Regisrado ]" 
    return texto

@app.route("/savePay", methods=['POST'])
def save_Pay():
    # numeroPlaca
    # hora
    # tipoVehiculo
    # vehiculo
    # importe
    if request.method == 'POST':
        texto=request.form.get("numeroPlaca")
        texto="/"+texto+"/"+request.form.get("hora")
        texto="/"+texto+"/"+request.form.get("tipoVehiculo")
        texto="/"+texto+"/"+request.form.get("vehiculo")
        texto="/"+texto+"/"+request.form.get("importe")
    
    # get all pay

    # save registers to dataBase

    texto="/"+texto+"/"+"[registrar pago de estancia]" 
    return texto



##----------------------------------------------------------------------------------
from datetime import datetime
import uuid
def getDate():  
    now = datetime.now()
    # now.year  # now.month  # now.day
    return str(now.year)+"/"+str(now.month)+"/"+str(now.day)
def getHour():  
    now = datetime.now()    
    return str(now.hour)+":"+str(now.minute)+":"+str(now.second)
def getUid():    
    return str(uuid.uuid4().hex)
    



if __name__ == "__main__":
   app.run(debug=True, port=8067, host='0.0.0.0')
