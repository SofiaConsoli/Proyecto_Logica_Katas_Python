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
cubo(20)
     
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

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos=set()
    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)
primer_duplicado([23 , 45 , 22 , 46 , 22 , 47])

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar(valor):
    s=str(valor)
    return "#"*(len(s)-4)+s[-4:]
enmascarar("ES615234095624527990987")

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def anagramas(a,b):
    return sorted(a)==sorted(b)
anagramas("sofia","aifos")

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    
    nombres = input("Para crear la lista, introduce nombres separados por coma: ")
    lista_nombres = [n.strip() for n in nombres.split(",")]

    nombre_buscar = input("Nombre a buscar: ").strip()

    if nombre_buscar in lista_nombres:
        print(f"{nombre_buscar} está en la lista")
    else:
        raise ValueError(f"{nombre_buscar} no está en la lista")

try:
    buscar_nombre()
except ValueError as e:
    print("Error:", e)

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la personan no trabaja aquí.
lista_empleados = [
    {"nombre": "Sofia Consoli", "puesto": "Coordinadora"},
    {"nombre": "Romina Consoli", "puesto": "Operadora"},
    {"nombre": "Gustavo Consoli", "puesto": "Project Manager"},
    {"nombre": "Sonia Srebernic", "puesto": "Directora"},
    {"nombre": "Angel Martin", "puesto": "Coordinador"}
]
def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "La persona no trabaja aquí"

buscar_empleado("Sofia Consoli", lista_empleados)

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_1 = [15 , 13 , 18]
lista_2 = [32 , 12 , 9]

suma_listas = list(map(lambda x,y: x+y, lista_1, lista_2))
suma_listas

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
""" 
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol 
"""

class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama+1 for rama in self.ramas]

    def quitar_rama(self,pos):
        if pos < len(self.ramas):
            self.ramas.pop(pos)

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes": self.ramas
        }

arbol=Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
arbol.info_arbol()

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
"""
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
"""

class UsuarioBanco:

    def __init__(self,nombre,saldo,cuenta_corriente):
        self.nombre=nombre
        self.saldo=saldo
        self.cuenta_corriente=cuenta_corriente

    def retirar_dinero(self,cantidad):
        if cantidad>self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo-=cantidad

    def transferir_dinero(self, otro, cantidad):
        try:
            self.retirar_dinero(cantidad)
            otro.agregar_dinero(cantidad)
        except ValueError:
            print("Saldo insuficiente") 

    def agregar_dinero(self,cantidad):
        self.saldo+=cantidad


alicia=UsuarioBanco("alicia",100,True)
bob=UsuarioBanco("bob",50,True)

bob.agregar_dinero(20)
bob.transferir_dinero(alicia,80)
alicia.retirar_dinero(50)

print(f"El saldo de Alicia es: {alicia.saldo} y el saldo de Bob es: {bob.saldo}")

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
"""
 Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
"""

def contar_palabras(texto):
    palabras=texto.split()
    freq={}
    for p in palabras:
        freq[p]=freq.get(p,0)+1
    return freq

def reemplazar_palabras(texto,original,nueva):
    return texto.replace(original,nueva)

def eliminar_palabra(texto,palabra):
    return " ".join([p for p in texto.split() if p!=palabra])

def procesar_texto(texto,opcion,*args):

    if opcion=="contar":
        return contar_palabras(texto)

    elif opcion=="reemplazar":
        return reemplazar_palabras(texto,args[0],args[1])

    elif opcion=="eliminar":
        return eliminar_palabra(texto,args[0])
    
texto = "Hola, me llamo Sofía y vivo en Madrid , mi hermana es Romina y vive en Madrid"
    
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar","Sofía","Romina"))
print(procesar_texto(texto, "eliminar","Hola,"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_dia(hora):
    if 6<=hora<12:
        return "día"
    elif 12<=hora<18:
        return "tarde"
    else:
        return "noche"
momento_dia(int(input("Introduce la hora (0-23): ")))

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
"""
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""
def calificacion(nota):
    if nota<70:
        return "insuficiente"
    elif nota<80:
        return "bien"
    elif nota<90:
        return "muy bien"
    else:
        return "excelente"

calificacion(int(input("Introduce la calificación del alumno (0-100): ")))

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def area(figura,datos):

    if figura=="rectangulo":
        base,altura=datos
        return base*altura

    elif figura=="circulo":
        (radio,) = datos
        return math.pi*radio**2

    elif figura=="triangulo":
        base,altura=datos
        return base*altura/2
    else:
        return "Figura no válida"
    
print(area("rectangulo", (4,2)))
print(area("circulo", (3,)))
print(area("triangulo", (10,2)))
print(area("pentagono", (5)))


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
"""
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.
"""

def compra():
    precio=float(input("Indique el precio del producto: "))
    cupon=input("¿Tiene cupón? (si/no): ")

    if cupon=="si":
        descuento=float(input("Indique el valor en euros del cupón: "))
        if descuento>0:
            precio-=descuento
    print("Precio final:",precio)
    
compra()

