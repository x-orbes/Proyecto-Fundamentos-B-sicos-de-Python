from API.procesador import obtener_datos, datos_no_encontrados
from UI.interfaz import solicitar_datos_usuario, mostrar_resultados

def main():
    depto, mun, cultivo, limite = solicitar_datos_usuario()

    print("\nConsultando datos en el archivo Excel, espere un momento...")
    try:
        resultados = obtener_datos(depto, mun, cultivo, limite)
        mostrar_resultados(resultados)

    except FileNotFoundError:
        print("\n[!] Error crítico: No se encontró el archivo 'resultado_laboratorio_suelo.xlsx'.")
    except datos_no_encontrados as e:
        print(f"\n[!] Aviso: {e}")
    except Exception as e:
        print(f"\n[!] Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()