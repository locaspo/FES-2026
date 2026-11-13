###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("Nom tècnic: ")
nom_xarxa = input("Nom xarxa: ")

print(f"Nom del tècnic: {nom_tecnic}. \nNom de la xarxa: {nom_xarxa}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

logitud_enllac = float(input("Introdueix longitud enllac en km: "))
velocitat_transmissio = float(input("Introdueix la velocitat de transmissió en Gbps: "))

temps = 8/velocitat_transmissio

print(f"Temps de transmisio: {temps} segons.")
# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores = int(input("Introduexi el nombre d'hores de feina: "))
preu_hora = float(input("Introdueix preu per hora de la instalació: "))
preu_material = float(input("Introdueix el preu del material: "))

total = hores*preu_hora + preu_material

print(f"Total instalació {total} €.")