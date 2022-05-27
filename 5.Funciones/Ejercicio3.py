def aniobisiesto():
  anio = int(input("Introduce un año cualquiera: "))
  if anio % 4 == 0 and anio % 100 != 0:
    print(anio, "Es un año bisiesto")
  else:
    print(anio, "No es un año bisiesto")

print(aniobisiesto())
