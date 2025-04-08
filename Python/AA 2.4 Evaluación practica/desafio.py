import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import reduce

# datos globales
# Lista de materias que serean evaluadas
asignaturas = [
    "Programación Lógica y Funcional",
    "Programación Web BackEnd",
    "Interacción y Diseño de Interfaces"
]

# Aspectos de cada materia que sere e valuaran
aspectos = [
    "Contenido de la materia",
    "Actividades prácticas",
    "Claridad del profesor",
    "Herramientas utilizadas"
]

# Aqui se guardaran las encuestas realizadas por los alumnos
encuestas = []

# FUNCIONES DE ESTADÍSTICA (FUNCIONES PURAS)

# Se encarga de calcular el promedio de la lista valores
def promedio(valores):
    return reduce(lambda acumulador, prom: acumulador + prom, valores) / len(valores) if valores else 0

# esta fución se encarga de sumar el total de la lista
def total(valores):
    return reduce(lambda acumulador, total: acumulador + total, valores) if valores else 0


# Encuentra el valor mínimo de una lista
def minimo(valores):
    return reduce(lambda acumulador, min: acumulador if acumulador < min else min, valores) if valores else 0

# encuentra el valor máximo de una lista
def maximo(valores):
    return reduce(lambda acumulador, max: acumulador if acumulador > max else max, valores) if valores else 0



# las siguientes fuciones se encargam del filtrado y analisis de las encuestas

# Filtrara las encuestas que correspondan a la materia dada
def Encuesta_Materia(materia):
    return list(filter(lambda acumulador: acumulador["materia"] == materia, encuestas))

# Filtrara las encuestas realizadas por un alumno
def encuesta_alumno(nombre):
    return list(filter(lambda acumulador: acumulador["nombre"].lower() == nombre.lower(), encuestas))

# Extraera una lista de los valores numéricos de un aspecto de un conjunto de encuestas
def valor_aspecto(encuestas_local, aspecto_key):
    return list(map(lambda acumulador: acumulador[aspecto_key], encuestas_local))

# Calculara el promedio, total, máximo y mínimo de cada aspecto por medio de las encuestas de una materia
def estadistica(encuestas_materia):
    resultado = {}
    for aspecto in aspectos:
        valores = valor_aspecto(encuestas_materia, aspecto)
        resultado[aspecto] = {
            "promedio": promedio(valores),
            "total": total(valores),
            "min": minimo(valores),
            "max": maximo(valores)
        }
    return resultado

# función recursiva para poder mostrar los resultaados 

# Recorre un diccionario de estadísticas de manera recursiva, llamandose a si misma
def formatear_resultados(diccionario, claves=None, i=0):
    if claves is None:
        claves = list(diccionario.keys())
    if i >= len(claves):
        return ""
    
    clave = claves[i]
    valor = diccionario[clave]
    
    if isinstance(valor, dict):
        resultado = f"\n{clave}:\n"
        for subclave in valor:
            resultado += f"  {subclave.capitalize()}: {valor[subclave]:.2f}\n"
    else:
        resultado = f"{clave}: {valor:.2f}\n"
    
    return resultado + formatear_resultados(diccionario, claves, i + 1)

# validar las calificaciones

# Filtrara una calificación entre 1 a 5. Si no hay ninguna, retorna True, si hay al menos una, False.
def rango(valores):
    return len(list(filter(lambda acumulador: acumulador < 1 or acumulador > 5, valores))) == 0

# funciones que conformara la interfaz

# Guardara los datos de una encuesta x
def guardar_encuesta():
    try:
        # Toma el nombre del alumno y la materia seleccionada.
        calificaciones = list(map(int, [entry.get() for entry in entradas_aspectos]))
        if not rango(calificaciones):
            messagebox.showerror("Error", "Las calificaciones deben estar entre 1 y 5")
            return
        
        # Toma las calificaciones de los aspectos desde las cajas de entrada
        # Valida que estén entre los rangos 1 y 5
        # guarda los datos en un diccionario y lo añadera a encuestas en caso que se encuentre bien todo.
        encuesta = {
            "nombre": entry_nombre.get(),
            "materia": materia_var.get()
        }
        for i, aspecto in enumerate(aspectos):
            encuesta[aspecto] = calificaciones[i]
        
        encuestas.append(encuesta)
        messagebox.showinfo("Guardado", f"Evaluación guardada para {encuesta['materia']}")
        
        # Limpia los campos para otra encuesta
        for entry in entradas_aspectos:
            entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos del 1 al 5.")

# Muestra los resultados generales por asignatura:
# Recorre todas las materias.
# Para cada una, obtiene las encuestas hechas.
# Calcula las estadísticas de cada aspecto.
# Muestra los resultados con messagebox.
def resultados_generales():
    if not encuestas:
        messagebox.showinfo("Sin datos", "Aún no se han registrado encuestas")
        return

    resultados = ""
    for materia in asignaturas:
        encuestas_materia = Encuesta_Materia(materia)
        if encuestas_materia:
            estadisticas = estadistica(encuestas_materia)
            resultados += f"\n=== {materia.upper()} ===\n"
            resultados += formatear_resultados(estadisticas)
    messagebox.showinfo("Resultados Generales por Asignatura", resultados)


# Muestra los resultados por materia.
def resultados_individuales():
    if not encuestas:
        messagebox.showinfo("Sin datos", "Aún no se han registrado encuestas")
        return

    nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del alumno:")
    if not nombre:
        return

    encuestas_alumno = encuesta_alumno(nombre)
    if not encuestas_alumno:
        messagebox.showinfo("Sin datos", f"No hay encuestas para {nombre}")
        return

    resultados = ""
    for materia in asignaturas:
        encuestas_materia = list(filter(lambda acumulador, materia=materia: acumulador["materia"] == materia, encuestas_alumno))
        if encuestas_materia:
            estadisticas = estadistica(encuestas_materia)
            resultados += f"\n=== {materia.upper()} ===\n"
            resultados += formatear_resultados(estadisticas)
    messagebox.showinfo(f"Resultados de {nombre}", resultados)

# se crea el interfaz

# Ventana principal
root = tk.Tk()
root.title("Evaluación de Asignaturas")

# Campo de nombre
tk.Label(root, text="Nombre del alumno:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

# Menú de selección de materia
tk.Label(root, text="Seleccione una materia:").pack()
materia_var = tk.StringVar(root)
materia_var.set(asignaturas[0])
tk.OptionMenu(root, materia_var, *asignaturas).pack()

# Entradas para los aspectos a evaluar
entradas_aspectos = []
for aspecto_local in aspectos:
    tk.Label(root, text=f"  {aspecto_local} (1-5):").pack()
    e = tk.Entry(root)
    e.pack()
    entradas_aspectos.append(e)

# Botones de acción
tk.Button(root, text="Guardar evaluación", command=guardar_encuesta).pack(pady=5)
tk.Button(root, text="Ver resultados generales de las asignaturas", command=resultados_generales).pack(pady=5)
tk.Button(root, text="Ver resultados por cada alumno", command=resultados_individuales).pack(pady=5)

# Inicia la GUI
root.mainloop()