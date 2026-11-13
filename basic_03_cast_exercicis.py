###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets = input("Nombre de paquets rebuts: ")
total = int(paquets) + 1200
print("Total: ", total)
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
mbps = input("Velocitat en mbps: ")
MBs = float(mbps)/8
print(f"Conversio: {MBs} MB/s ")