class Equipo():
    def __init__(self,id,code,name,group):
        self.id=id
        self.code=code
        self.name=name
        self.group=group
    
    def show_attr(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|                                                |")
        print(f" Id: {self.id}")
        print(f" Código: {self.code}- Nombre: {self.name} - (Grupo: {self.group})")
        print("|                                                |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")

#Creacion de clase tipo Equipo con su show que muestra los atributos de cada objeto especificamente.