def leer():
	print("")

def ausgabe():
	print("Ausgabe von Text aus einer Funktion")
ausgabe()
ausgabe()
ausgabe()
print("Programm abgelaufen")
leer()

def ausgabe1(wert1):
	print("Ausgabe von Text aus einer Funktion")
	print(wert1)
ausgabe1(555)
print("Programm abgelaufen")
leer()

def ausgabe2(wert10,wert11):
	print("Ausgabe von Text aus einer Funktion")
	print(wert10)
	print(wert11)
ausgabe2(444,555)
print("Programm abgelaufen")
leer()

def add(a,b):
	print("Ausgabe von Text aus einer Funktion")
	return a * b
print(add(6,6))
print("Programm abgelaufen")
leer()

def add1(z1,z2):
	print("Ausgabe von Text aus einer Funktion")
	result = z1 * z2
	return result
print(add1(12,12))
print("Programm abgelaufen")
leer()

def add2(x,y):
	z = x * y
	return z
result = add2(55,55)
print(result)
result1 = add2(result,result)
print(result1)
print(result + 5000000)
print("Programm abgelaufen")
leer()

def add2(zahl1,zahl2):
        return zahl1 + zahl2
result = add2(55,55)
result1 = add2(result,2)
print(result)
print(result1)
print("")
