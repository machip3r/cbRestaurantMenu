# Funcion para solicitar la clave
def solicitarClave():
  password = input("Por favor, introduce tu clave: ")
  
  return password

# Declaración de variables
decision = 0
decision_propina = 0
decision_propina_pago = 0
decision_recarga = 0
porcentaje_propina = 0
propina = 0
saldo = 1000
total = 0
total_adulto = 0
total_nino = 0
veces_recarga = 0

# Bienvenida
print("\n Bienvenido! \n")
# Solicitar clave
password = solicitarClave()

# Clave no sea nula
while(password == ""):
  password = solicitarClave()

# Salto línea
print("\n")

# Mostrar el saldo disponible
print("\n Saldo disponible: $" + str(saldo) + " \n")
# Menú
print("Con tu tarjeta de prepago puedes realizar lo siguiente: \n")
while(decision != 9):
  # Menú adulto
  print("Menú adulto:")
  print("\t 1.- Caldo de frijol - $50")
  print("\t 2.- Carne asada - $100")
  print("\t 3.- Café de olla - $20 \n")
  # Menú niño
  print("Menú niño:")
  print("\t 4.- Sandwich - $50")
  print("\t 5.- Pizza con piña - $100")
  print("\t 6.- Yakult - $10 \n\n")
  # Otras opciones
  print("7.- Pagar \n\n")
  print("8.- Recarga de tarjeta \n")
  print("9.- Salir \n")

  # Lectura de dato
  decision = int(input("Introduce el número de opción: "))

  # Sentencia if (Switch Type)
  if decision == 1:
    print("Perfecto, en un momento le llegará su caldo \n\n")
    # Cargar precio al total
    total_adulto += 50
  elif decision == 2:
    print("La mejor de todas las carnes, en breve se le dará \n\n")
    # Cargar precio al total
    total_adulto += 100
  elif decision == 3:
    print("Siempre es bueno para una buena charla, que lo disfrute \n\n")
    # Cargar precio al total
    total_adulto += 20
  elif decision == 4:
    print("Para el pequeño lo que pida, su sandwich disfrutará \n\n")
    # Cargar precio al total
    total_nino += 50
  elif decision == 5:
    print("La piña es mejor con pizza, o ¿cómo era?, que la disfrutes \n\n")
    # Cargar precio al total
    total_nino += 100
  elif decision == 6:
    print("Lactobacillus casei Shirota, rico rico \n\n")
    # Cargar precio al total
    total_nino += 10
  elif decision == 7:
    # Calcular el pago total
    total = total_adulto + total_nino;
    # Verificar si tiene saldo suficiente para pagar
    if(total > saldo):
      print("No cuenta con el saldo suficiente para pagar...")
      print("Por favor vaya a la opción de recarga de tarjeta.\n\n")
    else:
      # Propina
      print("¿Desea dejar propina? \n")
      # Lectura de dato
      decision_propina = int(input("\n1.- Si\n2.- No \n\n "))
      # Sentencia if (Switch Type)
      if decision_propina == 1:
        while (porcentaje_propina < 10):
          # Porcentaje de propina
          print("¿Qué porcentaje dejará? (mayor a 10%) \n")
          # Lectura de dato
          porcentaje_propina = int(input("%: "))
        # Calcular la propina
        propina = (porcentaje_propina * total) / 100
        # Autorización del cliente para descontar la propina
        print("¿Autoriza descontar la propina de su tarjeta prepago también? \n")
        # Lectura de dato
        decision_propina_pago = int(input("\n1.- Si\n2.- No \n\n "))
        # Sentencia if (Switch Type)
        if(decision_propina_pago == 1):
          # Cargar precio al total
          total += propina
          # Mostrar los pagos totales
          print("El gasto total en comida de adulto es de $" + str(total_adulto) + "\n")
          print("El gasto total en comida de adulto es de $" + str(total_nino) + "\n")
          print("La propina que se le descontará en su tarjeta es de $" + str(propina) + "\n")
          print("El pago total es de $" + str(total) + "\n\n")
          print("Gracias por su compra!")
          # Restar el pago total del saldo
          saldo -= total
          # Salir del ciclo while
          decision = 9
        elif(decision_propina_pago == 2):
          # Mostrar los pagos totales
          print("El gasto total en comida de adulto es de $" + str(total_adulto) + "\n")
          print("El gasto total en comida de niño es de $" + str(total_nino) + "\n")
          print("La propina que pagará en efectivo es de $" + str(propina) + "\n")
          print("El pago total es de $" + str(total) + "\n\n")
          print("Gracias por su compra!")
          # Restar el pago total del saldo
          saldo -= total
          # Salir del ciclo while
          decision = 9
        else:
          print("\n\n Opción no válida. No se descontará de su tarjeta.\n\n")
      elif decision_propina == 2:
          # Mostrar los pagos totales
          print("El gasto total en comida de adulto es de $" + str(total_adulto) + "\n")
          print("El gasto total en comida de niño es de $" + str(total_nino) + "\n")
          print("El pago total es de $" + str(total) + "\n\n")
          print("Gracias por su compra!")
          # Restar el pago total del saldo
          saldo -= total
          # Salir del ciclo while
          decision = 9
      else:
        # Mensaje de opción no válida
        print("\n\n Opción no válida. No dejará propina.\n\n")
  elif decision == 8:
    # Recarga
    print("¿Cuánto desea recargar a su tarjeta prepago? \n")
    # Lectura de dato
    decision_recarga = int(input("\n1.- $100\n2.- $250 \n3.- $500 \n\n "))
    # Sentencia if (Switch Type)
    if(decision_recarga == 1):
      # Cargar recarga al saldo
      saldo += 100
      # Mostrar el saldo disponible
      print("Ahora su saldo disponible es de: $" + str(saldo) + "\n\n")
    elif(decision_recarga == 2):
      # Cargar recarga al saldo
      saldo += 250
      # Mostrar el saldo disponible
      print("Ahora su saldo disponible es de: $" + str(saldo) + "\n\n")
    elif(decision_recarga == 3):
      # Cargar recarga al saldo
      saldo += 500
      # Mostrar el saldo disponible
      print("Ahora su saldo disponible es de: $" + str(saldo) + "\n\n")
      veces_recarga += 1
      # Bonificación de $100
      if(veces_recarga == 3):
        saldo += 100
        print("Usted ha recargado $500 3 veces, esto lo hace acreedor a $100 más. Felicidades!\n\n")
        veces_recarga = 0
        # Mostrar el saldo disponible
        print("Ahora su saldo disponible es de: $" + str(saldo) + "\n\n")
    else:
      # Mensaje de opción no válida
      print("\n\n Opción no válida. No se recargará nada a su tarjeta.\n\n")
  elif decision == 9:
    # Salto de línea
    print("\n")
  else:
    # Mensaje de opción no válida
    print("\n\n Opción no válida. Inténtalo de nuevo.\n\n")

# Si el pago total es mayor a 500 y dejó propina dar internet gratis
if(total > 500 and propina != 0):
  print("Puede gozar de internet gratis por cortesia de la casa. Disfrute! \n\n")
# Mostrar el saldo disponible
print("\n Saldo disponible: $" + str(saldo) + " \n")
# Despedida
print("Adiós!")