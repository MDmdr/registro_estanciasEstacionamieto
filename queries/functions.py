
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text

# engine = create_engine(
#     'mysql+pymysql://root:54321bd@localhost:3306/bd1',
#     echo=True
# )
# conn = engine.connect()


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



def conection():
    engine = create_engine(
        'mysql+pymysql://root:54321bd@localhost:3306/bd1',
        echo=True
    )
    return engine.connect()


# cruds

def getTypesVehicles():
	print( "tipos de veiculos, desde functions")
	# setTypeVehicle()
	return "tipos de veiculos, desde functions"

def setTypeVehicle():

	conn = conection()

	sql_text = text("INSERT INTO  bd1.t_test (id, text ) VALUES ( 16, 'texto  insert desde t 16' ) ")
	result = conn.execute(sql_text)

	conn.close()

	return ""

def saveRegisterTypeVehicle( TypeVehicle, description ):
    # typeVehicles TABLE
    # id VARCHAR(80), 
    # type_vehicle VARCHAR(150),
    # description VARCHAR(350)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.typeVehicles (id, type_vehicle, description ) VALUES ( ' "+getUid()+" ' , ' "+TypeVehicle+" ' , ' "+description+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print("tipo de vehiculo registrado en bd1")
    return ""


def saveRegisterVehicle( mark, car_plate, proprietor, type_vehicle ):
    # vehicles TABLE
    # id VARCHAR(80), 
    # mark VARCHAR(150),
    # car_plate VARCHAR(100),
    # proprietor VARCHAR(150),
    # type_vehicle VARCHAR(100)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.vehicles (id, mark, car_plate, proprietor, type_vehicle ) VALUES ( ' "+getUid()+" ' , ' "+mark+" ' , ' "+car_plate+" '  , ' "+proprietor+" ' , ' "+type_vehicle+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" vehiculo registrado en base de VEHICULOS bd1")
    return ""


def saveRegisterPayment( car_plate, amount, status ): ## ??? id_de_estancia
    # payments TABLE
    # id VARCHAR(80), 
    # car_plate VARCHAR(100),
    # amount FLOAT(100,3),
    # status VARCHAR(70)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.vehicles (id, car_plate, amount, status ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+amount+" ' , ' "+status+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Pago registrado en la tabla de la base de datos de pagos bd1")
    return ""


def saveRegisterParking( car_plate, hour_entry, hour_exit, proprietor, amount_acc ): ## ??? 
    # register_parking TABLE
    # id VARCHAR(80), 
    # car_plate VARCHAR(100),
    # hour_entry VARCHAR(60),
    # hour_exit VARCHAR(60),
    # proprietor VARCHAR(150),
    # amount_acc FLOAT(100,3)
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, hour_entry, hour_exit, proprietor, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+hour_entry+" ' , ' "+hour_exit+" ' , ' "+proprietor+" ' , ' "+amount_acc+" ' ) ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Registro de Estancia almacenado en la tabla de la base de datos")
    return ""

# get registers tables ----------------------------------------------------------

def getRegisterTypeVehicle( TypeVehicle, description ):
    # typeVehicles TABLE
    # id VARCHAR(80), 
    # type_vehicle VARCHAR(150),
    # description VARCHAR(350)
    conn = conection()
    # SELECT * FROM bd1.typeVehicles;
    sql_text = text(" SELECT * FROM bd1.typeVehicles ")
    result = conn.execute(sql_text)

    conn.close()
    print("Todos los Tipos de vehiculos obtenidos")
    return ""


def getRegisterVehicle( mark, car_plate, proprietor, type_vehicle ):
    # vehicles TABLE
    # id VARCHAR(80), 
    # mark VARCHAR(150),
    # car_plate VARCHAR(100),
    # proprietor VARCHAR(150),
    # type_vehicle VARCHAR(100)
    conn = conection()

    sql_text = text("SELECT * FROM  bd1.vehicles ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Todos los vehiculos obtenidos de la base de datos")
    return ""

# buscar matricula
def searchCarPlate(car_plate):
    result="No hay matricula"
    conn = conection()

    sql_text = text("SELECT * FROM bd1.vehicles WHERE car_plate='"+car_plate+"' ")
    result = conn.execute(sql_text)

    conn.close()
    print(" Matricula buscada: "+ str(result) )
    return ""

# ------------------------------------------------------------------------------------
# create data in BD
def saveEntryCarParking( car_plate, date_entry, hour_entry, type_vehicle):
    # conn = conection()
    # sql_text = text("INSERT INTO  bd1.vehicles (id, car_plate, amount, status ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+amount+" ' , ' "+status+" ' ) ")
    # result = conn.execute(sql_text)
    # conn.close()
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_entry, hour_entry ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date_entry+" ' , ' "+hour_entry+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    return ""

# updates data in the bd, of register in BD
# def saveExitCarParking( car_plate, date, hour, type_vehicle):

#     # se busca id ? y car_plate
#     # id, car_plate
#     # (UPDATE bd1.t_test SET id=8, text='texto update a 8' WHERE id=9)

#     "UPDATE bd1.register_parking date_exit=date,hour_exit=hour WHERE id=id AND car_plate=car_plate"
    
#     text("UPDATE bd1.register_parking date_exit=date,hour_exit=hour WHERE id=id AND car_plate=car_plate")
    


#     conn = conection()

#     text=text(UPDATE bd1.register_parking SET phone_no='Phone No',cust_city='Kolkata',grade=1 WHERE id='id' AND car_plate='car_plate')

#     sql_text = text("INSERT INTO  bd1.register_parking (date_exit, hour_exit, proprietor, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+hour_entry+" ' , ' "+hour_exit+" ' , ' "+proprietor+" ' , ' "+amount_acc+" ' ) ")
#     result = conn.execute(sql_text)

#     conn.close()
#     return ""

# def saveExitCarParking( car_plate, date, hour, type_vehicle): # ???
#     if type_vehicle == "oficial":        
#         saveRegister_Oficia()
#         return ""
#     if type_vehicle == "residente":        
#         saveRegister_Residente()
#         return ""
#     if type_vehicle == "no_residente":
#         saveRegister_No_residente()
#         return ""
#     else:
#         return "false"
#     return "false"

def saveRegister_Oficial(car_plate, date, hour):
    # aux=searchCarPlate(car_plate)
    aux1="NULL"
    aux2="NULL"
    conn = conection()

    # sql_text = text("SELECT id FROM bd1.register_parking WHERE car_plate='"+car_plate+"' AND date_exit='"+aux1+"' AND hour_exit='"+aux2+"'  ")
    sql_text = text("SELECT id FROM bd1.register_parking WHERE car_plate='"+car_plate+"' ")
    result = conn.execute(sql_text)

    conn.close()
    print("result: ")
    print(f"Numero de filas = {result.rowcount}.")
    # Number of rows
    for row in result:
        print(row)
    # -----------------------------------------------------
    id=getUid()
    amount_acc="0" #str()
    conn = conection()

    # "INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '  , ' "+amount_acc+" '  ) "

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit, amount_acc ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '  , 0.0  ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""

def saveRegister_Residente(car_plate, date, hour):
    # -----------------------------------------------------
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""

def saveRegister_No_residente(car_plate, date, hour):
    # -----------------------------------------------------
    id=getUid()
    conn = conection()

    sql_text = text("INSERT INTO  bd1.register_parking (id, car_plate, date_exit, hour_exit ) VALUES ( ' "+getUid()+" ' , ' "+car_plate+" '  , ' "+date+" ' , ' "+hour+" '   ) ")
    result = conn.execute(sql_text)

    conn.close()
    # -----------------------------------------------------
    return ""





