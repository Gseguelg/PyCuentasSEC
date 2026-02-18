import pathlib as plb
import pandas as pd
import zipfile as zf
import tempfile
import re


def txt_from_zip(path: plb.Path, files_to_extract: list[str]) -> None:
    """ Extrae los archivos 'files_to_extract' desde el zip en 'path' al directorio relativo. """
    with zf.ZipFile(path, 'r') as zip_ref:
        for file in files_to_extract:
            zip_ref.extract(file, path.parent)


def export_dfs_to_excel(path: plb.Path | str, dfs: dict[str, pd.DataFrame]):
    path = plb.Path(path)
    if not dfs:
        print("No se encontraron DataFrame con prefijo 'df_'")
        return

    # Regex para caracteres de control inválidos en openpyxl (excluye \t,\n,\r)
    _ctrl_re = re.compile(r'[\x00-\x08\x0B\x0C\x0E-\x1F]')

    def _sanitize_sheet(name: str) -> str:
        for ch in r'[]:*?/\\':
            name = name.replace(ch, "_")
        return name[:31]  # límite de 31 chars para nombres de hoja

    def _clean_df(df: pd.DataFrame) -> pd.DataFrame:
        df2 = df.copy()
        for col in df2.select_dtypes(include=["object"]):
            df2[col] = df2[col].apply(lambda v: _ctrl_re.sub("", v) if isinstance(v, str) else v)
        return df2

    used = set()
    sheets = {}
    for name, df in dfs.items():
        sheet = _sanitize_sheet(name)
        if sheet in used:
            i = 1
            while f"{sheet}_{i}" in used:
                i += 1
            sheet = f"{sheet}_{i}"
        used.add(sheet)
        sheets[sheet] = _clean_df(df)

    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Se exportaron {len(sheets)} hojas en: {path}")


def crear_zip_star(z_infra, z_incidencia, z_infra_incidencia):
    """ descripción general. """
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"temp_dir: {temp_dir}")
        # extrae ambos zip en carpeta temporal
        for z_file in (z_infra, z_incidencia):
            with zf.ZipFile(z_file, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        # comprime archivos temporales en un nuevo zip
        with zf.ZipFile(z_infra_incidencia, 'w') as zip_out:
            for file2zip in plb.Path(temp_dir).rglob('*'):
                # print(f"Agregando {file2zip} a {z_infra_incidencia}...")
                zip_out.write(file2zip, arcname=file2zip.name)