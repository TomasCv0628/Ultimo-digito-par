"""Programa para descubrir si es ultimo digito de una secuencia de números
es par o no es par"""

print("\n☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯")
print("☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯")
print("☯☯☯☯☯☯☯☯☯ Ultimo digito ☯☯☯☯☯☯☯☯☯")
print("☯☯☯☯☯☯☯☯☯☯☯☯☯☯ PAR ☯☯☯☯☯☯☯☯☯☯☯☯☯☯")
print("☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯")
print("☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯☯" + "\n")


# input
X = int(input("Inserte un número: "))

# processing

r = X % 10

if r % 2 == 0:
    msj = (" es par ")
else:
    msj = (" no es par ")

# output

print(" \nEl ultimo digito del valor " + str(X) + msj)

