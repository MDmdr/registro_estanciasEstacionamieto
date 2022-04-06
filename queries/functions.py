
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


