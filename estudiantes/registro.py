import csv


def cargar_estudiantes(ruta_csv):
    estudiantes = []

    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila["nombre"].strip()
            try:
                nota = float(fila["nota"])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append((nombre, nota))
            except ValueError:
                continue

    return estudiantes