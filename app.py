"""Aplicación Streamlit para analizar datos energéticos.

Este módulo contiene la lógica de carga, normalización y limpieza
para el conjunto de datos suministrado por el Bootcamp.
"""

from __future__ import annotations

from pathlib import Path
import unicodedata
from typing import Iterable

import pandas as pd
import streamlit as st

# Valores que, una vez normalizados, se consideran vacíos.
# Se trabajan en mayúsculas porque todos los textos se convierten previamente
# usando ``str.upper`` y se eliminan sus tildes para simplificar las
# comparaciones.
TEXT_EMPTY_VALUES: set[str] = {
    "",
    "NA",
    "N/A",
    "NONE",
    "NULL",
    "SIN INFORMACION",
    "SIN DATO",
    "SIN INFORMACION DISPONIBLE",
    "SIN REGISTRO",
    "S/D",
    "NO APLICA",
    "NO DEFINIDO",
    "NO REPORTA",
}

# Columnas clave con las que se detectan registros duplicados. Se escriben tal
# como aparecen en el archivo de origen para evitar errores ortográficos que
# impidan encontrar la columna.
KEY_COLUMNS: tuple[str, ...] = (
    "ID DEPARTAMENTO",
    "ID MUNICIPIO",
    "ID LOCALIDAD",
    "AÑO SERVICIO",
    "MES SERVICIO",
)


def _quitar_tildes(texto: str) -> str:
    """Elimina las tildes de un texto usando unicodedata."""
    normalized = unicodedata.normalize("NFD", texto)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")


def normalizar_texto(valor: object) -> object:
    """Normaliza un valor textual con strip, upper y sin tildes."""
    if pd.isna(valor):
        return pd.NA
    if not isinstance(valor, str):
        valor = str(valor)
    valor = _quitar_tildes(valor)
    valor = valor.strip().upper()
    return valor


def limpiar_columnas_texto(df: pd.DataFrame, columnas: Iterable[str]) -> pd.DataFrame:
    """Aplica la normalización y reemplaza textos vacíos por NA."""
    # Se crea una copia para no modificar el DataFrame original recibido.
    df = df.copy()
    for columna in columnas:
        # Normalizamos cada valor y luego sustituimos los textos considerados
        # como vacíos por ``pd.NA``.
        serie = df[columna].map(normalizar_texto)
        serie = serie.replace(TEXT_EMPTY_VALUES, pd.NA)
        df[columna] = serie.astype("string")
    return df


def eliminar_duplicados(df: pd.DataFrame, columnas_clave: Iterable[str]) -> tuple[pd.DataFrame, int]:
    """Elimina duplicados y devuelve el DataFrame limpio y el conteo eliminado."""
    # Nuevamente se trabaja con una copia para garantizar la inmutabilidad del
    # DataFrame original.
    df = df.copy()
    cantidad_inicial = len(df)
    df = df.drop_duplicates(subset=list(columnas_clave))
    eliminados = cantidad_inicial - len(df)
    return df, eliminados


@st.cache_data(show_spinner=False)
def cargar_datos(ruta_csv: Path) -> tuple[pd.DataFrame, int, tuple[str, ...]]:
    """Carga el CSV, limpia las columnas de texto y quita duplicados."""
    # ``dtype="object"`` asegura que no se pierda información al interpretar
    # códigos o identificadores que podrían verse como números con ceros a la
    # izquierda.
    df = pd.read_csv(ruta_csv, encoding="utf-8", dtype="object")
    columnas_texto = df.select_dtypes(include="object").columns
    df = limpiar_columnas_texto(df, columnas_texto)
    faltantes = tuple(col for col in KEY_COLUMNS if col not in df.columns)
    eliminados = 0
    if not faltantes:
        df, eliminados = eliminar_duplicados(df, KEY_COLUMNS)
    return df, eliminados, faltantes


def _resolver_ruta_datos() -> Path:
    raiz = Path(__file__).resolve().parent
    coincidencias = sorted(raiz.glob("Estado_de_la_prestación_del_servicio_de_energía_en_Zonas_No_Interconectadas_*.csv"))
    if not coincidencias:
        raise FileNotFoundError("No se encontró el archivo CSV esperado en el directorio del proyecto.")
    return coincidencias[0]


def main() -> None:
    st.set_page_config(page_title="Análisis servicio de energía ZNI", layout="wide")
    st.title("Estado del servicio de energía en Zonas No Interconectadas")

    try:
        ruta_csv = _resolver_ruta_datos()
    except FileNotFoundError as exc:
        st.error(str(exc))
        return

    df, eliminados, faltantes = cargar_datos(ruta_csv)

    if faltantes:
        st.sidebar.error(
            "No fue posible eliminar duplicados porque faltan las columnas clave: "
            + ", ".join(faltantes)
        )
    else:
        st.sidebar.metric("Registros eliminados por duplicados", eliminados)

    st.sidebar.write("Archivo analizado:")
    st.sidebar.code(ruta_csv.name)

    st.subheader("Vista previa de los datos limpiados")
    st.dataframe(df.head(100))

    st.caption(
        "Los textos fueron normalizados (sin tildes, en mayúsculas y sin espacios) y los valores vacíos "
        "fueron reemplazados por pd.NA antes de eliminar duplicados por las columnas clave."
    )


if __name__ == "__main__":
    main()
