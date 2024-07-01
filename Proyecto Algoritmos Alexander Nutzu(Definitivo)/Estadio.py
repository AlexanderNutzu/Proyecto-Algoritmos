class Estadio():
    def __init__(self,id,name,city,capacity,listarestaurantes):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.listarestaurantes = listarestaurantes
       

    def show_attr(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|                                                                  |")
        print(f" Id: {self.id}")
        print(f" Name: {self.name}- City {self.city} - ({self.capacity})")
        print("|                                                                  |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")

#Creacion de clase tipo Estadio con su show que muestra los atributos de cada objeto especificamente.
#Listarestaurantes siendo una lista de objetos restaurante