while True:
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: Suma")
    print("Ingrese la opción por favor:")
    opcion = int(input())
    if opcion <= 4 and opcion > 0:
        break

if opcion == 1:
    print("¡Bienvenido a la Opción Suma!")
    print("Ingrese el primer número:")
    num1 = float(input())
    print("Ingrese el segundo número:")
    num2 = float(input())
    resultado = num1 + num2

if opcion == 2:
    print("¡Bienvenido a la Opción Resta!")
    print("Ingrese el primer número:")
    num1 = float(input())
    print("Ingrese el segundo número:")
    num2 = float(input())
    resultado = num1 - num2

if opcion == 3:
    print("¡Bienvenido a la Opción Multiplicación!")
    print("Ingrese el primer número:")
    num1 = float(input())
    print("Ingrese el segundo número:")
    num2 = float(input())
    resultado = num1 * num2

if opcion == 4:
    print("¡Bienvenido a la Opción División!")
    print("Ingrese el primer número:")
    num1 = float(input())
    print("Ingrese el segundo número:")
    num2 = float(input())
    resultado = num1 / num2

print("El resultado de la operación es: ",resultado,"")