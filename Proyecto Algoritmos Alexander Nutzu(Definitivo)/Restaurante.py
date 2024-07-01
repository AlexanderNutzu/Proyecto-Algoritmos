class Restaurante():
    def __init__(self,id, nombre,listaproductos ):
        self.id = id
        self.nombre = nombre
        self.listaproductos = listaproductos
       
        
    def show_attr(self):
        print(self.nombre)
    
    def show_menu(self):
        print("Bebidas")
        print("Alcoholicas")
        print()
        for producto in self.listaproductos:
            if producto.adicional == "alcoholic":
                producto.show_attr()
        print("No alcoholicas")
        print()
        for producto in self.listaproductos:
            if producto.adicional == "non-alcoholic":
                producto.show_attr()
        print()
        print("Alimentos")
        print("De Plato")
        print()
        for producto in self.listaproductos:
            if producto.adicional == "plate":
                producto.show_attr()
        print()
        print("De Paquete")
        print()
        for producto in self.listaproductos:
            if producto.adicional == "package":
                producto.show_attr()

#Creacion de clase tipo Restaurante con su show que muestra los atributos de cada objeto especificamente.
#listaproductos siendo una lista de objetos producto que se muestran por tipo en el show_menu


        
           