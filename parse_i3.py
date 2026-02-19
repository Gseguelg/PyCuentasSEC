import pathlib as plb
import pandas as pd


def pc(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla I3 PUNTO_CONSUMO de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "PUNTO_CONSUMO_ID", "PUNTO_SUMINISTRO_ID", "NODO_IEC_ID", "TIPO_EMPALME_ID", 
            "SUBESTACION_PRIMARIA_ID", "COMUNA_ID", "NODO_ESQUEMATICO_ID", "NUMERO_FASES", "TIPO_RURALIDAD_ID"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'PUNTO_CONSUMO_ID': str, 'PUNTO_SUMINISTRO_ID': str, 'COMUNA_ID': str, 'NODO_ESQUEMATICO_ID': str}
    )
    return df


def ipc(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla INTERRUPCION_PUNTO_CONSUMO de Incidencias. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "INCIDENCIA_ID", "INTERRUPCION_ID", "BLOQUE_REPOSICION_ID", "PUNTO_CONSUMO_ID", "TIEMPO_INTERRUMPIDO [s]"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'INTERRUPCION_ID': str, 'INCIDENCIA_ID': str}
        )
    df['TIEMPO_INTERRUMPIDO [h]'] = df['TIEMPO_INTERRUMPIDO [s]'] / 3600
    return df


def interrupcion(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla INTERRUPCION de Incidencias. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "INTERRUPCION_ID", "CLASIFIACION_INTERRUPCION_ID", "TIPO_ORIGEN_INTERRUPCION_ID", "SISTEMA_ELECTRICO_ID", 
            "CAUSA_ID", "INCIDENCIA_ID", "EVENTORED_ID", "EMPRESA_SUMINISTRADORA_ID", "INTERRUPCION_SUMINISTRADORA_ID", "FH_INICIO_INTERRUPCION"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'INTERRUPCION_ID': str, 'INCIDENCIA_ID': str}
        )
    df['TIPIFICACION_INTERRUPCION'] = df['CLASIFIACION_INTERRUPCION_ID'].map({
        1: 'E',
        2: 'I',
        3: 'FM'
        })
    return df


def alimentador(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla ALIMENTADOR de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "ALIMENTADOR_ID", "NOMBRE_ALIMENTADOR", "TENSION_NOMINAL", "I_MAX", "FH_I_MAX", "RECONEXION_AUTOMATICA", 
            "REGULADOR_TENSION", "RELE_BAJA_FRECIENCIA", "FRECUENCIA_RELE", "ICC_TRIFASICO_CABECERA", "CLIENTES_BT1", "CLIENTES_OTROS_BT",
            "CLIENTES_AT", "CLIENTES_LIBRES", "KVA_INSTALADOS_U", "KVA_INSTALDOS_R1", "ES_SUBALIMENTADOR", "EMPRESA_SUMINISTRADORA_ID", 
            "ALIMENTADOR_SUMINISTRADOR_ID", "KVA_INSTALDOS_R2"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'INTERRUPCION_ID': str, 'INCIDENCIA_ID': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def tramo_bt(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TRAMO_BT de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TRAMO_BT_ID", "TIPO_DISPOSICION_TRAMO_ID", "COMUNA_ID", "TIPO_PROPIEDAD_ID", 
            "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR", "LARGO_RED", 
            "NUMERO_FASES", "NOMBRE_FASES"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'TRAMO_BT_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def tramo_mt(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TRAMO_MT de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TRAMO_MT_ID", "TIPO_DISPOSICION_TRAMO_ID", "COMUNA_ID", "TIPO_PROPIEDAD_ID", 
            "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR", "LARGO_RED", 
            "NUMERO_FASES", "NOMBRE_FASES"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'TRAMO_MT_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def poste(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla POSTE de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "POSTE_ID", "COMUNA_ID", "TIPO_TENSION_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", 
            "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR",
            "APOYO_COMUNICACIONES", "APOYO_TV_CABLE", "APOYO_ALUMBRADO", "APOYO_OTROS"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'POSTE_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def transformador(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TRANSFORMADOR de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TRANSFORMADOR_ID", "NODO_ESQUEMATICO_ID", "COMUNA_ID", "NODO_IEC_ID", "TIPO_RURALIDAD_ID", 
            "TIPO_PROPIEDAD_ID", "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR",
            "KVA"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'TRANSFORMADOR_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def tirante(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla TIRANTE de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "TIRANTE_ID", "COMUNA_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "EN_ZONA_CONCESION", 
            "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'TIRANTE_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def estructura_bt(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla ESTRUCTURA_BT de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "ESTRUCTURA_BT_ID", "COMUNA_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "EN_ZONA_CONCESION", 
            "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'ESTRUCTURA_BT_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df


def estructura_mt(ruta_archivo: plb.Path):
    """ Lee y agrega columnas a tabla ESTRUCTURA_MT de Infraestructura. """
    df = pd.read_csv(
        ruta_archivo,
        header=None,
        names=[
            "EMPRESA_ID", "PERIODO_STAR", "ESTRUCTURA_MT_ID", "COMUNA_ID", "NODO_IEC_ID", "TIPO_PROPIEDAD_ID", "EN_ZONA_CONCESION", 
            "CONECTADA_RED", "IDENTIFICADOR_VNR", "FECHA_INSTALACION", "CODIGO_VNR"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'ESTRUCTURA_MT_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
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
            "EMPRESA_ID", "PERIODO_STAR", "EQUIPO_ID", "TIPO_EQUIPO_ID", "COMUNA_ID", "TIPO_SERVICIO_EQUIPO_ID", "TIPO_TENSION_ID", 
            "NODO_IEC_ID", "NODO_ESQUEMATICO_ID", "TIPO_PROPIEDAD_ID", "EN_ZONA_CONCESION", "CONECTADA_RED", "IDENTIFICADOR_VNR", 
            "FECHA_INSTALACION", "CODIGO_VNR", "ES_EQUIPO_SUBESTACION", "DENOMINACION", "NORMALMENTE_CERRADO"
            ],
        dtype={'EMPRESA_ID': str, 'PERIODO_STAR': str, 'EQUIPO_ID': str, 'CODIGO_VNR': str, 'IDENTIFICADOR_VNR': str},
        decimal='.',
        sep=',',
        index_col=False
        )
    return df