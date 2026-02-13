# variables numericas
entero = 2 
print("Integer:", entero)
print("Tipo de variable enteros:", type(entero))

decimal = 2.5
print("Float:", decimal)
print("Tipo de variable float:", type(decimal))

booleano = True
print("Booeano",booleano)
print("Tipo de variable boolean:",booleano)

cadena = "Hola, Mundo"
print("Cadenas:",cadena)
print("Tipo de caruable string",type(cadena))

def pedirNumero(texto):
    print(texto)
    numero = input()
    return numero

def imprimirEdad():
    edad = pedirNumero("Introduce tu edad")
    if edad < 18:
        print("Eres menor de edad")
    else: 
        print("Eres mayor de edad")
imprimirEdad()