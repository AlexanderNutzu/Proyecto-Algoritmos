from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
import requests
from tabulate import tabulate
from Tabulate import mapavip, mapageneral
from factura import numero_vampiro,descuentovamp,descuentoperfecto,iva,factura
from Entrada import Entrada
from txt import registrarvip,registrargeneral,registrarvipres,inicio
from Producto import Producto
from Restaurante import Restaurante
import ast


def main():
    inicio()
    equipos= []
    estadios= []
    partidos=[]
    entradas=[]
    
    idconfirmados=["1"]
    entrada= False
    

    response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
    equipourl = response.json()
    responseestadio= requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
    estadiosurl=responseestadio.json()
    responsepartidos=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
    partidourl= responsepartidos.json()
    #Llamado a la api para creacion de objetos
    for equipo in equipourl:
        equipobjt = Equipo(equipo['id'], equipo['code'], equipo['name'], equipo["group"])
        equipos.append(equipobjt)
    
    
    
    for estadio in estadiosurl:
        lista_restaurantes=[]
        for restaurant in estadio["restaurants"]:
            lista_productos=[]
            for productos in restaurant["products"]:
                producto = Producto(productos["name"], productos["quantity"], productos["price"],productos["stock"],productos["adicional"])
                lista_productos.append(producto)
            restobjt = Restaurante(estadio["id"],restaurant["name"],lista_productos)
            lista_restaurantes.append(restobjt)
        estadiobjt = Estadio(estadio['id'], estadio['name'], estadio["city"], estadio["capacity"],lista_restaurantes)
        estadios.append(estadiobjt)
            

    
    for partido in partidourl:
        for equipo in equipos:
            if equipo.id==partido["home"]["id"]:
                home=equipo.name
            elif equipo.id==partido["away"]["id"]:
                away=equipo.name
        for estadio in estadios:
            if estadio.id==partido["stadium_id"]:
                estadioname = estadio
                capacidad=estadio.capacity
                partidoobjt= Partido(partido["id"],partido["number"],home,away,partido["date"],partido["group"],estadioname,capacidad) 
                partidos.append(partidoobjt)      

           #Creacion de objetos a partir de la api
    while True:
        print()
        print("Bienvenido a la EURO 2024")
        print("")
        print ("~~~~~~~~~~~~~~~~~~")
        if entrada==True:
            option= input("1-Buscar partidos\n2-Comprar entrada\n3-Validar entrada\n4-Ver restaurantes\n5-Estadisticas\n6-Salir\n~~~~~~~~~~~~~~~~~~\n\n>") 
        else:
            option= input("1-Buscar partidos\n2-Comprar entrada\n3-Validar entrada\n5-Estadisticas\n6-Salir\n~~~~~~~~~~~~~~~~~~\n\n>") 
        
        if option == "1":
            print ("~~~~~~~~~~~~~~~~~")
            optionbusqueda = input("1-Por pais\n2-Por estadio\n3-Por fecha\n~~~~~~~~~~~~~~~~~\n\n>")   
           
            if optionbusqueda == "1":
                pais = input("Ingrese el pais: ")
                for partido in partidos:
                    if pais == partido.home or pais == partido.away:
                        print()
                        partido.show_attr()
                        
            elif optionbusqueda == "2":
                estadio = input("Ingrese el estadio: ")
                for partido in partidos:
                    if estadio == partido.estadio.name:
                        print()
                        partido.show_attr()
                        
                        
            elif optionbusqueda == "3":
                fecha = input("Ingrese la fecha (yyyy-mm-dd): ")
                for partido in partidos:
                    if fecha == partido.date:
                        print()
                        partido.show_attr()
    #Opcion de busqueda de partidos tanto por fecha,estadio y pais participante
        elif option == "2":
            partidoatender=int(input("A que partido desea atender: "))
            for partido in partidos:
                
                if partidoatender == partido.number:
                    print("Partido encontrado")
                    print("")
                    partidonumero= partido.number
                    vip_seats= partido.estadio.capacity[1]
                    general_seats= partido.estadio.capacity[0]
                    partido.show_attr()
                    
                    tipoentrada = input("Que tipo de entrada desea comprar(VIP(75$),General(35$)): ").upper()
                    nombre=input("Ingrese su nombre: ")
                    cedula=input("Ingrese su cedula: ")
                    edad=int(input("Ingrese su edad: "))
                    if tipoentrada == "VIP":
                        monto= 75
                        puesto= mapavip(vip_seats,partido,partidonumero)
                        if puesto == False:
                            print()
                        else:
                            descuento_monto = descuentovamp(cedula, monto)
                            monto_con_iva = iva(descuento_monto)
                            factura(tipoentrada, monto,descuento_monto, monto_con_iva)
                            print()        
                            paga=input("Desea pagar: ").upper()
                            if paga == "SI" :
                                
                                print("Pago exitoso")
                                nombreid=nombre.upper()
                                edadid = str(edad)
                                id =edadid +nombreid + cedula + str(partidonumero) + "V" + str(puesto[0]) + str(puesto[1])
                                registrarvip(nombreid, edad, cedula, tipoentrada,partidonumero,puesto,id,monto_con_iva,"False")
                                entradas.append(Entrada(id,puesto,partido.number))
                                for entrada in entradas:
                                    if entrada.id == id:
                                        entrada.show_vip()
                                        
                            else:
                                print("No se realizo el pago")

        
                    elif tipoentrada == "GENERAL":
                        monto= 35
                        puesto= mapageneral(general_seats,partido,partidonumero)
                        if puesto == False:
                            print()
                        else:
                            descuento_monto = descuentovamp(cedula, monto)
                            monto_con_iva = iva(descuento_monto)
                            factura(tipoentrada, monto,descuento_monto, monto_con_iva)
                            print()        
                            pagageneral=input("Desea pagar: ").upper()
                            if pagageneral == "SI":
                                
                                
                                print("Pago exitoso")
                                print()
                                nombreid= nombre.upper()
                                edadid = str(edad)
                                id =edadid +nombreid + cedula + str(partidonumero) + "G" + str(puesto[0]) + str(puesto[1])
                                registrargeneral(nombreid, edad, cedula, tipoentrada,partidonumero,puesto,id,monto,"False")
                                entradas.append(Entrada(id,puesto,partido.number))
                                
                                for entrada in entradas:
                                    if entrada.id == id:
                                        entrada.show_general()
                                        
                            else: 
                                print("No se realizo el pago")
    #Menu de compra de entradas, con tablas de puestos y creacion de la entrada
        elif option == "3":
            idconfirmacion = input("Ingrese el id de la entrada: ")
            for entrada in entradas:
                if idconfirmacion == entrada.id:
                    print("Entrada encontrada")
                    if idconfirmacion in idconfirmados:
                        print("Entrada ya fue utilizada")
                    else:
                        print("Entrada disponible y confirmada")
                        idconfirmados.append(idconfirmacion)
                        if tipoentrada =="GENERAL":
                            registrargeneral(nombreid, edad, cedula, tipoentrada,partidonumero,puesto,id,monto_con_iva,"True")
                        
                        elif tipoentrada=="VIP":
                            registrarvip(nombreid, edad, cedula, tipoentrada,partidonumero,puesto,id,monto_con_iva,"True")
                            entrada= True
    #Validacion de asistencia al partido.                            
                        
                

        elif option == "4":            
              
            if tipoentrada == "VIP":
                if id in idconfirmados:
                    print("Al confirmar su asitencia al partido con entrada VIP, tiene la opcion de ver los restaurantes disponibles en el estadio")
                    opcionrestaurant= input("Desea ver los restaurantes?\n\n> ").upper()
                    if opcionrestaurant == "SI" :
                        print("Restaurantes disponibles:")
                        for partido in partidos:
                            if partidonumero == partido.number:
                                for restaurant in partido.estadio.listarestaurantes:
                                    restaurant.show_attr()
                    
                        
                        print("Desea ver los productos?\n")

                        while True:
                            opcionmenu=input("1-Por restaurante\n2-Por nombre\n3-Por tipo\n4-Por precio\n5-Comprar\n6-Salir\n\n> ")
                            if opcionmenu == "1":
                                opcionbusrest=input("De cual restaurante le gustaria revisar el  menu desea?\n\n> ")
                                for partido in partidos:
                                    if partidonumero == partido.number:
                                        for restaurant in partido.estadio.listarestaurantes:
                                            if opcionbusrest == restaurant.nombre:
                                                print("Menu disponible: ")
                                                print()
                                                restaurant.show_menu()
                                                print()

                            elif opcionmenu =="2":
                                opcionbusnom=input("Ingrese el nombre del producto: ")
                                for partido in partidos:
                                    if partidonumero == partido.number:
                                        for restaurant in partido.estadio.listarestaurantes:
                                            for producto in restaurant.listaproductos:
                                                if opcionbusnom == producto.nombre:
                                                    producto.show_attr()
                            elif opcionmenu =="3":
                                opcionbustip=input("Ingrese el tipo de producto\nalcoholic\nnon-alcoholic\npackage\nplate\n\n> ").lower()
                                for partido in partidos:
                                    if partidonumero == partido.number:
                                        for restaurant in partido.estadio.listarestaurantes:
                                            for producto in restaurant.listaproductos:
                                                if opcionbustip == producto.adicional:
                                                    producto.show_attr()
                            elif opcionmenu=="4":
                                numeromenor=input("Ingrese el precio menor que esta dispuesto a pagar: ")
                                numeromayor=input("Ingrese el precio mayor que esta dispuesto a pagar: ")
                                for partido in partidos:
                                    if partidonumero == partido.number:
                                        for restaurant in partido.estadio.listarestaurantes:
                                            for producto in restaurant.listaproductos:
                                                if numeromenor <= producto.precio <= numeromayor:
                                                    producto.show_attr()

                            elif opcionmenu=="5":
                                montores=0.0
                                listaproductoscompra=[]
                                while True:
                                    comprares=input("Ingrese el nombre del producto que desea comprar\n\n> ")
                                    for partido in partidos:
                                        if partidonumero == partido.number:
                                            for restaurant in partido.estadio.listarestaurantes:
                                                for producto in restaurant.listaproductos:
                                                    if comprares == producto.nombre:
                                                        if producto.adicional=="alcoholic" and edad < 18:
                                                            print()
                                                            print("No puede comprar alcohol")
                                                            print()
                                                        else:
                                                            montores += float(producto.precio)
                                                            producto.stock= producto.stock - 1
                                                            listaproductoscompra.append(producto.nombre)
                                                            print()
                                                            print("Producto agregado al carrito\n")
                                                            print()

                                    preguntares=input("Ya termino con su pedido?\n\n>").upper()
                                    if preguntares == "SI":
                                        print()
                                        descuento_montores = descuentoperfecto(cedula, montores)
                                        monto_con_ivares = iva(descuento_montores)
                                        factura(tipoentrada, montores,descuento_montores, monto_con_ivares)
                                        print()
                                        print("Gracias por su compra")
                                        registrarvipres(id, listaproductoscompra,monto_con_ivares)
                                        break
                                        
                                    elif preguntares == "NO":
                                        continue
                                                                                            
                                    

                            else:
                                break
                            
                    else:
                        print("No se veran los restaurantes")             
            else:
                print("No se tiene acceso a los restaurantes")
    #Menu de restaurante con busqueda de productos por precio, restaurante,tipo y nombre al igual que la compra del producto deseado

        elif option =="5":
            with open('BaseDeDatos.txt', 'r') as bd:
                lineas=[]
                for linea in bd:
                    lineabien=ast.literal_eval(linea)
                    lineas.append(lineabien)
            with open('BaseDeDatosRes.txt', 'r') as bd:
                lineasres=[]
                for lineares in bd:
                    lineabienres=ast.literal_eval(lineares)
                    lineasres.append(lineabienres)

            opcionestadisitica=input("1-Promedio Vip\n2-Mayor Asistencia\n3-Partido con mayor boletos vendidos\n4-Productos mas vendidos en restaurante\n5-Clientes que más compraron boletos\n>")
            if opcionestadisitica == "1":
                divisor=0
                promedio= 0
                for dicc in lineas:
                    if dicc["Asistencia"]== "False" and dicc["Tipo"] == "Entrada" and dicc["Tipo_de_Entrada"] == "VIP":
                        promedio += dicc["Monto_Entrada"]
                        divisor += 1
                        for dicc2 in lineasres:
                            if dicc2["Tipo"]== "Restaurant" and dicc2["ID_de_entrada"] == dicc["ID_de_entrada"]:
                                promedio += dicc2["Monto_Restaurant"]
                                
                print(f"El promedio total es de {promedio/divisor}")
            elif opcionestadisitica == "2":
                asistenciamayor = 0
                numeropartido= ""
                for partido in lineas:
                    if partido["Asistencia"] == "True":
                        asistenciapartido = sum(1 for p in lineas if p["Numero_de_Partido"] == partido["Numero_de_Partido"])
                        if asistenciapartido > asistenciamayor:
                            asistenciamayor = asistenciapartido
                            numeropartido = partido["Numero_de_Partido"]
                print(f"El partido con mayor asistencia fue el numero {numeropartido}")

            elif opcionestadisitica == "3":
                boletomayor = 0
                numeroboletopartido= ""
                for partido in lineas:
                    if partido["Asistencia"] == "False":
                        boletospartido = sum(1 for p in lineas if p["Numero_de_Partido"] == partido["Numero_de_Partido"])
                        if boletospartido > boletomayor:
                            boletomayor = boletospartido
                            numeroboletopartido = partido["Numero_de_Partido"]
                print(f"El partido con mayor venta fue el numero {numeroboletopartido}")

            elif opcionestadisitica == "4":
                opestares=input("Que restaurant desea revisar: ")
                for estadio in estadios:
                    for restaurant in estadio.listarestaurantes:
                        if restaurant.nombre == opestares:
                            producto_compras={}
                            for productores in restaurant.listaproductos:
                                for dicc3 in lineasres:
                                    for producto in dicc3["Lista_de_Productos"]:
                                        if producto == productores.nombre:
                                            if producto in producto_compras:
                                                producto_compras[producto] += 1
                                            else:
                                                producto_compras[producto] = 1
                top_3_productos = sorted(producto_compras.items(), key=lambda x: x[1], reverse=True)[:3]
                print("Top 3 productos más comprados en", opestares, ":")
                for producto, cantidad in top_3_productos:
                    print(f"{producto}: {cantidad} veces")


            elif opcionestadisitica == "5":
                clientes_compras = {}
                for cliente in lineas:
                    if cliente["Asistencia"] == "False" and cliente["Tipo"] == "Entrada":
                        cedula = cliente["Cedula"]
                        nombre = cliente["Nombre"]
                        if (cedula, nombre) in clientes_compras:
                            clientes_compras[(cedula, nombre)] += 1
                        else:
                            clientes_compras[(cedula, nombre)] = 1

                top_3_clientes = sorted(clientes_compras.items(), key=lambda x: x[1], reverse=True)[:3]
                print("Top 3 clientes que más compraron:")
                for cliente, cantidad in top_3_clientes:
                    print(f"{cliente[1]} ({cliente[0]}) - {cantidad} compras")
    #Menu estadisticas en base a los txts ya creados anteriormente                        
                       
                                            
                                            

                               

            
                            
                        
                            




                       
                       
                       
               
                


                
                
                
        elif option =="6":
            break                     
        else:
            continue               
                                    
                                                
                                                

                                
                                      
                                    
                                                


                            
            
                
                
                        
                
            

            

            




main()