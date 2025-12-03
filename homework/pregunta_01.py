"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output"
    
    df = pd.read_csv(input_file, sep=";", index_col=0)
    
    columnas_texto = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "monto_del_credito",
        "línea_credito",
    ]
    
    for columna in columnas_texto:
        df[columna] = (
            df[columna]
            .str.lower()
            .str.strip()
            .str.replace("_", " ", regex=False)
            .str.replace("-", " ", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(".00", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.strip()
        )
    
    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )
    
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(
        pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )
    
    df = df.drop_duplicates()
    
    df = df.dropna()
    
    if not os.path.exists(output_file):
        os.makedirs(output_file)
    
    df.to_csv(
        f"{output_file}/solicitudes_de_credito.csv",
        sep=";",
        index=False,
    )
pregunta_01()