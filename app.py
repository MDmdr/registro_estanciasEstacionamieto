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

# @app.route('/registerNew')
# def register_New():   
#     data={ 'date': getDate() ,
#            'hour': getHour() 
#           }
#     return render_template('registerNew.html', data=data)

@app.route('/registerNew')
def register_New():   
    data={ 'date': getDate() ,
           'hour': getHour() 
          }
    return render_template('optionRegisterParking.html', data=data)

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
@app.route('/registerEntry')
def register_Entry():
    return render_template('registerPay.html')

@app.route('/registerExit')
def register_Exit():
    
    return render_template('registerPay.html')
# ---------------------------------------------------------------------------------
# @app.route("/saveRegister", methods=['POST'])
# def save_Register():
#   if request.method == 'POST':
#     # texto=request.form.get("texto1")
#     texto=request.form.get("numeroPlaca")
#     texto=request.form.get("hora_E_S")
#     texto=request.form.get("tipoVehiculo") 

#   texto="[registro guardado]"
#   # save registers to dataBase  
#   # PROCESO FROM -->RESPOSE
#   return texto

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

    # texto="[registrar vehiculo]"
    # return texto
    data={ 'msg': "Vehiculo guardado en la base de datos",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)

@app.route("/saveTypeVehicle", methods=['POST'])
def save_TypeVehicle():
    if request.method == 'POST':    
        TypeVehicle=request.form.get("tipoVehiculo")
        description=request.form.get("descripcion")

        # save registers to dataBase
        functions.saveRegisterTypeVehicle( TypeVehicle, description )
        # saveRegisterTypeVehicle( TypeVehicle, description ):

    # texto="[ Tipo de vehiculo -> Regisrado ]" 
    # return texto
    data={ 'msg': "Tipo de vehiculo guardado",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)

@app.route("/savePay", methods=['POST'])
def save_Pay():
    # numeroPlaca
    # hora
    # tipoVehiculo
    # vehiculo
    # importe
    if request.method == 'POST':
        texto=request.form.get("numeroPlaca")
        texto=request.form.get("hora")
        texto=request.form.get("tipoVehiculo")
        texto=request.form.get("vehiculo")
        texto=request.form.get("importe")
    
    # get all pay

    # save registers to dataBase

    texto="/"+texto+"/"+"[registrar pago de estancia]" 
    return texto

# --------------------------------------------------------------------------------
@app.route("/viewInputCarPlate")
def view_InputCarPlate():
    # url to view input car plate    
    return render_template('inputCarPlate.html')


# @app.route("/searchCarPlate", methods=['POST'])
# def search_CarPlate():
#     if request.method == 'POST':    
#         car_plate=request.form.get("car_plate")
        
#         # search car plate
#         functions.searchCarPlate( car_plate )
#         # saveRegisterTypeVehicle( TypeVehicle, description ):

#     # texto="[ Tipo de vehiculo -> Regisrado ]" 
#     # return texto
#     data={ 'msg': "Tipo de vehiculo guardado",
#            'link': "null"
#         }
#     return render_template('exitApp.html', data=data)

@app.route("/captureCarPlate", methods=['POST'])
def capture_CarPlate():
    if request.method == 'POST':    
        car_plate=request.form.get("car_plate")
        
        # search car plate
        # functions.function( car_plate ) # some operation

        data={ 'msg': " ",
             'link': "null",
             'car_plate': car_plate
        }
        return render_template('optionRegisterParking.html', data=data)
        
    
    data={ 'msg': " ",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)

@app.route("/saveEntryCar", methods=['POST'])
def save_EntryCar():
    if request.method == 'POST':    
        car_plate=request.form.get("car_plate")        
        # some operation
        data={ 'msg': " ",
             'link': "null",
             'car_plate': car_plate,
             'option_ES': "entry",
             'date': getDate(),
             'hour': getHour()
        }
        return render_template('viewRegisterNew.html', data=data)
        
    
    data={ 'msg': " ",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)

@app.route("/saveExitCar", methods=['POST'])
def save_ExitCar():
    if request.method == 'POST':    
        car_plate=request.form.get("car_plate")        
        # some operation
        data={ 'msg': " ",
             'link': "null",
             'car_plate': car_plate,
             'option_ES': "exit",
             'date': getDate(),
             'hour': getHour()
        }
        return render_template('viewRegisterNew.html', data=data)
        
    
    data={ 'msg': " ",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)

@app.route("/saveRegisterParking", methods=['POST'])
def save_RegisterParking():
    if request.method == 'POST':
        option_ES=request.form.get("option_ES")
        car_plate=request.form.get("car_plate")
        date=request.form.get("date")
        hour=request.form.get("hour")
        type_vehicle=request.form.get("type_vehicle")

        if option_ES == "entry":
            # Entry car            
            functions.saveEntryCarParking( car_plate, date, hour, type_vehicle)
            data={ 'msg': "Registro de entrada Guardado",
                   'link': "null"
                }
            return render_template('exitApp.html', data=data)

            # # functions.saveEntryCarParking( car_plate, date, hour, type_vehicle)
            # data={ 'msg': "false",
            #    'link': "null"
            # }
            # return render_template('exitApp.html', data=data)
        if option_ES == "exit":
            # Exit car
            #functions.saveExitCarParking( car_plate, date, hour, type_vehicle)
            save_parking_car_exit( car_plate, date, hour, type_vehicle)
            
            data={ 'msg': "Registro de salida Guardado",
               'link': "null"
            }
            return render_template('exitApp.html', data=data)

        data={ 'msg': "No option",
               'link': "null"
            }
        return render_template('exitApp.html', data=data)

    data={ 'msg': " ",
           'link': "null"
        }
    return render_template('exitApp.html', data=data)



## ----------------------------------------------------------------------------------
def save_parking_car_exit( car_plate, date, hour, type_vehicle):
    if type_vehicle == "oficial":        
        functions.saveRegister_Oficial(car_plate, date, hour)
        return ""
    if type_vehicle == "residente":        
        functions.saveRegister_Residente(car_plate, date, hour)
        return ""
    if type_vehicle == "no_residente":
        functions.saveRegister_No_residente(car_plate, date, hour)
        return ""
    else:
        return "false"
    return "false"
## ---------------------------------------------------------------------------------
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
