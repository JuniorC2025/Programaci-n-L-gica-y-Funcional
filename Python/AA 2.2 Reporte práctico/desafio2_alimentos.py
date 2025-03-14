def preparar_pizza():
    return "🍕"

def preparar_hambuerguesa():
    return "🍔"

def preparar_Hotdog():
    return "🌭"

def calcular_bonus(num_porciones):
    if num_porciones >2:
        return "coca gratis"
    return ""

def ordenar_alimento(preparar_alimento, num_porciones):
    porciones = [preparar_alimento for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)
    return porciones, bonus




cafe_grupo_a = ordenar_alimento(preparar_pizza(),int(input('Ingrese tu orden: ')))

cafe_grupo_b = ordenar_alimento(preparar_hambuerguesa(), int(input('Ingrese tu orden: ')))
cafe_grupo_c = ordenar_alimento(preparar_Hotdog(), int(input('Ingrese tu orden: ')))


print(cafe_grupo_a)
print(cafe_grupo_b)
print(cafe_grupo_c)
