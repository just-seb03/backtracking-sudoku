import os


def readertxt():
    sudoku_matriz = []
    model_source = os.path.dirname(__file__)
    ruta_txt = os.path.join(model_source, "..", "..", "data", "test.txt")

    with open(ruta_txt, "r") as archivo:
        for linea in archivo:
            fila = [int(num) for num in linea.split(", ")]
            sudoku_matriz.append(fila)

    return sudoku_matriz