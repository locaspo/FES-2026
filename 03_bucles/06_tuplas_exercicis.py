# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
print("\n---EX 1---")
ciutats = ("Barcelona", "Madrid", "València", "Sevilla", "Girona")

segona = ciutats[1]
penultima = ciutats[-2]

print(f"Segona ciutat: {segona}")
print(f"Penúltima ciutat: {penultima}")
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
print("\n---EX 2---")

nums = (1, 3, 5, 3, 8, 3, 9, 2)
tres = nums.count(3)

print(f"El número 3 apareix {tres} vegades a la tupla.")
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
print("\n---EX 3---")

def ordenar_tupla(numeros):
    return tuple(sorted(numeros))

tupla = (8, 3, 1, 5, 2, 9)
tupla_ordenada = ordenar_tupla(tupla)

print(f"Tupla ordenada: {tupla_ordenada}")