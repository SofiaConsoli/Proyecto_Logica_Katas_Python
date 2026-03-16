# PROYECTO LÓGICA: Katas de Python
# 1 - Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    resultado = {}
    for letra in texto.replace(" ", "").lower():
        resultado[letra] = resultado.get(letra, 0) + 1
    return resultado

frecuencia_letras("Hola, me llamo Sofía")

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista_numeros = [10,15,20,25]
doble_numeros = list(map(lambda x: x*2, lista_numeros))
doble_numeros

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

buscar_palabras(["sofia","sola","filosofia","psicologia"],"sof")

# 4. 