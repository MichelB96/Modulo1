def funcion_contarcaracteres(var1):
    
    """var1 denomina el cuerpo de la funcion para el numero de caracteres
       Dentro de la funcion len es para determinar la longitud de la cadena 
       
    """
    
    print(f"La frase '{var1}' tiene {len(var1)} caracteres. ") 
    
    """La funcion convertir_numero servira para un numero entero como argumento dentro de la variable var2
       Dentro de la funcion, al convierte el numero a cadena usando string (str) y a flotante (float)
       Imprime dentro de los print en cadena: en Entero, Cadena y Flotante
    
    """
    
def convertir_numero(var2):
    
    print(f"Entero {var2}, tipo: {type(var2)}")    
    print(f"Cadena {str(var2)}, tipo {type(str(var2))}")
    print(f"flotante {float(var2)}, tipo{type(float(var2))}")
    

funcion_contarcaracteres("En este dia soy feliz")    
convertir_numero (5)


    