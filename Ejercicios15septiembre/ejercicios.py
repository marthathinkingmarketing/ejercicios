# Calcular el perímetro de un cuadrado.
lado = 25
perimetro = lado * 4
print("El perimetro es",perimetro)

# Encontrar el mínimo y máximo de una lista de números.
numeros = [28, 24, 31, 47, 43, 25, 28, 33, 16, 26, 22, 21]
minimo = min(numeros)
maximo = max(numeros)
print("El número mínimo de la lista es:",minimo)
print("El número máximo de la lista es", maximo)

# Verificar si una cadena de texto contiene solo dígitos.
cadena = "Este curso de 30 horas está explotando mi mente, llevo días con migraña"
if cadena.isdigit():
    print("La cadena contiene solo digitos")
else:
    print("La cadena no contiene digitos")

# Calcular el factorial de un número utilizando una función recursiva.
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)
    
numero = 5
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    resultado = factorial(numero)
    print("El factorial de", numero, "es", resultado)

#Invertir una lista.

mi_lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
mi_lista.reverse()
print("Lista invertida es:", mi_lista )

# Calcular el producto de dos matrices.

matriz_x= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

def multiplicar_matrices(matriz_x, matriz_y):
    filas_x = len(matriz_x)
    columnas_x = len(matriz_x[0])
    filas_y = len(matriz_y)
    columnas_y = len(matriz_y[0])
    if columnas_x != filas_y:
        return "Las matrices no son multiplicables"
    resultado = [[0 for _ in range(columnas_y)] for _ in range(filas_x)]
    for i in range(filas_x):
        for j in range(columnas_y):
            for k in range(columnas_x):
                resultado[i][j] += matriz_x[i][k] * matriz_y[k][j]

    return resultado

producto = multiplicar_matrices(matriz_x, matriz_y)

for fila in producto:
    print(fila)





