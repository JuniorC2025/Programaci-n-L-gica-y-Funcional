productos = ["Frijoles Refritos","Coca Cola","Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]


orden = sorted(productos)

ordenarCadena = ", ".join(orden)

slug = list(map(lambda nombre: nombre.lower().replace(" ", "-"), orden))

print(slug)
print()
print(ordenarCadena)