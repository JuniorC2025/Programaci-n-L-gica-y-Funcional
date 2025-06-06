% Módulo de sensores (datos dinámicos)
:- dynamic humedad_suelo/1.
:- dynamic temperatura/1.
:- dynamic hora/1.
:- dynamic pronostico_lluvia/1.

% Valores iniciales de los sensores
humedad_suelo(baja).
temperatura(35).
hora(20).
pronostico_lluvia(false).

% Tipos de humedad posibles
humedad_posible(baja).
humedad_posible(media).
humedad_posible(alta).

% Rangos válidos para sensores
rango_temperatura_valida(T) :- number(T), T >= -10, T =< 50.
rango_hora_valida(H) :- integer(H), H >= 0, H =< 23.

% Validación de datos de sensores
sensor_valido :-
    humedad_suelo(H), humedad_posible(H),
    temperatura(T), rango_temperatura_valida(T),
    hora(Hora), rango_hora_valida(Hora),
    pronostico_lluvia(P), (P == true ; P == false).

% Reglas mejoradas para hora adecuada
hora_adecuada :- hora(H), (H < 10 ; H > 18).  % Ahora solo riego nocturno para mejor eficiencia
    hora_adecuada :- hora(H), (H < 10 ; H > 18).

% Regla principal mejorada con validación
activar_riego :- 
    sensor_valido,
    humedad_suelo(baja), 
    pronostico_lluvia(false), 
    hora_adecuada,
    \+ condiciones_peligrosas.

% Condiciones que impiden el riego
condiciones_peligrosas :-
    temperatura(T), T >= 40.  % Temperatura extremadamente alta

% Estados del sistema mejorados
estado_riego('Activado - Riego en curso') :- activar_riego.
estado_riego('No activado - Humedad adecuada') :- 
    humedad_suelo(media), writeln('Info: Humedad del suelo en nivel óptimo').
estado_riego('No activado - Humedad alta') :- 
    humedad_suelo(alta), writeln('Advertencia: Suelo ya saturado de agua').
estado_riego('No activado - Hora inadecuada') :- 
    \+ hora_adecuada, writeln('Info: Esperando horario nocturno para riego').
estado_riego('No activado - Lluvia pronosticada') :-
    pronostico_lluvia(true), writeln('Info: Se espera lluvia pronto').
estado_riego('No activado - Condiciones peligrosas') :-
    condiciones_peligrosas, writeln('ALERTA: Condiciones extremas detectadas').

% Sistema de alertas mejorado
alerta_calor :- 
    temperatura(T), 
    T >= 32,
    writeln('Alerta: Temperatura elevada detectada').

alerta_helada :-
    temperatura(T),
    T =< 2,
    writeln('Alerta: Riesgo de heladas detectado').

% Recomendaciones avanzadas
recomendacion :-
    activar_riego,
    alerta_calor, !,
    writeln('Recomendación: Riego activado con temperatura alta.'),
    writeln('* Usar riego por goteo para eficiencia hídrica'),
    writeln('* Verificar aspersores para evitar evaporación').

recomendacion :-
    activar_riego,
    writeln('Recomendación: Riego activado bajo condiciones óptimas').

recomendacion :-
    condiciones_peligrosas,
    writeln('Recomendación: Suspender riego por condiciones extremas').

recomendacion :-
    humedad_suelo(alta),
    writeln('Recomendación: Reducir frecuencia de riego - suelo saturado').

recomendacion :-
    writeln('Recomendación: Monitoreo continuo - sin acciones requeridas').

% Interface de usuario
mostrar_estado :-
    writeln('\n=== ESTADO DEL SISTEMA DE RIEGO ==='),
    estado_riego(Estado),
    writeln('Estado: '), writeln(Estado),
    (alerta_calor ; alerta_helada ; true),
    recomendacion,
    writeln('==================================\n').

% Predicados para actualizar sensores
actualizar_humedad(Valor) :-
    retract(humedad_suelo(_)),
    asserta(humedad_suelo(Valor)),
    writeln('Humedad actualizada').

actualizar_temperatura(Valor) :-
    number(Valor),
    retract(temperatura(_)),
    asserta(temperatura(Valor)),
    writeln('Temperatura actualizada').

actualizar_hora(Valor) :-
    integer(Valor),
    Valor >= 0, Valor =< 23,
    retract(hora(_)),
    asserta(hora(Valor)),
    writeln('Hora actualizada').

actualizar_pronostico(Valor) :-
    (Valor == true ; Valor == false),
    retract(pronostico_lluvia(_)),
    asserta(pronostico_lluvia(Valor)),
    writeln('Pronóstico actualizado').