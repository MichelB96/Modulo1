
def calcular_calorias(carbohidratos, proteinas, grasas):
    # Cada gramo de carbohidrato = 4 calorías
    # Cada gramo de proteína = 4 calorías
    # Cada gramo de grasa = 9 calorías
    
    calorias = (carbohidratos * 4 + proteinas * 4 + grasas * 9)
    return calorias

calorias1 = calcular_calorias(45, 60, 18)

print("Total de Calorias:", calorias1)
