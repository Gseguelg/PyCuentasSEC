import pathlib as plb
import pandas as pd
import numpy as np


def blorest(ruta_archivo: plb.Path, N_CLIENTES: int, tipo: str):
    """ Lee y agrega columnas para cálculo de revisión. """
    df = pd.read_csv(
        ruta_archivo, 
        dtype={'Incidencia': str, 'Interrupcion': str, 'Caso Op. Reposición': str},
        parse_dates=['Inicio', 'Fin'],
        encoding='UTF-8'
        )
    df['HORAS CALC'] = pd.to_datetime(df['Fin']) - pd.to_datetime(df['Inicio'])
    df = df[ ~df['SAIDI'].isna() ]
    if tipo == 'bra':
        df['SAIDI BLOQUE'] = df['HORAS CALC'].dt.total_seconds()/3600 * df['Clientes Afectados'] / N_CLIENTES
    elif tipo == 'brc':
        df['SAIDI BLOQUE'] = df['SAIDI']
    else:
        raise Exception("Debe definir tipo como 'bra' o 'brc")
    # print(df[ df['SAIDI BLOQUE'].apply(type) != np.int64 ])
    df['SAIDI BLOQUE HORAS'] = pd.to_timedelta(df['SAIDI BLOQUE'], unit='h')
    df['SAIDI %'] = df['SAIDI BLOQUE'] / df['SAIDI BLOQUE'].sum() * 100

    return df
