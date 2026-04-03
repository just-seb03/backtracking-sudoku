

def confirmarNum(sudoku, fila, columna, num):
    for i in range(9):
        if sudoku[fila][i] == num:
            return False

    for i in range(9):
        if sudoku[i][columna] == num:
            return False

    # Verificar subcuadrícula 3x3
    inicioFila = (fila // 3) * 3
    inicioColumna = (columna // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku[inicioFila + i][inicioColumna + j] == num:
                return False

    return True


def mostrarSudoku(sudoku, iteracion=None):
    if iteracion is not None:
        return [fila[:] for fila in sudoku]


def resolucionSudoku(x, y, sudoku, fila=0, columna=0, iteracion=0):
    global contador
    # Guardar la matriz original al inicio
    matriz_original = [fila[:] for fila in sudoku]

    # Caso base: fin del tablero
    if fila == y - 1 and columna == x:
        return True, []

    # Siguiente fila
    if columna == x:
        fila += 1
        columna = 0

    # Saltar celdas ya llenas
    if sudoku[fila][columna] != 0:
        return resolucionSudoku(x, y, sudoku, fila, columna + 1, iteracion)

    matrices_iteraciones = []

    # Probar números del 1 al 9
    for num in range(1, 10):
        if confirmarNum(sudoku, fila, columna, num):
            sudoku[fila][columna] = num
            iteracion += 1

            # Guardar la matriz en esta iteración
            matrices_iteraciones.append(mostrarSudoku(sudoku, iteracion))
            solucion, sub_iteraciones = resolucionSudoku(x, y, sudoku, fila, columna + 1, iteracion)
            if solucion:
                matrices_iteraciones.extend(sub_iteraciones)
                return True, matrices_iteraciones
            # Backtracking
            sudoku[fila][columna] = 0
            iteracion += 1
            matrices_iteraciones.append(mostrarSudoku(sudoku, iteracion))

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j] = matriz_original[i][j]
    return False, [matriz_original]