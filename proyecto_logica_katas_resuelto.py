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

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
lista_1 = [1760 , 4326 , 7634]
lista_2 = [543 ,712 , 54]

diferencia_listas = list(map(lambda x,y: x-y, lista_1, lista_2))
print(f"La diferencia entre listas es: {diferencia_listas}")


# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_notas_media(lista, nota_aprobado=5):
    media = sum(lista)/len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (f"Como la nota media es {media}", f"el estado es {estado}")

evaluar_notas_media([2.5 , 8.4 , 4.7 , 9.1 , 3.9])

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(13))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def de_tuplas_a_strings(lista):

    resultado = list(map(lambda x: " ".join(x), lista))

    return resultado
tuplas = [("Me","llamo",":","Sofía")]
print(de_tuplas_a_strings(tuplas))

# 8.Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir():
    try:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: "))
        print(f"El resultado de la divisón es: {a/b}")
    except ValueError:
        print("Debes introducir números")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
dividir()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def mascotas_permitidas(lista):
    prohibidas = ["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"]
    return list(filter(lambda x: x not in prohibidas, lista))
print(f"Las mascotas permitidas en España son : {mascotas_permitidas(['Perro','Tigre','Tortuga' , 'Serpiente Pitón' , 'Oso' , 'Sapo' , 'Ratón'])}")

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class Lista_Vacia(Exception):
    pass

def promedio(lista):
    if not lista:
        raise Lista_Vacia("La lista está vacía")
    return sum(lista)/len(lista)

promedio([5 , 2 , 25 , 7 , 10 , 1 , 19])

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Valor fuera de rango")
        print("Edad válida")
    except ValueError as e:
        print("Error:", e)
pedir_edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    return list(map(len, frase.split()))
longitud_palabras("Me llamo Sofía")

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def letras(caracteres):
    unicas = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))
letras("Me llamo Sofía")

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def letra_inicial(lista, letra):
    return list(filter(lambda x: x.startswith(letra), lista))
print(f"Los nombres que empiezan con S son: {letra_inicial(['Sofia' , 'Sonia' , 'Romina' , 'Gustavo'],'S')}")

# 15. Crea una función lambda que  sume 3 a cada número de una lista dada.
lista = [13 , 17 , 654]
resultado = list(map(lambda x: x+3, lista))
resultado

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def recuento_palabras(texto, n):
    return list(filter(lambda x: len(x)>n, texto.split()))
recuento_palabras("Me llamo Sofía , vivo en Madrid",3)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce
def lista_numero(lista):
    return reduce(lambda x,y: x*10 + y, lista)
lista_numero([5,7,2])
#también se puede resolver con un bucle for de la siguiente forma:
def lista_numero(lista):
    resultado = 0

    for digito in lista:
        resultado = resultado * 10 + digito

    return resultado
print(lista_numero([5,7,2]))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter().
estudiantes = [
    {"nombre":"Sofia","edad":27,"calificacion":86},
    {"nombre":"Romina","edad":23,"calificacion":95},
    {"nombre":"Sonia","edad":34,"calificacion":73},
    {"nombre":"Gustavo","edad":29,"calificacion":100},
]

aprobados = list(
    map(
        lambda x: {"nombre": x["nombre"], "calificacion": x["calificacion"]},
        filter(lambda x: x["calificacion"] >= 90, estudiantes)
    )
)
print(f"Los aprobados son: {aprobados}")

# 19. Crea una función lambda que filtre los números impares de una lista dada.
lista = [13, 17, 654, 32, 1, 6, 7, 34, 23]
filtrar_impares = list(filter(lambda x: x%2!=0, lista))
filtrar_impares

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista = [13,"Sofía",3,"hola", "Romina" , 6 , 9]
filtrar_numeros = list(filter(lambda x: isinstance(x,int), lista))
filtrar_numeros

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda x: x**3
cubo(20
     
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()
from functools import reduce
lista=[2,5,7]
producto = reduce(lambda x,y: x*y, lista)
producto

# 23. Concatena una lista de palabras.Usa la función reduce()
from functools import reduce
palabras=["hola", "," , "soy","Sofía"]
texto = reduce(lambda x,y: x+" "+y, palabras)
texto

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
from functools import reduce
lista=[13,3,2 , 10]
resultado = reduce(lambda x,y: x-y, nums)
resultado

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(texto):
    return len(texto)
contar_caracteres("Hola, soy Sofía")

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda a,b: a%b
resto(346,23)

# 27. Crea una función que calcule el promedio de una lista de números.
def promedio_lista(lista):
    return sum(lista)/len(lista)
promedio_lista([643,240,16])
