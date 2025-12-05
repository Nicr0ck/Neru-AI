def calculadora():
    print("Calculadora Simple")
    numero1 = float(input("Ingrese el primer número: "))
    operacion = input("Ingrese la operación deseada (+, -, *, /): ")
    numero2 = float(input("Ingrese el segundo número: "))

    if operacion == "+":
        resultado = numero1 + numero2
        print(f"El resultado es: {resultado}")
    elif operacion == "-":
        resultado = numero1 - numero2
        print(f"El resultado es: {resultado}")
    elif operacion == "*":
        resultado = numero1 * numero2
        print(f"El resultado es: {resultado}")
    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado es: {resultado}")
        else:
            print("No se puede dividir por cero.")
    else:
        print("Operación inválida. Por favor, ingrese una operación válida (+, -, *, /)")

calculadora()