import os
import shutil
from tkinter import Tk, filedialog

model_source = os.path.dirname(__file__)
ruta_data = os.path.join(model_source, "..", "..", "data")
ruta_data = os.path.abspath(ruta_data)


def seleccionar_archivo():
    root = Tk()
    root.withdraw()

    archivo_path = filedialog.askopenfilename(
        title="Selecciona un archivo sigiendo el formato solicitado",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    root.destroy()

    if archivo_path:
        destino_path = os.path.join(ruta_data, "test.txt")
        shutil.copy2(archivo_path, destino_path)
