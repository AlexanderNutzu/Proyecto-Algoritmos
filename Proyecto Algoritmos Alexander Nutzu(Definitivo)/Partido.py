class Partido():
    def __init__(self, id, number, home, away, date,group,estadio,capacidad):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.estadio = estadio
        self.capacidad = capacidad
        self.crearAsientos()    

    def show_attr(self):
        print(f"ID: {self.id}")
        print(f"Number: {self.number}")
        print(f"Local: {self.home}")
        print(f"Visitante: {self.away}")
        print(f"Fecha: {self.date}")
        print(f"Grupo: {self.group}")
        print(f"Estadio: {self.estadio.name}")
      
        print("")
    
    def crearAsientos(self):
        
           
        self.asientos_vip = []
        self.asientos_general = []
        capacity = self.capacidad
        for i in range(int(capacity[1]/10)):
            columnas=[]
            for i in range(10):
                columnas.append(False)
            self.asientos_vip.append(columnas)
        
        for i in range(int(capacity[0]/10)):
            columnas=[]
            for i in range(10):
                columnas.append(False)
            self.asientos_general.append(columnas) 


        faltantes=capacity[1]-len(self.asientos_vip)*10
        self.asientos_vip.append([False for i in range(faltantes)]+[None for i in range(10-faltantes)])
        faltantes=capacity[0]-len(self.asientos_general)*10
        self.asientos_general.append([False for i in range(faltantes)]+[None for i in range(10-faltantes)])
          
#Creacion de clase tipo partido con su show que muestra los atributos de cada objeto especificamente.
#Creacion de matrizes con Trues y Falses para uso en el tabulate, faltantes siendo lo que sobra de la division capacity/10


