
saldo = 500000
saldo_minimo = 10000
while True: 
 print("\n1 - Retirar dinero")
 print("2 - consultar saldo")
 print("3 - salir")
 opcion = input("Seleccione una opcion:")
 if opcion == "1":
   print ("Hacer retiro")
    
   try:
      monto = int(input ("dijite el monto a retirar"))
   except ValueError:
   
      print("Ingrese un monto valido")
      
      continue
   if monto <= 0:
      print ("monto incorrecto")

   elif saldo - monto >= saldo_minimo:
      saldo = saldo - monto
      print("Su nuevo saldo es:", saldo)
   
   else:
    print("saldo insuficiente o debe mantener el saldo minimo")

   
 elif opcion == "2":
  print("Su saldo actual es:", saldo)

 elif opcion == "3":
   print("Gracias por utilizar el cajero")
   break
 else:
  print("Opción inválida. Seleccione 1, 2 o 3.")
 

    
    





    
