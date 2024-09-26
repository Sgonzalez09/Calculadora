
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

