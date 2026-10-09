import pandas as pd
import unicodedata
from pathlib import Path

class datos_no_encontrados(Exception):
    pass

def normalizar_texto(texto):

    """
    Convierte el texto a mayúsculas, elimina espacios sobrantes y remueve tildes.
    Ejemplo: 'Villapinzón' -> 'VILLAPINZON'
    """
    if not isinstance(texto, str):
        texto = str(texto)
    # Descompone caracteres con acento y descarta la tilde
    texto_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', texto) 
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_tildes.strip().upper()

def obtener_datos (departamento, municipio, cultivo, numero_de_registros):

    ruta_excel = Path("data/resultado_laboratorio_suelo.xlsx")
    df = pd.read_excel(ruta_excel)
    
    cols = ['pH agua:suelo 2,5:1,0', 'Fósforo (P) Bray II mg/kg', 'Potasio (K) intercambiable cmol(+)/kg']

    for c in cols:
        df[c] = pd.to_numeric(df[c], errors = 'coerce')

    depto_busc = normalizar_texto(departamento)
    muni_busc = normalizar_texto(municipio)
    cultivo_busc = normalizar_texto(cultivo)

    filtro = df[
        (df['Departamento'].apply(normalizar_texto) == depto_busc) &
        (df['Municipio'].apply(normalizar_texto) == muni_busc) &
        (df['Cultivo'].apply(normalizar_texto) == cultivo_busc)
    ]

    if numero_de_registros > 0:
        filtro = filtro.head(numero_de_registros)

    if filtro.empty:
        raise datos_no_encontrados("No hay registro para esa consulta.")

    topografia = ", ".join(filtro['Topografia'].dropna().unique())

    return {
        "Departamento": departamento.upper(),
        "Municipio": municipio.upper(),
        "Cultivo": cultivo.upper(),
        "Topografia": topografia,
        "Mediana_pH": filtro['pH agua:suelo 2,5:1,0'].median(),
        "Mediana_Fosforo": filtro['Fósforo (P) Bray II mg/kg'].median(),
        "Mediana_Potasio": filtro['Potasio (K) intercambiable cmol(+)/kg'].median()
    }