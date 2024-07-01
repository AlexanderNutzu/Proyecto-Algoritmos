def inicio():
    with open('BaseDeDatos.txt', 'a+') as bd:
        bd.write("")
    with open('BaseDeDatosRes.txt', 'a+') as bd:
        bd.write("")
#Creacion de los archivos utilizados para bases de datos internos
def registrarvip(nombre, edad, cedula, tipo_entrada, partido, puesto, id, monto, asistencia):
    vip_data = {
       "Tipo" : 'Entrada',

        'Nombre': nombre,
        'Edad': edad,
        'Cedula': cedula,
        'Tipo_de_Entrada': tipo_entrada,
        'Numero_de_Partido': partido,
        'Puesto': puesto,
        'ID_de_entrada': id,
        'Monto_Entrada': monto,
        'Asistencia': asistencia,
        
        
    }
    
    with open('BaseDeDatos.txt', 'a+') as bd:
        bd.write(str(vip_data) + '\n')

def registrargeneral(nombre, edad, cedula, tipo_entrada, partido, puesto, id, monto,asistencia):
    general_data = {
        "Tipo" : 'Entrada',
        'Nombre': nombre,
        'Edad': edad,
        'Cedula': cedula,
        'Tipo_de_Entrada': tipo_entrada,
        'Numero_de_Partido': partido,
        'Puesto': puesto,
        'ID_de_entrada': id,
        'Monto_Entrada': monto,
        'Asistencia': asistencia,
        
        
    }
    
    with open('BaseDeDatos.txt', 'a+') as bd:
        bd.write(str(general_data) + '\n')

def registrarvipres(id,listaproductoscompra,montores):
    vipres_data = {
        "Tipo" : 'Restaurant',
        'ID_de_entrada': id,
        'Lista_de_Productos': listaproductoscompra,
        'Monto_Restaurant': montores
        }
   
    with open('BaseDeDatosRes.txt', 'a+') as bd:
        bd.write(str(vipres_data) + '\n')



#Creacion de base de datos (Diccionarios con datos de cada cliente)