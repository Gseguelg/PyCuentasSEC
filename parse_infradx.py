import pathlib as plb
import pandas as pd


def tramo(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TRAMO_MT de Infraestructura Dx. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TRAMO_ID", "CUDN", "ALIMENTADOR_ID", "TIPO_PROPIEDAD_ID", "TIPO_TENSION_ID", 
            "FECHA_INSTALACION", "LARGO", "NUMERO_FASES", "NOMBRE_FASES", "TIPO_DISPOSICION_TRAMO_ID", "TIPO_PROTECCION_ID",
            "TENSION_kV_TRAMO"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'TRAMO_ID': str, 'CUDN': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def poste(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla POSTE de Infraestructura Dx. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "POSTE_ID", "COMUNA_ID", "TIPO_TENSION_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", 
            "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR",
            "APOYO_COMUNICACIONES", "APOYO_TV_CABLE", "APOYO_ALUMBRADO", "APOYO_OTROS"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'POSTE_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def transformador(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TRANSFORMADOR de Infraestructura Dx. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TRANSFORMADOR_ID", "CUDN", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "FECHA_INSTALACION",
            "TIPO_CAMBIADOR_ID", "TIPO_DISPOSICION_ID", "SUBESTACION_DISTRIBUCION_ID", "KVA"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'TRANSFORMADOR_ID': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def tirante(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TIRANTE de Infraestructura Dc. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TIRANTE_ID", "COMUNA_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "FECHA_INSTALACION", "ES_POSTE_MOZZO"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'TIRANTE_ID': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def estructura(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla ESTRUCTURA de Infraestructura Dx. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "ESTRUCTURA_ID", "CUDN", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "TIPO_TENSION_ID", 
            "FECHA_INSTALACION", "TIPO_DISPOSICION_ID", "TIPO_INSTALACION_ID"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'ESTRUCTURA_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def equipo(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla EQUIPO de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "EQUIPO_ID", "CUDN", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "TIPO_TENSION_ID",
            "FECHA_INSTALACION", "TIPO_INSTALACION_ID", "TIPO_DISPOSICION_ID", "DENOMINACION", "NORMALMENTE_CERRADO",
            "TIPO_FUNCION_NODO_ID"
            ],
        dtype={'EMPRESA_ID': int, 'PERIODO_STAR': str, 'EQUIPO_ID': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df