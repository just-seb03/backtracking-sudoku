import os

model_source = os.path.dirname(__file__)
ruta_logs = os.path.join(model_source, "..","..", "results", "logs.txt")

def escribir_generator(matriz,tiempo):
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nHaz generado un Sudoku\n")
        for fila in matriz:
            linea = ' '.join(str(elemento) for elemento in fila)
            archivo.write(linea + '\n')
        archivo.write(f"Tiempo tardado: [{tiempo}]\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def escribir_resolution(matriz,tiempo):
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nEl Sudoku se a resuelto en su totalidad\n")
        for fila in matriz:
            linea = ' '.join(str(elemento) for elemento in fila)
            archivo.write(linea + '\n')
        archivo.write(f"Tiempo tardado: [{tiempo}]\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def insertar_sudoku(matriz):
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nHas insertado un Sudoku\n")
        for fila in matriz:
            linea = ' '.join(str(elemento) for elemento in fila)
            archivo.write(linea + '\n')
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def escribir_cuadrante(matriz,tiempo):
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nSe a resuelto un cuadrante del sudoku\n")
        for fila in matriz:
            linea = ' '.join(str(elemento) for elemento in fila)
            archivo.write(linea + '\n')
        archivo.write(f"Tiempo tardado: [{tiempo}]\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def escribir_cuadrante4(matriz,tiempo):
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nSe han resuelto cuatro cuadrantes del sudoku\n")
        for fila in matriz:
            linea = ' '.join(str(elemento) for elemento in fila)
            archivo.write(linea + '\n')
        archivo.write(f"Tiempo tardado: [{tiempo}]\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def error_insertar():
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nNo has respetado el formato especificado\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")
def error_sudoku():
    with open(ruta_logs, 'a') as archivo:
        archivo.write("\n-----------------------------------------------------------------------------------------------------------------------")
        archivo.write("\nEl Sudoku que has insertado no es valido\n")
        archivo.write("-------------------------------------------------------------------------------------------------------------------------")