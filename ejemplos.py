#1. crear una funcion
# palabra reservada def seguido del nombre
# del la funcion

from re import A


def miFuncion():
    print("Este es un mensaje")

miFuncion()

#2. funciones con parametros
def miFuncion(nombre, apellido):
    print(f"Hola {nombre} {apellido}!!")

miFuncion('Yosselyn','Hernandez')

#3. Retornar4 valores a traves de la funcion
def sumar(a,b):
    return a + b

resultado = sumar(4, 6)
print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(5,6)}")

#. Parametros (por nombre y por posición)
def areaTriangulo(base,altura):
    return (base*altura) / 2 

alturaTriangulo = 10
baseTriangulo = 20

# - por posicion
print(areaTriangulo(alturaTriangulo, baseTriangulo))

#- por nombre
print(
    areaTriangulo(
        altura = alturaTriangulo,
        base = baseTriangulo
    )   
)

# 5. Valores por defecto
def multiplicar(a,b = 1):
    return a * b

print(f"La multiplicacion es:{multiplicar(2,5)}")
print(f"La multiplicacion es:{multiplicar(2)}")

# 6. argumentos indeterminados

def multiplicarMuchos(a,*numeros):
    for numero in numeros:
        a *= numero

    return a

print(multiplicarMuchos(2))
print(multiplicarMuchos(2,3))
print(multiplicarMuchos(2,3,4))

#7. Otra forma de argumentos indeterminados
def mostrarInformacion(**persona):
    informacion = persona.items()
    for clave, valor in informacion:
        print(f"{clave}:{valor}")


mostrarInformacion(
    Nombre = 'Yosselyn Marilyn'

)

mostrarInformacion(
    Nombre = 'Yosselyn Hernandez',
    Apellido = 'Hernandez Orellana'
)

# 8. Retorno de multiples valores
def datos():
    nombre = "Isai"
    apellido = "Herrera"
    return "Yosselyn", "Hernandez", 22, "Femenino"

misDatos = datos()

print(misDatos[0])







