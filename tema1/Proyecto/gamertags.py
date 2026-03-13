def cabecera():
    """Muestra la cabecera de la aplicación"""
    titulo = r"""  ______                                                __                         
 /      \                                              |  \                        
|  $$$$$$\  ______   ______ ____    ______    ______  _| $$_     ______    ______  
| $$ __\$$ |      \ |      \    \  /      \  /      \|   $$ \   |      \  /      \ 
| $$|    \  \$$$$$$\| $$$$$$\$$$$\|  $$$$$$\|  $$$$$$\\$$$$$$    \$$$$$$\|  $$$$$$
| $$ \$$$$ /      $$| $$ | $$ | $$| $$    $$| $$   \$$ | $$ __  /      $$| $$  | $$
| $$__| $$|  $$$$$$$| $$ | $$ | $$| $$$$$$$$| $$       | $$|  \|  $$$$$$$| $$__| $$
 \$$    $$ \$$    $$| $$ | $$ | $$ \$$     \| $$        \$$  $$ \$$    $$ \$$    $$
  \$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$         \$$$$   \$$$$$$$ _\$$$$$$$
                                                                         |  \__| $$
                                                                          \$$    $$
                                                                           \$$$$$$ 
                            Crea tu Identidad Gamer                                               
"""
    print(titulo)
cabecera()    

#Cabecera()

def crear_tag_basico(nombre):
    """
    Crea un Gamertag basico usando las primeras 4 letras del nombre.
    
    Parametro:
    nombre(str): El nombre del usuario
    
    Retorna:
    str: Gamertag basico
    
    """
    tag = nombre[0:4]
    return tag

#tag_basico = crear_tag_basico("Michel")
#print(tag_basico)

def crear_tag_invertido(nombre):
    """
    Crea un Gamertag invirtiendo el nombre completo 
    
    Parametro:
    str: El nombre del usuario 
    
    Retorna:
    str: Gamertag (nombre) invertido
    """
    tag = nombre[::-1]
    return tag
#tag_invertido = crear_tag_invertido ("Michel")
#print(tag_invertido)

def crear_tag_intercalado(nombre, apellido): 

    """ 

    Crea un gamertag combinando letras del nombre y apellido. 

    Ejemplo: nombre="Michel", apellido="Belmont" → "MBelmont" 

    Parámetros: 

    nombre (str): El nombre del usuario 

    apellido (str): El apellido del usuario 

    Retorna: 

    None (imprime directamente) 

    """ 
    tag = nombre[0]
    tag1 = apellido[0]
    tag2 =nombre[1:]
    tag3 = apellido[1:]

    print(tag, tag1, tag2,tag3, sep="")
crear_tag_intercalado( "Michel","Belmont")
pass
    
def crear_tag_elite(nombre): 

    """ 
    Crea un gamertag "elite" usando inicio y final del nombre. 

    Ejemplo: "Santiago" → "Sago" 

    Parámetro: 

    nombre (str): El nombre del usuario 
    
    Retorna: 

    None (imprime directamente) 

    """ 
    inicio = nombre[:3] 
    final = nombre[0:-2]
    print("4 TAG ELite", inicio, final, sep="")
    #pass
def crear_tag_con_numero(nombre, numero_favorito): 

    """ 
    Crea un gamertag añadiendo número al final. 

    Parámetros: 

    nombre (str): El nombre del usuario 

    numero_favorito (int): Número favorito del usuario 
    
    Retorna: 

    None (imprime directamente) 

    """ 
    print("5 Tag con numero ",nombre[:5],numero_favorito, sep="")
    
def mostrar_estadisticas(nombre):
    """
    Muestra Estadisticas del nombre proporcionado
    
    Parametro:
    Nombre(str): El nombre a analizar
    Retorna:
    None(Imorime directamente)
    """
    
    longitud_nombre = len(nombre)
    print("\nEstadisticas de tu nombre:")
    print("Nombre Completo:", nombre)
    print("Longitud del nombre:", longitud_nombre)
    print("Primera letra:", nombre[0])
    print("Ultima letra:", nombre[-1])
    
def generar_todas_las_funciones(nombre, apellido, numero):
    """
    Genera y Muestra todas las opciones de GamerTags
    
    Parametros:
    nombre(str): Nombre del usuario
    apellido(str): Apellido del usuario
    numero (str):  Número favorito del usuario
    
    Retorna:
    None (Imprime de manera directa)
    """
    print("\n================================================")
    print(" TUS OPCIONES DE GAMERTAG:")
    print("=============================================")
    
    tag_basico = crear_tag_basico(nombre)
    print("\1. TAG BASICO:", tag_basico)
    print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)
    
    print("\n=================================================")




#=========================
#Aplicación Principal
#=========================
#Llamar la función cabecera
cabecera()    

# Solicitar Datos al usuario
nombre = input("\n Introduce tu Nombre:  ")
apellido = input("Introduce tu Aepllido: ")
numero = input("Introduce tu número Favorito: ")

#Mostrar Estadisticas del Nombre

mostrar_estadisticas(nombre)
generar_todas_las_funciones(nombre,apellido,numero)

print("\n Elige tu favorito y conquista el mundo gamer")

