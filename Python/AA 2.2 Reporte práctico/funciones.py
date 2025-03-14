def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a, b): # Función de primer orden
    return a + b

def resta(a, b):
    return a - b

resultado = operar(5, 3, suma)  # Pasamos la función suma como argumento
print(resultado)



def saludo():
    return "¡Hola!"

mi_variable = saludo  # Asignamos la función a una variable
print(mi_variable())  # Llamamos a la función a través de la variable


def elegir_operacion(operacion): # Función de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicar  # Retornamos la función sin ejecutarla
    else:
        return dividir

doble = elegir_operacion("multiplicar")  # Devuelve la función multiplicar
print(doble(10))
divide2 = elegir_operacion("dividir")  # Devuelve la función dividir
print(divide2(10))

doble = lambda x: x * 2
print(doble(5))  # Salida: 10


numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8]

alumnos = ['Alejandro', 'miguel', 'vinicio', 'rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola ' + nombre, alumnos))
print(saludar_alumnos)

#sin lambda
def saludar(nombre):
    return 'hola ' + nombre

#usamos map con la función saludar
lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)


