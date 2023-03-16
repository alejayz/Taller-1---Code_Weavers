x : float
Velocidad_Luz : float = 3e8
Velocidad_Sonido : float = 343.2 
Velocidad_Vehículo : float = 141.1
Velocidad_Bolt : 12.4

x = float(input("ingrese una distancia en metros: "))

Tluz = x/3e8
print("la luz se tardaría " + str(Tluz) + " segundos en recorrer " + str(x))

TSonido = x/343.2
print("el sonido se tardaría " + str(TSonido) + " segundos en recorrer " + str(x))

TVehículo = x/141.1
print("el vehículo se tardaría " + str(TVehículo) + " segundos en recorrer " + str(x))

TBolt = x/12.4
print("Bolt se tardaría " + str(TBolt) + " segundos en recorrer " + str(x))

