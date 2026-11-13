###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
print("---EX 1---")
senyal = float(input("Introdueix el nivell de senyal: "))
if senyal >= -50:
    cobertura = "excel·lent"
elif senyal >= -67:
    cobertura = "bona"
elif senyal >= -75:
    cobertura = "feble"
else:
    cobertura = "molt feble"

print(f"La cobertura es {cobertura}.")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
print("\n---EX 2---")
recepcio = float(input("Introdueix el nivell de recepcio: "))
if recepcio < -27:
    nivell = "baix"
elif -27 <= recepcio <= -8:
    nivell = "acceptable"
elif recepcio > -8:
    nivell = "massa alt"

print(f"El nivell és {nivell}.")


# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
print("\n---EX 3---")
pla = 20
consum = float(input("Introdueix el teu consum de dades: "))

if consum <= pla:
    print("Consum dins del límit.")
else:
    print(f"S'han consumit {consum - pla} addicionals al pla.")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
print("\n---EX 4---")
los_ences = input("L'indicador LOS del terminal òptic està encès? (y/n): ")
internet_ences = input("L'indicador d'Internet del router està encès? (y/n): ")

if los_ences == "y":
    diagnostic = "Cal revisar el cable de fibra."
elif internet_ences == "n":
    diagnostic = "Cal comprovar el servei del proveïdor."
else:
    diagnostic = "La connexió sembla funcionar correctament."

# Mostrem el resultat
print(f"\nDiagnòstic: {diagnostic}")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
print("\n---EX 5---")
bateria = float(input("Introdueix el percentatge de bateria: "))

if bateria < 0 or bateria > 100:
    print("Error: El percentatge ha d'estar entre el 0% i el 100%.")
elif 0 <= bateria < 20:
    print(f"Nivell de bateria crític ({bateria}%).")
elif 20 <= bateria < 50:
    print(f"Nivell de bateria baix ({bateria}%).")
else:
    print(f"Nivell de bateria suficient ({bateria}%).")

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
print("\n---EX 6---")
latencia = float(input("Introdueix la latència: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Error: Valors d'entrada fora de rang.")
elif latencia <= 30 and perdua <= 1:
    print("Qualitat de la connexió: excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("Qualitat de la connexió: bona")
elif latencia <= 150 and perdua <= 5:
    print("Qualitat de la connexió: acceptable")
else:
    print("Qualitat de la connexió: deficient")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
print("\n---EX 7---")
pla = input("Introdueix el tipus de pla bàsic o plus (b/p): ")
consum = float(input("Introdueix el consum mensual (GB): "))

if consum < 0 or (pla != "b" and pla != "p"):
    print("Error: Consum negatiu o tipus de pla desconegut.")
elif pla == "b"
    preu_base = 10
    limit = 10
    preu_extra = 1.5
    
    if consum > limit:
        cost_total = preu_base + (consum - limit) * preu_extra
    else:
        cost_total = preu_base
        
    print(f"Cost total del pla bàsic: {cost_total:.2f} €")
else: 
    preu_base = 20
    limit = 30
    preu_extra = 0.75
    
    if consum > limit:
        cost_total = preu_base + (consum - limit) * preu_extra
    else:
        cost_total = preu_base
        
    print(f"Cost total del pla plus: {cost_total:.2f} €")
# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
print("\n---EX 8---")

compte_actiu = input("El compte està actiu? (s/n): ")

if compte_actiu != "s":
    print("Accés denegat: el compte està desactivat.")
else:
    contrasenya_correcta = input("La contrasenya és correcta? (s/n): ")
    
    if contrasenya_correcta != "s":
        print("Accés denegat: la contrasenya és incorrecta.")
    else:
        codi_correcte = input("El codi de doble verificació és correcte? (s/n): ")

        if codi_correcte == "s":
            print("Accés permès.")
        else:
            print("Accés denegat: el codi de doble verificació és incorrecte.")

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

print("\n---Exercici 9---")
router_ences = input("El router està encès? (s/n): ").strip().lower()

if router_ences != "s":
    print("Cal encendre el router.")
else:
    # Només demanem l'estat dels LED si el router ja està encès
    los_ences = input("L'indicador LOS està encès? (s/n): ").strip().lower()
    
    if los_ences == "s":
        print("Cal revisar el cable de fibra.")
    else:
        internet_ences = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()
        
        if internet_ences != "s":
            print("Cal contactar amb el proveïdor.")
        else:
            print("La connexió funciona correctament.")

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
print("\n---Exercici 10---")

servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Quants usuaris estan afectats? "))

if usuaris < 0:
    print("El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n): ").strip().lower()

    # Agrupem la lògica: si compleix alguna de les dues condicions I no hi ha alternativa
    if (servei_critic == "s" or usuaris >= 50) and alternativa != "s":
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")