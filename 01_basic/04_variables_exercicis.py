###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom = "Enc-1"
ubicacio = "Biblioteca"
nombre_ports = 12
esta_ences = True

print(f"L'encaminador {nom}, ubicat en {ubicacio}, te {nombre_ports} ports i el seu estat d'encesa és {esta_ences} ")
# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos = 120
gb_consumits = 79

print(f"Queden {gb_inclosos - gb_consumits} GB.")

gb_consumits_nou = 23

print(f"Ara queden {gb_inclosos - gb_consumits - gb_consumits_nou} GB.")