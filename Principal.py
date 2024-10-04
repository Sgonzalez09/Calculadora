#funciones
def restar():
 
    a = 0
    b = 0
 
    while(a<=0):
        a=float(input("Digite un numero positivo y mayor a 0: "))
    while(b>a or b<=0):
        b=float(input("Digite otro numero mayor a 0 y menor al primero para realizar la resta: "))
 
    c=a-b
 
    print("\nEl resultado de la resta es: ", c)
 
 
def multiplicacion ():
 
    a=float(input("Digite un número: "))
    b=float(input("Digite otro número: "))
 
    c = a*b
 
    print ("\nEl resultado de multiplicar ", a, " y ", b , " es ", c)
 
def suma ():
 
    a=float(input("Digite un número: "))
    b=float(input("Digite otro número: "))
 
    c = a+b
    print("\nEl resultado de la suma es: ", c)
 
 
#menú
 
print("<<Bienvenido a calculadora básica de dos números>>")
print("\n1. Suma \n2. Resta \n3. Multiplicación")
r = int (input ("\n¿Qué opción deseas? "))

while (r > 0 or r <3):
    if (r ==1):
        suma()
        break

        
 
    elif r == 2:
        restar()
        break
 
    elif r == 3:
        multiplicacion()
        break
 
    else:
        r = int (input("Opción fuera de rango, por favor intentelo de nuevo: "))
 
 