
from tabulate import tabulate
import ast


def mapavip(vip_seats,partido,partidonumero):
    print()
    columns = 10

    vip_rows = vip_seats // columns

    
    

    vip_table = []
    
    for fila in partido.asientos_vip:
        fila_creada=[]
        for asiento in fila:
            if asiento==False: 
                fila_creada.append('O')
            elif asiento==True:
                fila_creada.append('X')
            else:
                fila_creada.append('')
        vip_table.append(fila_creada)
    #Creacion de matriz conformada por O y X respectivamente si el puesto esta ocupado o no
    with open('BaseDeDatos.txt', 'r') as bd:
                lineas=[]
                for linea in bd:
                    lineabien=ast.literal_eval(linea)
                    lineas.append(lineabien)

    for dicc in lineas:
        if dicc["Asistencia"]== "False" and  dicc['Numero_de_Partido'] == partidonumero and dicc["Tipo_de_Entrada"]== "VIP":
            puesto_x, puesto_y = dicc["Puesto"][0], dicc["Puesto"][1]
            vip_table[puesto_y][puesto_x] = 'X'
            #Se reemplaza el O por X en la matriz si el asiento esta ocupado segun los datos del txt
           

                    
        
    vip_table_output = tabulate(vip_table, headers = [f'{i}' for i in range(columns)], tablefmt='grid',showindex="always")
    #Creacion de tabla con la matriz de base que indica columans y filas con numeros
    print('Asientos VIP: ')
    print(vip_table_output)

    print("""

                    |──────────────────────────────────────────────────────|
                    |                                                      |
                    |                                                      |
                    |                                                      |
             ───────|              O         /|\                           |───────
            |                     /|\       / | \            O                     |                                                    
            |                     / \ o     | | |           \|/                    |                                                
            |                               \ | /           / \                    |
             ───────|                        \|/                           |───────       
                    |                                                      |
                    |                                                      |
                    |                                                      |
                    |──────────────────────────────────────────────────────|

                    """)
    
    print("Que puesto desea:")
    while True:     
        puestocolumna = int(input("Columna (0-9): ")) 
        if 0 <= puestocolumna <= 9:
            break
        else:
            print("Columna invalida")
    while True:
        puestorow = int(input(f"Fila (0-{vip_rows}): "))
        if 1 <= puestorow <= vip_rows:
            break
        else:
            print("Fila invalida")
    #Seleccion de fila y columma solicitada por el cliente

    if vip_table[puestorow][puestocolumna] == 'O':
        vip_table[puestorow][puestocolumna] = 'X'
        vip_table_output = tabulate(vip_table, headers=[f'{i}' for i in range(columns)], tablefmt='grid', showindex="always")
        print('Asientos VIP: ')
        partido.asientos_vip[puestorow][puestocolumna] = True
        print(vip_table_output)
        return puestocolumna,puestorow
    #Segun la seleccion anterior cambiar ambas matrizes ya creadas para guardar la informacion
    
    
    

        
    else:
        print("Ese puesto ya esta asignado")
        return False

def mapageneral(general_seats,partido,partidonumero):
    print()
    columns = 10

    general_rows = general_seats // columns

    general_table=[]

    for fila in partido.asientos_general:
        fila_creada=[]
        for asiento in fila:
            if asiento==False: 
                fila_creada.append('O')
            elif asiento==True:
                fila_creada.append('X')
            else:
                fila_creada.append('')
        general_table.append(fila_creada)
        
    with open('BaseDeDatos.txt', 'r') as bd:
                lineas=[]
                for linea in bd:
                    lineabien=ast.literal_eval(linea)
                    lineas.append(lineabien)

    for dicc in lineas:
        if dicc["Asistencia"]== "False" and  dicc['Numero_de_Partido'] == partidonumero and dicc["Tipo_de_Entrada"]== "GENERAL":
            puesto_x, puesto_y = dicc["Puesto"][0], dicc["Puesto"][1]
            general_table[puesto_y][puesto_x] = 'X'


    



    general_table_output = tabulate(general_table, headers = [f'{i}' for i in range(columns)], tablefmt='grid',showindex="always")
    print('Asientos General: ')
    print(general_table_output)


    


    print("""

                |──────────────────────────────────────────────────────|
                |                                                      |
                |                                                      |
                |                                                      |
         ───────|              O          /|\                          |───────
        |                     /|\        / | \           O                     |                                                    
        |                     / \ o      | | |          \|/                    |                                                
        |                                \ | /          / \                    |
         ───────|                         \|/                          |───────       
                |                                                      |
                |                                                      |
                |                                                      |
                |──────────────────────────────────────────────────────|

                """)


    print("Que puesto desea: ")
   
    while True:     
        puestocolumna = int(input("Columna (0-9): ")) 
        if 0 <= puestocolumna <= 9:
            break
        else:
            print("Columna invalida")
    
    
    while True:
        puestorow = int(input(f"Fila (0-{general_rows}): "))
        if 1 <= puestorow <= general_rows:
            break
        else:
            print("Fila invalida")

    if general_table[puestorow][puestocolumna] == 'O':
        general_table[puestorow][puestocolumna] = 'X'
        general_table_output = tabulate(general_table, headers=[f'{i}' for i in range(columns)], tablefmt='grid', showindex="always")
        print('Asientos Generales: ')
        partido.asientos_general[puestorow][puestocolumna] = True
        print(general_table_output)
        return puestocolumna,puestorow
        
        
    else:
        print("Ese puesto ya esta asignado")
        return False