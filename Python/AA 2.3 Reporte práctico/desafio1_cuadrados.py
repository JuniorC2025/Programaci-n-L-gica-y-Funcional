def cuadradosLista(arreglo):
    positivos = filter(lambda x: x > 0 and x == int(x), arreglo)
    cuadradosMap = map(lambda x: x ** 2, positivos)
    return list(cuadradosMap)

cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)