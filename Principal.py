#funciones
def restar():
 
    a = 0
    b = 0
 
    while(a<0 or a==0):
        a=float(input("Digite un numero positivo y mayor a 0: "))
    while(b>a or b==0):
        b=float(input("Digite otro numero menor al primero para realizar la resta: "))
 
    c=a-b
 
    print("El resultado de la resta es: ", c)
 
 
def multiplicacion ():
 
    a=float(input("Digite un número: "))
    b=float(input("Digite otro número: "))
 
    c = a*b
 
    print ("El resultado de multiplicar ", a, " y ", b , " es ", c)
 
def suma ():
 
    a=float(input("Digite un número: "))
    b=float(input("Digite otro número: "))
 
    c = a+b
 
 
#menú
 
print("<<Bienvenido a calculadora básica de dos números>>")
print("1. Suma \n 2.Resta \n 3. Multiplicación")
r = input ("¿Qué opción deseas?")
while (r < 0 or r >3):
    if (r ==1):
        suma()
 
    elif r == 2:
        restar()
 
    elif r == 3:
        multiplicacion()
 
    else:
        r = input("Opción fuera de rango, por favor intentelo de nuevo")
 
 