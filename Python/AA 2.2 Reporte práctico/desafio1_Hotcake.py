def preparar_hotcake():
    return "🥞"

def ordenar_hotcake(numero_piezas):
    piezashc = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezashc

hotcake_familia = ordenar_hotcake(int(input('Ingrese el número de tu familia: ')))
print(hotcake_familia)
