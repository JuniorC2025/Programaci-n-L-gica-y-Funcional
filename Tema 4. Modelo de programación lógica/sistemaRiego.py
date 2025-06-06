class SistemaRiego:
    def __init__(self):
        # Datos dinámicos de los sensores
        self.humedad_suelo = "baja"
        self.temperatura = 35
        self.hora = 20
        self.pronostico_lluvia = False
        
        # Tipos de humedad posibles
        self.humedades_posibles = ["baja", "media", "alta"]
    
    def rango_temperatura_valida(self, t):
        return isinstance(t, (int, float)) and -10 <= t <= 50
    
    def rango_hora_valida(self, h):
        return isinstance(h, int) and 0 <= h <= 23
    
    def sensor_valido(self):
        return (self.humedad_suelo in self.humedades_posibles and
                self.rango_temperatura_valida(self.temperatura) and
                self.rango_hora_valida(self.hora) and
                isinstance(self.pronostico_lluvia, bool))
    
    def hora_adecuada(self):
        return self.hora < 10 or self.hora > 18
    
    def condiciones_peligrosas(self):
        return self.temperatura >= 40
    
    def activar_riego(self):
        return (self.sensor_valido() and
                self.humedad_suelo == "baja" and
                not self.pronostico_lluvia and
                self.hora_adecuada() and
                not self.condiciones_peligrosas())
    
    def estado_riego(self):
        if self.activar_riego():
            return "Activado - Riego en curso"
        elif self.humedad_suelo == "media":
            print("Info: Humedad del suelo en nivel óptimo")
            return "No activado - Humedad adecuada"
        elif self.humedad_suelo == "alta":
            print("Advertencia: Suelo ya saturado de agua")
            return "No activado - Humedad alta"
        elif not self.hora_adecuada():
            print("Info: Esperando horario nocturno para riego")
            return "No activado - Hora inadecuada"
        elif self.pronostico_lluvia:
            print("Info: Se espera lluvia pronto")
            return "No activado - Lluvia pronosticada"
        elif self.condiciones_peligrosas():
            print("ALERTA: Condiciones extremas detectadas")
            return "No activado - Condiciones peligrosas"
        else:
            return "Estado desconocido"
    
    def alerta_calor(self):
        if self.temperatura >= 32:
            print("Alerta: Temperatura elevada detectada")
            return True
        return False
    
    def alerta_helada(self):
        if self.temperatura <= 2:
            print("Alerta: Riesgo de heladas detectado")
            return True
        return False
    
    def recomendacion(self):
        if self.activar_riego() and self.alerta_calor():
            print("Recomendación: Riego activado con temperatura alta.")
            print("* Usar riego por goteo para eficiencia hídrica")
            print("* Verificar aspersores para evitar evaporación")
        elif self.activar_riego():
            print("Recomendación: Riego activado bajo condiciones óptimas")
        elif self.condiciones_peligrosas():
            print("Recomendación: Suspender riego por condiciones extremas")
        elif self.humedad_suelo == "alta":
            print("Recomendación: Reducir frecuencia de riego - suelo saturado")
        else:
            print("Recomendación: Monitoreo continuo - sin acciones requeridas")
    
    def mostrar_estado(self):
        print("\n=== ESTADO DEL SISTEMA DE RIEGO ===")
        print("Estado:", self.estado_riego())
        self.alerta_calor() or self.alerta_helada()
        self.recomendacion()
        print("==================================\n")
    
    # Métodos para actualizar sensores
    def actualizar_humedad(self, valor):
        if valor in self.humedades_posibles:
            self.humedad_suelo = valor
            print("Humedad actualizada")
        else:
            print(f"Error: Humedad {valor} no válida. Valores posibles: {self.humedades_posibles}")
    
    def actualizar_temperatura(self, valor):
        if self.rango_temperatura_valida(valor):
            self.temperatura = valor
            print("Temperatura actualizada")
        else:
            print(f"Error: Temperatura {valor} fuera de rango válido (-10 a 50)")
    
    def actualizar_hora(self, valor):
        if self.rango_hora_valida(valor):
            self.hora = valor
            print("Hora actualizada")
        else:
            print(f"Error: Hora {valor} no válida (0-23)")
    
    def actualizar_pronostico(self, valor):
        if isinstance(valor, bool):
            self.pronostico_lluvia = valor
            print("Pronóstico actualizado")
        else:
            print("Error: El pronóstico debe ser True o False")

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaRiego()
    
    # Mostrar estado inicial
    sistema.mostrar_estado()
    
    # Actualizar algunos valores
    sistema.actualizar_humedad("media")
    sistema.actualizar_temperatura(38)
    sistema.actualizar_hora(21)
    
    # Mostrar estado después de cambios
    sistema.mostrar_estado()
    
    # Probar condiciones de riego
    sistema.actualizar_humedad("baja")
    sistema.actualizar_temperatura(25)
    sistema.actualizar_pronostico(False)
    sistema.mostrar_estado()