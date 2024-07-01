from itertools import permutations



def numero_vampiro(cedula):
    if len(cedula) %2 == 0:
        posibles_permutaciones = permutations(cedula)
        for permutacion in posibles_permutaciones:
            mitad_cedula = len(cedula) //2
            colmillo1 = int(''.join(permutacion[:mitad_cedula]))
            colmillo2 = int(''.join(permutacion[mitad_cedula:]))
            if colmillo1 * colmillo2 == int(cedula):
                return True

def numero_perfecto(cedula):
    divisores=[]
    acumulador=0
    for i in range(1,int(cedula)):
        if int(cedula) % i == 0:
            divisores.append(i)
    for divisor in divisores:
        acumulador += divisor

    if acumulador== int(cedula) and int(cedula) !="1":
        return True
                
    
def descuentovamp(cedula,monto):
    if numero_vampiro(cedula)== True:
       return monto - monto*0.5
    else:
        return monto
    
def descuentoperfecto(cedula,monto):
    if numero_perfecto(cedula)== True:
        return monto - monto*0.15
    else:
        return monto
    
def iva(monto): 
    return monto + monto*0.16
 
    
def factura(tipoentrada,subtotal,descuento,monto):
    if tipoentrada== "VIP":
        print("Factura VIP")
        print(f"Subtotal={subtotal}\nDescuento({descuento})\nIva(16%)\nMonto={monto}") 
    if tipoentrada== "GENERAL":
        print("Factura general")
        print(f"Subtotal={subtotal}\nDescuento({descuento})\nIva(16%)\nMonto={monto}")               

#Creacion de funciones requeridas para llevar a cabo con la creacion de las facturas con sus descuentos asignados.