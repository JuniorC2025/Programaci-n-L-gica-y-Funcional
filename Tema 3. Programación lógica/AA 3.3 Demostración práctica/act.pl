% Categorías principales
categoria_festividad(religiosa).
categoria_festividad(etnica).
categoria_festividad(historica).
categoria_festividad(comunitaria).

% Subcategorías
subcategoria(dia_de_muertos, [ancestral, religiosa]).
subcategoria(guelaguetza, [etnica, indigena, oaxaquena]).
subcategoria(grito_independencia, [historica, patriotica, nacional]).
subcategoria(carnaval_veracruz, [comunitaria, mestiza, costena]).

% Festividades con sus categorías
festividad(dia_de_muertos, religiosa, ['1-2 noviembre']).
festividad(guelaguetza, etnica, ['Julio (dos lunes)']).
festividad(grito_independencia, historica, ['15-16 septiembre']).
festividad(carnaval_veracruz, comunitaria, ['Febrero-Marzo']).

% Regiones con datos geoculturales
region(todo_mexico, pais, 127).
region(oaxaca, estado, 8.5).  % Corregido: oaxaca en lugar de oaxaca
region(veracruz, estado, 8.1).

% Elementos culturales tipificados
elemento(altares, objeto_ritual).
elemento(pan_de_muerto, alimento_simbolico).
elemento(danza_flor_de_pina, expresion_corporal).
elemento(mariachi, musica_tradicional).

% Necesario para las reglas que usan member/2
:- use_module(library(lists)).

% Regla 1: Identificar festividad por elementos
festividad_por_elementos([Elemento1, Elemento2], Festividad) :-
    contiene_elemento(Festividad, Elemento1),
    contiene_elemento(Festividad, Elemento2).

% Regla 2: Determinar nivel de importancia regional
importancia_regional(Festividad, alta) :-
    se_celebra_en(Festividad, todo_mexico).
importancia_regional(Festividad, muy_alta) :-
    se_celebra_en(Festividad, Region),
    region(Region, _, Poblacion),
    Poblacion > 8.

% Regla 3: Recomendación de participación
recomendacion_participacion(Festividad, 'Participación activa') :-
    subcategoria(Festividad, Categorias),
    member(comunitaria, Categorias).
recomendacion_participacion(Festividad, 'Observación respetuosa') :-
    subcategoria(Festividad, Categorias),
    member(religiosa, Categorias).

% Contenido elemental de festividades
contiene_elemento(dia_de_muertos, altares).
contiene_elemento(dia_de_muertos, pan_de_muerto).
contiene_elemento(guelaguetza, danza_flor_de_pina).
contiene_elemento(grito_independencia, mariachi).

% Distribución geográfica
se_celebra_en(dia_de_muertos, todo_mexico).
se_celebra_en(guelaguetza, oaxaca).
se_celebra_en(grito_independencia, todo_mexico).
se_celebra_en(carnaval_veracruz, veracruz).

% Similitud cultural entre festividades
festividades_relacionadas(Fest1, Fest2, Razones) :-
    subcategoria(Fest1, Cats1),
    subcategoria(Fest2, Cats2),
    intersection(Cats1, Cats2, Razones),
    Razones \= [],
    Fest1 \= Fest2.

% Impacto cultural estimado
impacto_cultural(Festividad, Impacto) :-
    (se_celebra_en(Festividad, todo_mexico) -> Impacto = nacional;
    (se_celebra_en(Festividad, Region), region(Region, _, Pobl), Pobl > 8) -> Impacto = regional_significativo;
    Impacto = local).