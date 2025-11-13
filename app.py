# ============================================================
# 🌿 Proyecto: Dashboard de Negocios Ecológicos
# Autor: Natacha Ochoa
# Descripción:
#   Esta aplicación muestra una plantilla base en Streamlit con
#   estilo ecológico, integrando un banner, información general,
#   métricas rápidas, y una visualización de datos limpia y moderna.
#   El enfoque es promover la sostenibilidad a través de datos y diseño.
#
# Notas para el lector (Profesor/Compañeros):
#   - Este script está estructurado en secciones lógicas para facilitar la comprensión.
#   - Cada función tiene un docstring explicativo.
#   - Los estilos CSS usan una paleta ecológica (verdes suaves) para coherencia visual.
#   - La limpieza de datos asegura integridad; la visualización es accesible y moderna.
#   - Si ejecutas esto, asegúrate de que las imágenes en 'img/' existan o usa URLs públicas.
# ============================================================

import base64
import re
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# ------------------------------------------------------------
# 🌿 Función: Convertir imagen a base64 para usar en el banner
# ------------------------------------------------------------
def img_to_base64(img_path: str) -> Optional[str]:
    """Convierte una imagen local en una cadena base64.

    Si la imagen no existe, se devuelve ``None`` y se muestra
    una advertencia en la interfaz.
    """

    try:
        with open(img_path, "rb") as img_file:
            b64_data = base64.b64encode(img_file.read()).decode()
        return b64_data
    except FileNotFoundError:
        st.warning(f"Imagen no encontrada en {img_path}. Usando placeholder.")
        return None


# ------------------------------------------------------------
# 📊 Función: Cargar y limpiar dataset de negocios verdes
# ------------------------------------------------------------
@st.cache_data
def load_and_clean_data(url: str) -> pd.DataFrame:
    """Carga un dataset CSV, lo limpia y lo prepara para su análisis."""

    try:
        df = pd.read_csv(url)

        # Limpieza de nombres de columnas
        renames = {col: col.split('\n')[0].strip() for col in df.columns if '\n' in col}
        df = df.rename(columns=renames)
        df.columns = df.columns.str.upper()

        # Convertir a mayúsculas la columna PRODUCTO PRINCIPAL
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].str.upper()
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].str.replace(".", "", regex=False)
        df["PRODUCTO PRINCIPAL"] = df["PRODUCTO PRINCIPAL"].replace("MIEL", "MIEL DE ABEJAS")

        # Diccionario para corregir regiones según autoridad ambiental
        mapeo_region = {
            "AMVA": "ANDINA",
            "CAM": "ANDINA",
            "CAR": "ANDINA",
            "CARDER": "ANDINA",
            "CARDIQUE": "CARIBE",
            "CARSUCRE": "CARIBE",
            "CAS": "ANDINA",
            "CDA": "AMAZONÍA",
            "CDMB": "ANDINA",
            "CODECHOCÓ": "PACÍFICA",
            "CORALINA": "INSULAR",
            "CORANTIOQUIA": "ANDINA",
            "CORMACARENA": "ORINOQUÍA",
            "CORNARE": "ANDINA",
            "CORPAMAG": "CARIBE",
            "CORPOAMAZONÍA": "AMAZONÍA",
            "CORPOBOYACÁ": "ANDINA",
            "CORPOCALDAS": "ANDINA",
            "CORPOCESAR": "CARIBE",
            "CORPOCHIVOR": "ANDINA",
            "CORPOGUAJIRA": "CARIBE",
            "CORPOGUAVIO": "ANDINA",
            "CORPOMOJANA": "CARIBE",
            "CORPONARIÑO": "PACÍFICA",
            "CORPONOR": "CARIBE",
            "CORPORINOQUÍA": "ORINOQUÍA",
            "CORPOURABÁ": "PACÍFICA",
            "CORTOLIMA": "ANDINA",
            "CRA": "CARIBE",
            "CRC": "PACÍFICA",
            "CRQ": "ANDINA",
            "CSB": "CARIBE",
            "CVC": "PACÍFICA",
            "CVS": "CARIBE",
            "DADSA": "ANDINA",
            "DAGMA": "ANDINA",
            "EPA Barranquilla Verde": "CARIBE",
            "EPA Buenaventura": "PACÍFICA",
            "EPA Cartagena": "CARIBE",
            "SDA": "ANDINA",
        }

        # Limpiar y asignar correctamente regiones, reemplazando "No registra"
        df["AUTORIDAD AMBIENTAL"] = df["AUTORIDAD AMBIENTAL"].str.strip()
        df["REGIÓN"] = df["REGIÓN"].str.strip()

        def asignar_region(row: pd.Series) -> str:
            if pd.isna(row["REGIÓN"]) or row["REGIÓN"].lower() == "no registra":
                return mapeo_region.get(row["AUTORIDAD AMBIENTAL"], row["REGIÓN"])
            return row["REGIÓN"]

        df["REGIÓN"] = df.apply(asignar_region, axis=1)

        def limpiar_numeros(texto: str) -> str:
            if pd.isna(texto):
                return texto
            return re.sub(r"^\s*[\d\.]+\s*", "", texto)

        for col in ["CATEGORÍA", "SECTOR", "SUBSECTOR"]:
            if col in df.columns:
                df[col] = df[col].apply(limpiar_numeros)

        if "AÑO" in df.columns:
            df["AÑO"] = df["AÑO"].astype(str).str.replace(",", "", regex=False)
            df["AÑO"] = pd.to_numeric(df["AÑO"], errors="coerce").astype("Int64")

        return df
    except Exception as exc:  # noqa: BLE001
        st.error(f"Error al cargar datos: {exc}. Verifica la URL.")
        return pd.DataFrame()


# ------------------------------------------------------------
# 🌍 Configuración general de la página Streamlit
# ------------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="Basura Cero | Economía Circular",
    page_icon="♻️",
    initial_sidebar_state="expanded",
)


# ------------------------------------------------------------
# 🎨 CSS personalizado (paleta inspirada en tonos verdes suaves y modernos)
# ------------------------------------------------------------
banner_image_path = "img/verde2.png"
banner_inferior_image_path = "img/verde.png"
img_col1_image_path = "img/baner_l.png"

banner_base64 = img_to_base64(banner_image_path)
banner_inferior_base64 = img_to_base64(banner_inferior_image_path)
img_col1_base64 = img_to_base64(img_col1_image_path)

st.markdown(
    f"""
<style>
    [data-testid="stHeader"] {{
        background: linear-gradient(90deg, #88C999, #A8E55A) !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    [data-testid="stHeader"] * {{
        color: #1C3B2F !important;
    }}
    [data-testid="stAppViewContainer"], body {{
        background-color: #E6FFF7 !important;
        font-family: 'Arial', sans-serif;
    }}
    .stTitle {{
        color: #1C7C54;
        font-weight: bold;
        text-align: center;
    }}
    .stText, .stMarkdown {{
        color: #3C3C3C;
        line-height: 1.6;
    }}
    .banner {{
        position: relative;
        width: 100%;
        height: 250px;
        background-image: url("data:image/jpg;base64,{banner_base64 if banner_base64 else ''}");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2em;
        font-weight: bold;
        color: white;
        border-bottom: 3px solid #C9B79C;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        border-radius: 8px;
        overflow: hidden;
    }}
    .banner::before {{
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(45deg, rgba(0,0,0,0.3), rgba(0,0,0,0.1));
        z-index: 0;
    }}
    .banner > * {{
        position: relative;
        z-index: 1;
    }}
    .banner-inferior {{
        position: relative;
        width: 100%;
        height: 200px;
        background-image: url("data:image/jpg;base64,{banner_inferior_base64 if banner_inferior_base64 else ''}");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5em;
        font-weight: bold;
        color: white;
        border-top: 3px solid #C9B79C;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        border-radius: 8px;
        overflow: hidden;
        margin-top: 20px;
    }}
    .banner-inferior::before {{
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(45deg, rgba(0,0,0,0.3), rgba(0,0,0,0.1));
        z-index: 0;
    }}
    .banner-inferior > * {{
        position: relative;
        z-index: 1;
    }}
    .imagen-con-texto {{
        position: relative;
        width: 100%;
        height: 300px;
        background-image: url("data:image/jpg;base64,{img_col1_base64 if img_col1_base64 else ''}");
        background-size: cover;
        background-position: center;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .texto-superpuesto {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        z-index: 1;
    }}
    .imagen-con-texto::before {{
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(45deg, rgba(0,0,0,0.3), rgba(0,0,0,0.1));
        z-index: 0;
    }}
    button {{
        background: linear-gradient(45deg, #A8E55A, #88C999);
        color: #1C3B2F;
        border: none;
        padding: 12px 20px;
        font-weight: bold;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    button:hover {{
        background: linear-gradient(45deg, #9CD25B, #7BBF8A);
        color: #0F261D;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    .metric {{
        background: #F0FFF4;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #A8E55A;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }}
    @media (max-width: 768px) {{
        .banner {{
            height: 150px;
            font-size: 1.4em;
        }}
        .metric {{
            padding: 10px;
        }}
    }}
</style>
""",
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# 🛠️ Funciones de renderizado por sección
# ------------------------------------------------------------
def render_home(df: pd.DataFrame) -> None:
    """Muestra la sección principal del dashboard."""

    st.markdown(
        """
<div class="banner">
    🌿 Residuos con propósito: Colombia hacia la Economía Circular 🌿
</div>
""",
        unsafe_allow_html=True,
    )

    st.title("Integrando datos de Negocios Verdes, aprovechamiento y Ciencia, Tecnología e Innovación♻️")

    st.markdown(
        """
¡Bienvenidos! 🌱  
Este espacio presenta, de forma interactiva, cómo Colombia avanza hacia el objetivo **Basura Cero**, 
transformando los residuos en oportunidades sostenibles.  

Explora los mapas y gráficos para conocer los **proyectos activos**, las **inversiones por región** 
y las **iniciativas empresariales verdes** que promueven una gestión responsable del ambiente.
"""
    )

    st.markdown("")

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image(
                "img/mapa_basura_cero.jpg",
                caption="Fuente: Datos abiertos del Gobierno de Colombia (SSPD y MinVivienda, 2023–2024)",
                use_container_width=True,
            )
            st.markdown(
                """
       <div class="imagen-con-texto">
           <div class="texto-superpuesto">
               🌱 Principios clave del proyecto:<br>
               <strong>Impulsando el Futuro Sostenible</strong>
           </div>
       </div>
       """,
                unsafe_allow_html=True,
            )
        except FileNotFoundError:
            st.image(
                "https://via.placeholder.com/300x200?text=Imagen+Ecológica",
                caption="Placeholder ecológico",
            )

    with col2:
        st.markdown(
            """
El mapa muestra la **distribución geográfica de 12 proyectos del Programa Basura Cero**, 
con una inversión total aproximada de **$119.212 millones de pesos**.  
Estas iniciativas están orientadas a la **gestión integral de residuos**, el **aprovechamiento de materiales reciclables** y el **cierre progresivo de botaderos**.

Explora el mapa para conocer en qué departamentos se están desarrollando los proyectos, su inversión y fase de avance. 
"""
        )
        if st.button("¡Explora Más!", key="explora-mas"):
            st.success("¡Gracias por interesarte en negocios ecológicos! 🌿")

        st.markdown("------")
        st.markdown(
            """
**Principios clave del proyecto:**
- ♻️ **Sostenibilidad:** Promover prácticas amigables con el planeta.  
- 💡 **Innovación:** Fomentar tecnologías limpias.  
- 🌍 **Comunidad:** Conectar emprendedores y consumidores verdes. 
"""
        )

    st.markdown("---")

    if not df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                f'<div class="metric"><h3>📊 Total Negocios</h3><p>{len(df)}</p></div>',
                unsafe_allow_html=True,
            )
        with col2:
            top_sector = (
                df["SECTOR"].value_counts().idxmax()
                if "SECTOR" in df.columns and not df["SECTOR"].isna().all()
                else "N/A"
            )
            st.markdown(
                f'<div class="metric"><h3>🏆 Sector Líder</h3><p>{top_sector}</p></div>',
                unsafe_allow_html=True,
            )
        with col3:
            top_product = (
                df["PRODUCTO PRINCIPAL"].value_counts().idxmax()
                if "PRODUCTO PRINCIPAL" in df.columns and not df["PRODUCTO PRINCIPAL"].isna().all()
                else "N/A"
            )
            st.markdown(
                f'<div class="metric"><h3>🌟 Producto Líder</h3><p>{top_product}</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("")

    if not df.empty and "SECTOR" in df.columns and not df["SECTOR"].isna().all():
        st.markdown("### 🌿 Top 10 Sectores con más Negocios Verdes")

        custom_palette = [
            "#E6FFF7",
            "#B2F2E8",
            "#66D1BA",
            "#1FA88E",
            "#0B5C4A",
            "#A8E55A",
            "#88C999",
            "#C9B79C",
            "#7BBF8A",
            "#9CD25B",
        ]

        top_sectores = df["SECTOR"].value_counts().head(10)

        sns.set_style("whitegrid")
        plt.rcParams["font.family"] = "Arial"

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            x=top_sectores.values,
            y=top_sectores.index,
            palette=custom_palette[: len(top_sectores)],
            edgecolor="#0B5C4A",
            ax=ax,
        )

        for container in ax.containers:
            ax.bar_label(container, fmt="%d", padding=3, fontsize=9, color="#0B5C4A")

        ax.set_title(
            "Top 10 Sectores con más Negocios Verdes",
            fontsize=12,
            weight="bold",
            color="#0B5C4A",
            pad=10,
        )
        ax.set_xlabel("Número de Negocios", fontsize=10, color="#0B5C4A")
        ax.set_ylabel("Sector", fontsize=10, color="#0B5C4A")
        sns.despine(left=True, bottom=True)
        plt.tight_layout()

        st.pyplot(fig)
    else:
        st.warning(
            "La columna 'SECTOR' no está presente, está vacía o no contiene datos válidos. "
            "No se puede generar la visualización. Verifica el dataset y la limpieza aplicada."
        )

    if not df.empty:
        with st.expander("📋 Ver Base de Datos Normalizada Completa"):
            st.dataframe(df)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Descargar Base de Datos en CSV",
                data=csv,
                file_name="negocios_verdes_normalizados.csv",
                mime="text/csv",
            )
    else:
        st.warning("No se pudieron cargar los datos. Verifica la URL o la conexión a internet.")

    st.markdown(
        """
<div class="banner-inferior">
    🌿 Gracias por apoyar los Negocios Ecológicos 🌿
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(
        """
💚 *Proyecto académico realizado con Streamlit - Inspirado en la sostenibilidad y el diseño ecológico.*  
[Visita nuestro sitio web](https://example.com) para más información.
"""
    )


def render_sitemap() -> None:
    """Presenta una guía visual rápida de la aplicación."""

    st.title("Mapa del sitio")
    st.markdown(
        """
Conoce la estructura general del dashboard para navegar con facilidad.  
Cada sección está pensada para que encuentres la información clave sobre la estrategia **Basura Cero**.
"""
    )

    st.markdown("---")
    st.subheader("Secciones principales")
    st.markdown(
        """
- **Inicio:** Panorama general, métricas clave y visualizaciones de los negocios verdes.  
- **Mapa del sitio:** Esta guía rápida con accesos y descripción de cada módulo.  
- **Preguntas frecuentes:** Respuestas a dudas comunes sobre el proyecto y los datos.  
- **Descargas:** En la sección de Inicio puedes descargar la base de datos normalizada.  
"""
    )

    st.subheader("Próximas incorporaciones")
    st.markdown(
        """
- Paneles interactivos por región.  
- Seguimiento a indicadores de aprovechamiento y economía circular.  
- Integración con historias de éxito de emprendimientos verdes.  
"""
    )

    st.info(
        "Sugerencia: Usa el menú lateral para moverte entre secciones o desplegar la base de datos completa"
    )


def render_faq() -> None:
    """Muestra un listado de preguntas frecuentes con respuestas."""

    st.title("Preguntas frecuentes")
    st.markdown(
        """
Aquí encontrarás respuestas rápidas sobre el origen de la información, cómo se procesan los datos
y cómo puedes aprovechar el tablero en tus proyectos.
"""
    )

    faq_items = [
        (
            "¿De dónde provienen los datos?",
            "Los datos se descargan de fuentes oficiales como la Superintendencia de Servicios Públicos "
            "Domiciliarios y MinVivienda, además del listado nacional de Negocios Verdes disponible "
            "en datos abiertos.",
        ),
        (
            "¿Cada cuánto se actualiza la información?",
            "Puedes reemplazar el enlace del CSV por la versión más reciente publicada en GitHub u otra fuente. "
            "La función de carga está cacheada para optimizar el rendimiento.",
        ),
        (
            "¿Cómo se realizó la limpieza de los datos?",
            "Se estandarizaron nombres de columnas, se normalizaron productos y sectores, y se completaron "
            "las regiones basadas en la autoridad ambiental correspondiente.",
        ),
        (
            "¿Puedo descargar la base de datos filtrada?",
            "Sí. En la sección de Inicio encontrarás un botón para descargar el CSV con la versión normalizada "
            "del dataset.",
        ),
        (
            "¿Qué puedo hacer si falta una imagen del banner?",
            "La aplicación mostrará una advertencia y utilizará un marcador de posición, por lo que puedes "
            "subir tus propias imágenes a la carpeta `img/` para personalizarlo.",
        ),
    ]

    for question, answer in faq_items:
        with st.expander(question):
            st.write(answer)

    st.success("¿Tienes otra pregunta? ¡Añádela en el repositorio o compártela con el equipo!")


# ------------------------------------------------------------
# 🚀 Ejecución principal
# ------------------------------------------------------------
def main() -> None:
    """Punto de entrada de la aplicación Streamlit."""

    data_url = (
        "https://github.com/natachasena2023-sys/bootcam_analisis/raw/refs/heads/main/"
        "Listado_de_Negocios_Verdes_20251025.csv"
    )
    df = load_and_clean_data(data_url)

    st.sidebar.header("Navegación")
    section = st.sidebar.radio(
        "Selecciona una sección",
        ("Inicio", "Mapa del sitio", "Preguntas frecuentes"),
        index=0,
    )

    st.sidebar.markdown(
        """
---
**Tip:** Desde la sección Inicio puedes descargar la base normalizada 
y acceder a la visualización de sectores líderes.
"""
    )

    if section == "Inicio":
        render_home(df)
    elif section == "Mapa del sitio":
        render_sitemap()
    else:
        render_faq()


if __name__ == "__main__":
    main()
