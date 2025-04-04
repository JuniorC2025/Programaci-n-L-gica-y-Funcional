
from functools import reduce

ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000]
tipoCambio = 20.46

prom = reduce(lambda acumulador, venta: acumulador + venta, ventas, 0) / len(ventas)

ventaMap = list(map(lambda venta: round(venta/tipoCambio), ventas))

mayor150 = list(filter(lambda venta: venta > 150, ventaMap))

sumaventas = reduce(lambda acumulador, venta: acumulador + venta, mayor150, 0)


print("El promedio de ventas en pesos mexicanos: ", round(prom))
print("Las ventas de la semana en dolares: " , ventaMap)
print("Las ventas en dólares mayores a 150:  ", mayor150)
print("La suma total de las ventas en dólares mayores a 150:  ", sumaventas)

