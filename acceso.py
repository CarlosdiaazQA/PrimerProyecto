while True:
    nombre = input("Cual es su nombre: ")
    if nombre.isdigit() or nombre == "":

     print("debe ingresar su nombre")
    else:
        break
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
    
     print("Valor incorrecto. Ingrese su edad sin letras ni decimales. Ejemplo: 18")     

if edad <0 or edad >120:
     print ("Edad invalida por favor introduzca edad valida")     
elif edad <=17:
     print("Acceso denegado")
else:
    print("Acceso permitido")
    

   




