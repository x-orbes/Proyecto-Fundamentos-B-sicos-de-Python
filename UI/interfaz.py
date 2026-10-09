from tabulate import tabulate
import math


def solicitar_datos_usuario():

    print ("\n" + "=" * 50)
    print ("\n--- CONSULTA DE PROPIEDADES EDÁFICAS DE SUELOS ---")
    print ("\n" + "=" * 50)

    departamento = input("1. Ingrese el Departamento: ").strip()
    municipio = input("2. Ingrese el Municipio: ").strip()
    cultivo = input("3. Ingrese el Cultivo: ").strip()

    while True:
        try:
            numero_de_registros = int(input("4. Ingrese el número de registros a consultar: ").strip())
            if numero_de_registros > 0:
                break
            else:
                print("(!) Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

    return departamento, municipio, cultivo, numero_de_registros

def mostrar_resultados (resultados):
    if not resultados:
        print ("\nNo se encontraron datos para la consulta realizada.")
        return

    print ("\n" + "=" * 50)
    print ("\n      --- RESULTADOS DEL ANÁLISIS DE SUELO ---")
    print ("\n" + "=" * 50)

    def formatear_numero(valor):
        if valor is None or math.isnan(valor):
            return "N/A"
        return f"{valor:.2f}"

    tabla_final = [
        ["Departamento", resultados["Departamento"]],
        ["Municipio", resultados["Municipio"]],
        ["Cultivo", resultados["Cultivo"]],
        ["Topografía", resultados["Topografia"]],
        ["Mediana pH", formatear_numero(resultados["Mediana_pH"])],
        ["Mediana Fósforo (P) mg/kg", formatear_numero(resultados["Mediana_Fosforo"])],
        ["Mediana Potasio (K)  cmol(+)/kg", formatear_numero(resultados["Mediana_Potasio"])]
    ]

    print(tabulate(tabla_final, headers=["Propiedad", "Resultado"], tablefmt="fancy_grid"))
    print("\n" + "=" * 50)