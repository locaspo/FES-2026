###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
print("\n---EX 1---")
i = 10
while (i>0):
    print(f"{i} ")
    i -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
print("\n---EX 2---")
i_2 = 0
suma = 0 
while(i_2<=20): 
    suma += i_2
    i_2 += 2 

print(f"Total = {suma}. ")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\n---EX 3---")
enter = int(input("Introdueix un nombre enter positiu: "))
fact = 1 

while (enter>0):
    fact *= enter
    enter -= 1 

print(f"Factorial: {fact}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
print("\n---EX 4---")
contrasenya = input("Introdueix la contraenya de almenys 8 caràcters: ")
while len(contrasenya) < 8:
    print("Contrasenya no compleix els requisits.")
    contrasenya = input("Introdueix la contraenya de almenys 8 caràcters: ")

print("Contrasenya vàlida.")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
print("\n---EX 5---")
num = int(input("Introdueix un numero: "))

i_5 = 1
while i_5 < 11:
    print(f"{num*i_5}")
    i_5 += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
print("\n---EX 6---")
n = int(input("Introdueix numero enter positiu: "))
i_6 = 2
while(i_6 < n):
    es_primo = True
    j = 2

    while j * j <= i_6:
        if i_6 % j == 0:
            es_primo = False
            break
        j += 1
        
    if es_primo:
        print(i_6)
        
    i_6 += 1