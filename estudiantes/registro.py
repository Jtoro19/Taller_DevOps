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

def mostrar_estudiantes(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[0].lower())

    print("\nEstudiantes:")
    print(f"{'Nombre':<15} {'Nota':<5}")
    print("-" * 22)
    for nombre, nota in estudiantes_ordenados:
        print(f"{nombre:<15} {nota:<5.2f}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes válidos para calcular el promedio.")
        return

    suma = sum(nota for _, nota in estudiantes)
    promedio = suma / len(estudiantes)
    print(f"\nPromedio general: {promedio:.2f}")