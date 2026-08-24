nombre = input("cual es tu nombre?")
edad = int(input("cuantos años tienes"))
print("hola", nombre)    
print("tienes", edad, "años")   
if edad < 18:
    print("eres menor de edad")
elif edad < 65:
    print("eres adulto")
else:
    print("eres adulto mayor")                