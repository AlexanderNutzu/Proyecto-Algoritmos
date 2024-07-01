class Producto():
    def __init__(self,nombre,cantidad, precio, stock,adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.adicional = adicional
    def show_attr(self):
        print("Nombre: ", self.nombre)
        print(f"Precio {self.precio} + IVA  ")
        print()

#Creacion de clase tipo Prodcuto con su show que muestra los atributos de cada objeto especificamente.