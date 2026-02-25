# PyCuentasSEC

**PyCuentasSEC** es un conjunto de módulos Python orientados al procesamiento, análisis y generación de datos normativos y de infraestructura eléctrica, especialmente para reportes SEC y gestión de activos de distribución.

## Estructura del Proyecto

- cudn.py: Generador profesional de CUDN (Código Único de Disposiciones Normalizadas) para instalaciones eléctricas. Incluye funciones para empalmes, cámaras, conductores, canalizaciones, toma de tierra, transformadores y generación.
- inout.py: Utilidades para manejo de archivos, extracción de datos desde ZIP, exportación de DataFrames a Excel, y sanitización de datos.
- parse_i3.py: Lectura y procesamiento de archivos de infraestructura (I3) y de incidencias, agregando columnas relevantes para análisis.
- parse_infradx.py: Procesamiento de archivos de infraestructura de distribución (Dx), como tramos y postes, con definición de columnas y tipos de datos.
- parse_reporte.py: Funciones para cálculo de indicadores de revisión (SAIDI, bloques), procesamiento de incidencias y análisis de datos de reportes.
- __init__.py: Importa los módulos principales para facilitar el uso como paquete.
- requirements.txt: Lista de dependencias del proyecto.

## Instalación y Requisitos

- Python 3.10+
- Instalar dependencias desde requirements.txt:

```bash
pip install -r requirements.txt
```

## Uso Básico

### Generación de CUDN
```python
from cudn import GeneradorCUDN
cudn = GeneradorCUDN.empalme(fases="3", tension="B", caracteristica="A", capacidad="3")
print(cudn)  # Ejemplo: A3BA3
```

### Procesamiento de archivos
```python
from parse_i3 import pc
import pathlib as plb

df = pc(plb.Path("I3.csv"))
print(df.head())
```

### Exportar DataFrames a Excel
```python
from inout import export_dfs_to_excel
import pandas as pd

dfs = {"Hoja1": pd.DataFrame(...)}
export_dfs_to_excel("salida.xlsx", dfs)
```

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

## Autor
Gabriel Seguel G. (2026)
