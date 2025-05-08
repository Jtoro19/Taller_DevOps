from estudiantes.registro import (
    cargar_estudiantes,
    mostrar_estudiantes,
    calcular_promedio,
)


def main():
    ruta_csv = "estudiantes.csv"
    estudiantes = cargar_estudiantes(ruta_csv)
    mostrar_estudiantes(estudiantes)
    calcular_promedio(estudiantes)


if __name__ == "__main__":
    main()