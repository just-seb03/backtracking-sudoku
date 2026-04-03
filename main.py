#---------------------------------------------------------------#
#               Universidad Central -Sede Coquimbo-             #
#                                                               #
#       Nombre del proyecto: Backtracking con heurística MRV    #
#               Nombre del archivo: main.py                     #
#               Programador: ALL                                #
#                   Fecha de inicio: 15-10-2025                 #
#---------------------------------------------------------------#
# Funciones:                                                    #
#   - Controlador principal                                     #
#---------------------------------------------------------------#
# Notas:                                                        #
#   - Codigo principal en el cual se ejecutaran pruebas y el    #
#     objetivo principal del proyecto                           #
#---------------------------------------------------------------#

import time
import src.model.generator as generator
import src.model.writer as writer
import src.model.explorer as explorer
import src.model.reader as reader
import src.model.resolution as resolution
import src.model.verification as verification
from src.view.pygame_menu import ejecutar, manejar_tablero, animar_resolucion

matriz = generator.crear_matriz_vacia()

for accion in ejecutar():
    if accion == "generar":
        start_time = time.time()
        matriz = generator.generar_sudoku(matriz)
        end_time = time.time()
        writer.escribir_generator(matriz,end_time-start_time)
        manejar_tablero(385.1, 197.1, matriz, True)
    elif accion == "insertar":
        explorer.seleccionar_archivo()
        matriz = reader.readertxt()
        if verification.verificar(matriz):
            writer.insertar_sudoku(matriz)
            manejar_tablero(385.1, 197.1, matriz, True)
        else:
            writer.error_insertar()
    elif accion == "resolver":
        start_time = time.time()
        exito, historial_matrices = resolution.resolucionSudoku(9,9,matriz, 0, 0, 0)
        end_time = time.time()
        if exito==True:
            writer.escribir_resolution(matriz,end_time-start_time)
            animar_resolucion(historial_matrices)
        else:
            writer.error_sudoku()
    elif accion == "cuadrante":
        start_time = time.time()
        exito, historial_matrices = resolution.resolucionSudoku(3, 3, matriz, 0, 0, 0)
        end_time = time.time()
        writer.escribir_cuadrante(matriz, end_time - start_time)
        animar_resolucion(historial_matrices)
    elif accion == "4":
        start_time = time.time()
        exito, historial_matrices = resolution.resolucionSudoku(6, 6, matriz, 0, 0, 0)
        end_time = time.time()
        writer.escribir_cuadrante4(matriz, end_time - start_time)
        animar_resolucion(historial_matrices)