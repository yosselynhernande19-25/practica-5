def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i+1}: "))
        datos.append(dato)
    return datos

def ordenar_lista(lista):
    return sorted(lista)

def sumatoria_lista(lista):
    return sum(lista)

def calcular_media(lista):
    sumatoria = sumatoria_lista(lista)
    n = len(lista)
    media = sumatoria / n
    return media

def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
    else:
        mediana = lista_ordenada[n//2]
    return mediana

def calcular_moda(lista):
    from collections import Counter
    contador = Counter(lista)
    moda = [item for item, count in contador.items() if count == max(contador.values())]
    return moda

def calcular_desviacion_estandar(lista):
    import math
    media = calcular_media(lista)
    n = len(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    desviacion_estandar = math.sqrt(suma_cuadrados / (n - 1))
    return desviacion_estandar

# Ejemplo de uso:
datos = ingresar_datos()
print("Datos ingresados:", datos)
datos_ordenados = ordenar_lista(datos)
print("Datos ordenados:", datos_ordenados)
suma = sumatoria_lista(datos)
print("Sumatoria de los datos:", suma)
media = calcular_media(datos)
print("Media de los datos:", media)
mediana = calcular_mediana(datos)
print("Mediana de los datos:", mediana)
moda = calcular_moda(datos)
print("Moda de los datos:", moda)
desviacion_estandar = calcular_desviacion_estandar(datos)
print("Desviación estándar de los datos:", desviacion_estandar)

