while True:
    print("\n--- menu ---")
    print("1. saludar")
    print("2. sumar dos numeros")
    print("3. salir")

    opcion = input("seleccione una opcion: ")

    if opcion== "1":
        nombre = input("¿cual es tu nombre? ")
        print("hola", nombre)

    elif opcion == "2":
        numero1 = int(input("digite el primer numero: "))

        numero2 = int(input("digite el segundo numero "))
        resultado = numero1 + numero2
        print("el resultado es:", resultado)

    elif opcion =="3":
        print("programa finalizado")
        break

    else:
        print("opcion incorrecta")