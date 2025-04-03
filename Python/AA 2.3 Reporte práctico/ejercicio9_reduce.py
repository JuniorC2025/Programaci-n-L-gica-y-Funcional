











from functools import reduce

jugadores = [

    {"nombre":"Brandon", "Edad":22},
    {"nombre":"Alana", "Edad":23},
    {"nombre":"Oso", "Edad":24},
    {"nombre":"Kafai", "Edad":25}
]

suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador["Edad"], jugadores, 0)

print(suma_edades)