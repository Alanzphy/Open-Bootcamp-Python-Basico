def numeroprimo():
  numero = int(input("Introduce un numero que sea entero: "))
  if numero > 1:
    for i in range(2, numero):
      if (numero % i) == 0:
        print(numero, "No es un numero primo")
        break
    else:
      print(numero, "Es un numero primo")

  else:
    print(numero, "El numero 1 no es un numero primo")

print(numeroprimo())



