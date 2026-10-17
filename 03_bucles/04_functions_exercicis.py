###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("\n---EX 1---")
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}.")

saludar_a("Lara")

def saludar_b(nom, salutacio):
    print(f"{salutacio}, {nom}.")

saludar_b("Lara", "Bon dia")


# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
print("\n---EX 2---")
def es_parell(numero):
    if numero % 2 ==0:
        return True
    else:
        return False

es_parell(2)
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
print("\n---EX 3---")
def mitjana(numeros):
    suma = 0
    for num in numeros:
        suma += num
    
    return suma/len(numeros)
    

nums = [10, 15, 20, 25, 30]
resultado = mitjana(nums)

print(f"Mitjana: {resultado}")

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
print("\n---EX 4---")
def sumar_tot(*args):
    total = 0 
    for num in args:
        total += num
    return total


res_2 = sumar_tot(10, 20)
print(f"Suma de 2 números: {res_2}")

res_5 = sumar_tot(1, 2, 3, 4, 5)
print(f"Suma de 5 números: {res_5}")

res_10 = sumar_tot(1, 1, 1, 1, 1, 2, 2, 2, 2, 2)
print(f"Suma de 10 números: {res_10}")

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
print("\n---EX 5---")
def taula_multiplicar(numero, limit=10):
    for i in range (0, limit+1, 1):
        print(numero*i)

taula_multiplicar(5)
# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
print("\n---EX 6---")
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom="Lucas", edad="19", grau="Enginyeria en Telecos")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
print("\n---EX 7---")

def factorial(num):
    fact = 1 
    while (num>0):
        fact *= num
        num -= 1 
    return fact

def maxim(numeros):
    max = numeros[0]
    for i in numeros:
        if (max < i):
            max = i
    return max

fact = factorial(5)
numeros = [10, 15, 20, 25, 30]
maximo = maxim(numeros)

print(f"Factorial de 5: {fact}.\n Maxim de la llista: {maximo}.")
