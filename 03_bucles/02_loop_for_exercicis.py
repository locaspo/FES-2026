###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
print("\n---EX 1---")
for i in range (2,21,2):
    print(i)
# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
print("\n---EX 2---")
numeros = [10, 20, 30, 40, 50]
suma = 0
for i in numeros:
    suma += numeros[i]
    media = suma/5

print(f"Media: {media}.")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
print("\n---EX 3---")
numeros = [15, 5, 25, 10, 20]
temp = numeros[0]
for i in numeros:
    if (temp < numeros[i]):
        temp = numeros[i]

print(f"Maxim: {temp}")


# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
print("\n---EX 4---")
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]

llista = []

for paraula in paraules:
    if len(paraula) > 5:
        llista.append(paraula)

print(llista)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
print("\n---EX 5---")

paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
contador = 0
lletra = input("Introdueix una lletra").strip().lower()

for lletra in paraules:
    if paraula.startswith(lletra):
        contador += 1

print(f"Hi ha {contador} paraules que comencen per la lletra '{lletra}'.")