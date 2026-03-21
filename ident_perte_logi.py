palabra_adivinar = "Ingeniero"

def adivinar_palabra(letra_prueba, palabra_intento):


    letra_en_palabra = letra_prueba in palabra_adivinar
    
    print("¿La letra de prueba se encuentra en la palabra?", letra_en_palabra)

    
    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len(palabra_intento) == len(palabra_adivinar))

    print("El jugador gana:", resultado_adivinanza)
    
letra_prueba = input("Ingresa una letra: ")
palabra_intento = input("Intenta adivinar la palabra: ")

adivinar_palabra(letra_prueba, palabra_intento)