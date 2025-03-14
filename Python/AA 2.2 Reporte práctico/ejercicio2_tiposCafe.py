def preparar_cafe_ame():
    return "cafe_americano"

def preparar_cafe_olla():
    return "cafe de olla"

def ordenar_cafe(preparar, numero_tazas):
    tazas_cafe = [preparar for _ in range(numero_tazas)]
    return tazas_cafe


cafe_grupo_a = ordenar_cafe(preparar_cafe_olla(),int(input('Ingrese tu orden: ')))

cafe_grupo_b = ordenar_cafe(preparar_cafe_ame(), int(input('Ingrese tu orden: ')))
print(cafe_grupo_a)
print(cafe_grupo_b)
