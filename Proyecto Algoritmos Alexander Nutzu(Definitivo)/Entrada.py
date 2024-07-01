class Entrada():
    def __init__(self,id,puesto,partido):
        self.id=id
        self.puesto=puesto
        self.partido=partido
    def show_vip(self):
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Entrada VIP")
        print(f"Entrada valida para el partido numero {self.partido}")
        print(f"Ubicada en el puesto {self.puesto}")
        print(f"ID de entrada: {self.id}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        

    def show_general(self):
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Entrada General")
        print(f"Entrada valida para el partido numero {self.partido}")
        print(f"Ubicada en el puesto {self.puesto}")
        print(f"ID de entrada: {self.id}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#Creacion de clase tipo entrada con su show que muestra los atributos de cada objeto especificamente.