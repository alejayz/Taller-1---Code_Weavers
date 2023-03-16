# indicar el número mayor
a : float
b : float
c : float
a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un numero: "))
c = float(input("Ingrese un numero: "))

if a > b and b > c:
  print("El numero " + str(a) + " es el mayor")
elif a < b and b > c:
  print("El numero " + str(b) + " es el mayor")
else:
  print("El numero " + str(c) + " es el mayor")



# indicar si el primero es multiplo del segundo
a : float
b : float
a = float(input("ingrese el primer número: "))
b = float(input("ingrese el segundo número: "))

if a % b == 0 :
    print(str(a) + " es múltiplo de " + str(b))
else:
    print(str(a) + " no es múltiplo de " + str(b))



# indicar si es vocal o consonante
x : str
x = str(input("ingrese una letra: "))

if x == "a" or x == "A":
    print("la letra " + str(x) + " es una vocal")
elif x == "e" or x == "E":
    print("la letra " + str(x) + " es una vocal")
elif x == "i" or x == "I":
    print("la letra " + str(x) + " es una vocal")
elif x == "o" or x == "O":
    print("la letra " + str(x) + " es una vocal")
elif x == "u" or x == "U":
    print("la letra " + str(x) + " es una vocal")
else:
    print("la letra " + str(x) + " es una consonante")



# ingresar frecuencia en hz e indicar donde se encuentra
x : float
x = float(input("ingresa frecuencia en hz: "))

if x < 30E3:
    print("la frecuencia " + str(x) + " se encuentra en Muy Baja Frecuencia - Radio")
elif x > 30E3 and x <= 650E3:
    print("la frecuencia " + str(x) + " se encuentra en Onda Larga - Radio")
elif x > 650E3 and x <= 1.7E6:
    print("la frecuencia " + str(x) + " se encuentra en Onda Media - Radio")
elif x > 1.7E6 and x <= 30E6:
    print("la frecuencia " + str(x) + " se encuentra en Onda Corta - Radio")
elif x > 30E6 and x <= 300E6:
    print("la frecuencia " + str(x) + " se encuentra en Muy Alta Frecuencia - Radio")
elif x > 300E6 and x <= 3E8:
    print("la frecuencia " + str(x) + " se encuentra en Ultra Alta Frecuencia - Radio")
elif x > 3E8 and x <= 300E9:
    print("la frecuencia " + str(x) + " se encuentra en Microondas")
elif x > 300E9 and x <= 6.00E12:
    print("la frecuencia " + str(x) + " se encuentra en Infrarrojo lejano/submilimetrico")
elif x > 6.00E12 and x <= 120E12:
    print("la frecuencia " + str(x) + " se encuentra en Infrarrojo medio")
elif x > 120E12 and x <= 384E12:
    print("la frecuencia " + str(x) + " se encuentra en Infrarrojo cercano")
elif x > 384E12 and x <= 7.89E14:
    print("la frecuencia " + str(x) + " se encuentra en Espectro Visible")
elif x > 7.89E14 and x <= 1.5E15:
    print("la frecuencia " + str(x) + " se encuentra en Ultravioleta cercano")
elif x > 1.5E15 and x <= 30.0E15:
    print("la frecuencia " + str(x) + " se encuentra en Ultravioleta extremo")
elif x > 30.0E15 and x <= 30.0E18:
    print("la frecuencia " + str(x) + " se encuentra en Rayos X")
elif x > 30.0E18:
    print("la frecuencia " + str(x) + " se encuentra en Rayos gamma")
else:
    print("la frecuencia " + str(x) + "no se encuentra")
