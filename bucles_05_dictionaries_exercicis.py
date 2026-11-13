###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
print("\n---EX 1---")

estudiant = {
    "nom": "Marc",
    "edat": 20,
    "assignatures": ["CiCE", "FES", "RiOG"]
}

print(estudiant)

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.
print("\n---EX 2---")
asignatura_2 = estudiant["assignatures"][1]
estudiant["edat"] = 10
print(estudiant)

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
print("\n---EX 3---")
estudiant["aprovades"] = 3
del estudiant["edat"]
print(estudiant)

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print("\n---EX 4---")
nom = "nom" in estudiant
email = "email" in estudiant
print(f"Nom en estudiant: {nom}.\nEmail en estudiant: {email}.")

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
print("\n---EX 5---")

for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
print("\n---EX 6---")
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]

comptador = {}

for paraula in paraules:
    if paraula in comptador:
        comptador[paraula] += 1
    else: 
        comptador[paraula] = 1

print(comptador)