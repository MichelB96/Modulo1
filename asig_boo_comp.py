def longitudpalabra(palabra1, palabra2):
    long1 = len(palabra1)
    long2 = len(palabra2)
    return long1 == long2

palabra1 = "perro"
palabra2 = "gato"

palabras = longitudpalabra(palabra1, palabra2)

print(f"Son {palabra1} y {palabra2} dos palabras de la misma longitud? {palabras}")