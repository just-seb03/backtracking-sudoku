#---------------------------------------------------------------#
#               Universidad Central -Sede Coquimbo-             #
#                                                               #
#       Nombre del proyecto: Backtracking con heurística MRV    #
#               Nombre del archivo: generator.py                #
#               Programador: Sebastian Arredondo                #
#                   Fecha de inicio: 07-09-2025                 #
#---------------------------------------------------------------#
# Funciones:                                                    #
#   -  crear_matriz_vacia                                       #
#   -  es_valido                                                #
#   -  llenar_sudoku                                            #
#   -  eliminar_numeros                                         #
#   -  generar_sudoku                                           #
#---------------------------------------------------------------#
# Notas:                                                        #
#   - Aqui se genera la matriz sudoku, debo comentar que tuve   #
#     problemas importantes con la validacion, sobretodo porque #
#     cuando comence a programar no tenia idea de una de las    #
#     reglas la cual era que en cada fila, columna y cuadrante  #
#     debian tener numeros 1 al 9 si o si.                      #
#---------------------------------------------------------------#

# Librerias a importar
import random

# Aqui solo estoy creando una matriz sin nada
def crear_matriz_vacia():
    return [[0 for _ in range(9)] for _ in range(9)]


# Aqui estoy verificando si el numero es valido dependiendo de la condicion
def es_valido(matriz, fila, columna, num):
    # Verifica si el número está en la fila
    if num in matriz[fila]:
        return False

    # Verifica si el número está en la columna
    for i in range(9):
        if matriz[i][columna] == num:
            return False

    # Verifica si el número está en el cuadrado 3x3 actual del numero
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if matriz[inicio_fila + i][inicio_columna + j] == num:
                return False

    return True


# Función para rellenar el Sudoku de manera recursiva
def llenar_sudoku(matriz):
    for fila in range(9):
        for columna in range(9):
            if matriz[fila][columna] == 0:
                # aqui randomizo los numeros
                numeros_posibles = list(range(1, 10))
                random.shuffle(numeros_posibles)

                # aqui estoy verificando los numeros con la funcion es_valido
                for num in numeros_posibles:
                    if es_valido(matriz, fila, columna, num):
                        matriz[fila][columna] = num
                        if llenar_sudoku(matriz):
                            return True
                        matriz[fila][columna] = 0  # si no fuera valido solo pone un cero y tal
                return False
    return True


# aqui borro numeros random simplemente
def eliminar_numeros(matriz, cantidad=50):
    while cantidad > 0:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if matriz[fila][columna] != 0:
            matriz[fila][columna] = 0
            cantidad -= 1


# esta es una funcion globla que llama a todas las funciones anteriores para crear la matriz que luego retornara para el main
def generar_sudoku(matriz):
    llenar_sudoku(matriz)
    eliminar_numeros(matriz, 56)
    return matriz

