#Juego tierra de dragones

import random
import time

#Funcion que anuncia la introduccion de la historia
def mostrarIntroduccion():
    print("Estas en una tierra llena de dragones. Frente a ti")
    print("hay dos cuevas. En una de ellas, el dragon es generoso y")
    print("amigable y compartira su tesoro contigo. El otro dragon")
    print("es codicioso y hambriento, y te devorara inmediatamente.")
    print()
#Fin de la funcion mostrarIntroduccion

#Funcion que le pide al usuario escoger una de dos opciones y la opcion se guarda en una variable
def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        cueva = input("¿A que cueva quieres entrar? (1 o 2): ")
    return cueva 
#Fin de la funcion elegirCueva

#Funcion que toma un argumento y dependiendo del valor te indica si ganaste un tesoro o te come el dragon
def explorarCueva(cuevaElegida):
    print("Te aproximas a la cueva...")
    time.sleep(2)
    print("Es oscura y espeluznante...")
    time.sleep(2)
    print("¡Un gran dragon aparece subitamente frente a ti! Abre sus fauces...")
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
        print("Te regala un tesoro!!!")

    else:
        print("Te come de un bocado!!!")
#Fin de la funcion explorarCueva

#Variable que tiene el valor 'si' por defecto la cual hara que entre en el bucle while y active el juego
jugarDeNuevo = 'si'

#Bucle que activa el juego la primera vez
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroduccion()

    numeroDeCueva = elegirCueva()

    explorarCueva(numeroDeCueva)

    jugarDeNuevo = input("Quieres jugar de nuevo?? (si o no): ")
