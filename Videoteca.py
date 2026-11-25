# Fase 5 - Evaluación Final POA
# Curso: Fundamentos de Programación (213022)
# Problema 4: Videoteca digital
# Objetivo: contar cuántos títulos tienen calificación >= umbral
# Y año de lanzamiento >= año límite (las dos a la vez).


# ---------------------------------------------------------------
# FUNCIÓN
# ---------------------------------------------------------------
def contar_titulos(matriz, umbral, anio_limite):
    """Recorre la matriz y cuenta los títulos que cumplen ambos criterios.

    Cada fila tiene: [título, año, calificación, género]
    Posiciones:        0       1        2           3
    """
    contador = 0  # Acumulador: empieza en 0

    # Recorre cada fila (cada título) de la matriz
    for fila in matriz:
        # fila[2] es la calificación y fila[1] es el año.
        # Se usa "and": deben cumplirse las dos condiciones a la vez.
        # Se usa ">=": si el valor es igual al límite, también cuenta.
        if fila[2] >= umbral and fila[1] >= anio_limite:
            contador = contador + 1  # Suma 1 al contador

    # Devuelve el resultado al programa principal
    return contador


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------

# Matriz con 7 títulos: [título, año, calificación (1 a 10), género]
catalogo = [
    ["Aventura Lunar", 2018, 9, "Ciencia ficción"],
    ["Sombras del Valle", 2012, 9, "Drama"],
    ["Ritmo Urbano", 2020, 7, "Musical"],
    ["El Último Faro", 2016, 8, "Misterio"],
    ["Cocina Real", 2015, 8, "Comedia"],
    ["Ecos del Pasado", 2005, 6, "Drama"],
    ["Ruta Salvaje", 2021, 10, "Aventura"],
]

# Criterios definidos
umbral = 8          # calificación mínima
anio_limite = 2015  # año mínimo de lanzamiento

# Llamada a la función
total = contar_titulos(catalogo, umbral, anio_limite)

# Salida: número total de títulos que cumplen ambos criterios
print("Títulos que cumplen ambos criterios:", total)
