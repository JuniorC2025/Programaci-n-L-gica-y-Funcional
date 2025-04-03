from functools import reduce

lista_peliculas = [
{
    "Titulo": "El Origen",
    "Año": "2010",
    "Clasificación": "PG-13",
    "Estreno": "16 Jul 2010",
    "Duración": "148 min",
    "Género": "Acción, Aventura, Crimen",
    "Director": "Christopher Nolan",
    "Guionista": "Christopher Nolan",
    "Actores": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy",
    "Trama": "Un ladrón que roba secretos corporativos mediante el uso de tecnología para compartir sueños recibe la tarea inversa de implantar una idea en la mente de un CEO.",
    "Idioma": "Inglés, Japonés, Francés",
    "País": "EE.UU., Reino Unido",
    "Premios": "Ganó 4 premios Oscar. Otros 143 premios y 198 nominaciones.",
    "Póster": "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
    "PuntajeMetascore": "74",
    "CalificaciónIMDB": "8.8",
    "VotosIMDB": "1,446,708",
    "IDIMDB": "tt1375666",
    "Tipo": "película",
    "Respuesta": "Verdadero"
},
{
    "Titulo": "Interestelar",
    "Año": "2014",
    "Clasificación": "PG-13",
    "Estreno": "07 Nov 2014",
    "Duración": "169 min",
    "Género": "Aventura, Drama, Ciencia Ficción",
    "Director": "Christopher Nolan",
    "Guionista": "Jonathan Nolan, Christopher Nolan",
    "Actores": "Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow",
    "Trama": "Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento por asegurar la supervivencia de la humanidad.",
    "Idioma": "Inglés",
    "País": "EE.UU., Reino Unido",
    "Premios": "Ganó 1 premio Oscar. Otros 39 premios y 132 nominaciones.",
    "Póster": "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX300.jpg",
    "PuntajeMetascore": "74",
    "CalificaciónIMDB": "8.6",
    "VotosIMDB": "910,366",
    "IDIMDB": "tt0816692",
    "Tipo": "película",
    "Respuesta": "Verdadero"
},
{
    "Titulo": "El Caballero de la Noche",
    "Año": "2008",
    "Clasificación": "PG-13",
    "Estreno": "18 Jul 2008",
    "Duración": "152 min",
    "Género": "Acción, Aventura, Crimen",
    "Director": "Christopher Nolan",
    "Guionista": "Jonathan Nolan, Christopher Nolan, David S. Goyer",
    "Actores": "Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine",
    "Trama": "Cuando la amenaza conocida como el Joker causa caos y destrucción en Gotham, el caballero enmascarado debe enfrentarse a una de las mayores pruebas psicológicas para luchar contra la injusticia.",
    "Idioma": "Inglés, Mandarín",
    "País": "EE.UU., Reino Unido",
    "Premios": "Ganó 2 premios Oscar. Otros 146 premios y 142 nominaciones.",
    "Póster": "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
    "PuntajeMetascore": "82",
    "CalificaciónIMDB": "9.0",
    "VotosIMDB": "1,652,832",
    "IDIMDB": "tt0468569",
    "Tipo": "película",
    "Respuesta": "Verdadero"
},
{
    "Titulo": "Batman inicia",
    "Año": "2005",
    "Clasificación": "PG-13",
    "Estreno": "15 Jun 2005",
    "Duración": "140 min",
    "Género": "Acción, Aventura",
    "Director": "Christopher Nolan",
    "Guionista": "Bob Kane, David S. Goyer, Christopher Nolan",
    "Actores": "Christian Bale, Michael Caine, Liam Neeson, Katie Holmes",
    "Trama": "Después de entrenar con su mentor, Batman comienza su lucha para liberar a Gotham City del crimen y la corrupción impuesta por el Espantapájaros y la Liga de las Sombras.",
    "Idioma": "Inglés, Urdu, Mandarín",
    "País": "EE.UU., Reino Unido",
    "Premios": "Nominado a 1 premio Oscar. Otros 15 premios y 66 nominaciones.",
    "Póster": "http://ia.media-imdb.com/images/M/MV5BNTM3OTc0MzM2OV5BMl5BanBnXkFtZTYwNzUwMTI3._V1_SX300.jpg",
    "PuntajeMetascore": "70",
    "CalificaciónIMDB": "8.3",
    "VotosIMDB": "972,584",
    "IDIMDB": "tt0372784",
    "Tipo": "película",
    "Respuesta": "Verdadero"
},
{
    "Titulo": "Avatar",
    "Año": "2009",
    "Clasificación": "PG-13",
    "Estreno": "18 Dic 2009",
    "Duración": "162 min",
    "Género": "Acción, Aventura, Fantasía",
    "Director": "James Cameron",
    "Guionista": "James Cameron",
    "Actores": "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
    "Trama": "Un marine parapléjico enviado a la luna Pandora en una misión especial se debate entre seguir órdenes y proteger el mundo que considera su hogar.",
    "Idioma": "Inglés, Español",
    "País": "EE.UU., Reino Unido",
    "Premios": "Ganó 3 premios Oscar. Otros 80 premios y 121 nominaciones.",
    "Póster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
    "PuntajeMetascore": "83",
    "CalificaciónIMDB": "7.9",
    "VotosIMDB": "876,575",
    "IDIMDB": "tt0499549",
    "Tipo": "película",
    "Respuesta": "Verdadero"
}
]

lista_filtrada = list(filter(lambda pelicula: pelicula["Director"]=="Christopher Nolan", lista_peliculas))

listaMap = list(map(lambda pelicula: {"titulo": pelicula["Titulo"], "calificacion": pelicula["CalificaciónIMDB"]}, lista_filtrada))

promChrisNolan = reduce(lambda acumulador, pelicula: acumulador + float(pelicula["CalificaciónIMDB"]), lista_filtrada, 0) / len(lista_filtrada)

print(lista_filtrada)
print()
print(listaMap)
print()
print("El promedio de Christopher Nolan:", promChrisNolan)