def preparar_cafe():
    return "Cafe"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(int(input('Ingrese tu orden: ')))
print(cafe_grupo_a)

