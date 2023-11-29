

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

def calculadora():
    operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "+":
        resultado = suma(num1, num2)
    elif operacion == "-":
        resultado = resta(num1, num2)
    elif operacion == "*":
        resultado = multiplicacion(num1, num2)
    elif operacion == "/":
        resultado = division(num1, num2)
    else:
        resultado = "Error: Operación no válida"

    print("El resultado de la operación es:", resultado)
    ultimo_resultado = resultado

    return ultimo_resultado

while True:
    calculadora()
    seguir = input("¿Desea realizar otra operación? (s/n): ")
    if seguir == "s":
        ultimo_resultado = calculadora()
    else:
        break