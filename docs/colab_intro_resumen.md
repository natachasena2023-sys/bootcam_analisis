# Introducción al Entorno de Trabajo del Bootcamp

## 1. Entorno de Programación
- **Google Colaboratory (Colab):** plataforma basada en Jupyter Notebook que permite ejecutar Python en la nube con acceso a GPU/TPU.
- **Gestión de cuentas:** confirmar la cuenta activa al abrir Colab y, si es necesario, cambiarla desde el menú superior derecho.
- **Archivos `.ipynb`:** se descargan y suben fácilmente; para entregas se recomienda enviar el archivo descargado.

## 1.1 Uso de Google Colab
- Al ingresar se muestra una lista de cuadernos recientes y la opción de crear un "Bloc de notas nuevo".
- Si hay dudas sobre la cuenta utilizada, cancelar, verificar la cuenta en la esquina superior derecha y seleccionar la correcta.

## 1.2 Cuadernos Jupyter
- Combina celdas de texto y código; se ejecutan con el botón ▶ a la izquierda de cada celda.
- Admite contenido enriquecido: código, imágenes, HTML y LaTeX.

## 1.3 Sintaxis de Texto Enriquecido (Markdown)
- Títulos: `#`, `##`, `###`.
- Viñetas: `*` o `-`.
- Listas numeradas: `1.`.
- Código en línea: `` `codigo()` ``.
- Negrita: `**texto**`; cursiva: `*texto*`.
- Citas: `>`.
- Bloques de código: ``` ```python ... ``` ```.
- Vínculos: `[texto](https://url)`.
- Imágenes: `![texto alternativo](https://url)`.
- Regla horizontal: `---`.

## 1.4 Almacenamiento en Drive
- Los cuadernos se guardan en la carpeta **Colab Notebooks** del Google Drive asociado.
- Se pueden abrir desde Drive con doble clic.

## 2. Lenguaje de Programación: Python
- Elegido por su curva de aprendizaje, ecosistema de bibliotecas de análisis de datos y machine learning, y compatibilidad multiplataforma.
- Fortalezas: analítica, ciencia de datos, ML, comunidad activa.
- Debilidad: rendimiento alto (mitigable con vectorización o extensiones).

### 2.1 Tipos de Datos en Python
- **Texto:** `str`.
- **Numéricos:** `int`, `float`, `complex`.
- **Secuencias:** `list`, `tuple`, `range`.
- **Mapeos:** `dict`.
- **Conjuntos:** `set`, `frozenset`.
- **Booleanos:** `bool`.
- **Binarios:** `bytes`, `bytearray`, `memoryview`.

#### 2.1.1 Númericos
- `int`: enteros sin límite de longitud.
- `float`: números con decimales.
- `complex`: incluyen una parte imaginaria con `j`.
- Las variables se crean asignando valores.

## 3. Concepto de Algoritmo
- Serie de pasos para resolver un problema, similar a seguir una receta.
- Importantes en programación y análisis de datos para automatizar tareas y encontrar patrones.
- Ejemplo en Python:

```python
# Sumar dos números
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("El resultado es:", resultado)
```

### 3.1 Condiciones de un Algoritmo
1. Resuelve un problema específico.
2. Es finito.
3. Interactúa con datos o variables externas.

### 3.2 Variables
- Espacios en memoria que almacenan temporalmente valores de cualquier tipo.
- Se recomienda nomenclatura **snake_case** (PEP 8) y nombres descriptivos.

#### 3.2.1 Asignación de Valores
- **Interna:** valores predefinidos en el código.
- **Externa:** valores ingresados por el usuario (usando `input()` y conversión de tipos).

#### 3.2.2 Visualización
- Se usa `print()` y se puede combinar texto con variables mediante concatenación o f-strings.

```python
nombre_tecnologia = input('Ingrese el Nombre de la Tecnología elegida ')
energia_generada = float(input('Ingrese la cantidad de Energía Generada '))
print(f'El nombre de la Tecnología elegida es: {nombre_tecnologia}')
```

### 3.3 Ejemplos Básicos
- Reasignación de variables.
- Operaciones aritméticas simples con captura de datos y uso de f-strings para mostrar resultados.

## 4. Mini Retos Resueltos

Cada mini reto aborda conceptos esenciales de Python a través de problemas contextualizados en proyectos de energía y territorio. A continuación se presenta un resumen de los objetivos, la lógica empleada y los fragmentos de código clave.

### 🏆 Mini Reto 0 · Paneles Solares en un Techo Rectangular
- **Objetivo:** estimar cuántos paneles de 2×2 m caben en un techo rectangular.
- **Conceptos:** variables numéricas, operadores aritméticos, f-strings.
- **Código base:**

```python
area_panel = 4
ancho_techo = 10
largo_techo = 20

area_techo = ancho_techo * largo_techo
numero_paneles = area_techo / area_panel

print('☀️ Cálculo de Páneles Solares')
print(f'Para un techo de {ancho_techo} x {largo_techo}, se necesitan {numero_paneles} páneles')
```

### 🏆 Mini Reto 1 · Área de un Trapezoide en un Terreno Romboide
- **Objetivo:** determinar cuántos módulos trapezoidales caben en un lote romboide.
- **Conceptos:** entrada de datos, módulo `math`, división entera (`math.floor`) y aproximación (`math.ceil`).
- **Decisión:** comparar el número exacto de módulos con su aproximación por exceso y defecto para justificar la mejor opción según el uso del suelo.
- **Código base:**

```python
import math

base_mayor = 10
base_menor = 4
altura = 4

diagonal_mayor = float(input('Ingrese el valor de la Diagonal Mayor '))
diagonal_menor = float(input('Ingrese el valor de la Diagonal Menor '))

area_modulo = (base_mayor + base_menor) * altura / 2
area_terreno = diagonal_mayor * diagonal_menor / 2

numero_modulos = area_terreno / area_modulo
modulos_exactos = math.floor(numero_modulos)
modulos_aprox = math.ceil(numero_modulos)
```

### 🧭 Mini Reto 2 · Distancia Euclidiana
- **Objetivo:** calcular la distancia entre dos puntos en el plano.
- **Conceptos:** captura de `float`, diferencia de coordenadas, `math.sqrt`, formato de impresión con dos decimales.
- **Código base:**

```python
import math

x_1 = float(input('Ingrese el valor de x₁: '))
y_1 = float(input('Ingrese el valor de y₁: '))
x_2 = float(input('Ingrese el valor de x₂: '))
y_2 = float(input('Ingrese el valor de y₂: '))

distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
print(f'La distancia en línea recta es de {distancia:.2f} metros')
```

### 🏕️ Mini Reto 3 · Áreas según la Figura Seleccionada
- **Objetivo:** calcular el área de cuadrados, rectángulos o círculos dependiendo de la opción ingresada.
- **Conceptos:** condicionales `if/elif/else`, validación simple, `math.pi`, manejo de errores.
- **Código base:**

```python
import math

opcion = input('''\
1. 🔲 Zona de carga solar
2. 🟫 Área logística
3. 🟢 Espacio comunitario
''')

try:
    opcion = int(opcion)
except ValueError:
    opcion = 0

if opcion == 1:
    lado = float(input('Lado del terreno: '))
    area = math.pow(lado, 2)
elif opcion == 2:
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = base * altura
elif opcion == 3:
    radio = float(input('Radio: '))
    area = math.pi * math.pow(radio, 2)
else:
    area = None

if area is None:
    print('Has elegido una opción inválida')
else:
    print(f'El área es: {area:.2f}')
```

### 🏞️ Mini Reto 4 · Raíces de una Ecuación Cuadrática
- **Objetivo:** encontrar las intersecciones de un canal parabólico con el terreno.
- **Conceptos:** discriminante cuadrático, validación de coeficiente `a`, `math.sqrt`, estructura condicional anidada.
- **Código base:**

```python
import math

a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

discriminante = math.pow(b, 2) - 4 * a * c

if a == 0:
    print('No es posible dividir por 0')
elif discriminante < 0:
    print('No tiene solución en los reales')
else:
    x_1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f'X1: {x_1:.2f}\nX2: {x_2:.2f}')
```

### ⚡ Mini Reto 5 · Registro Inteligente de Consumo Energético
- **Objetivo:** registrar consumos mensuales, calcular totales y detectar máximos/mínimos.
- **Conceptos:** listas, ciclos `for`, funciones nativas (`sum`, `max`, `min`, `list.index`).
- **Puntos clave:**
  - Validar que los consumos sean positivos.
  - Identificar mes de mayor y menor consumo para el reporte.
- **Código base:**

```python
meses = []
consumos = []

cantidad_meses = int(input('Meses a registrar: '))

for _ in range(cantidad_meses):
    mes = input('Nombre del mes: ')
    consumo = float(input(f'Consumo en {mes}: '))
    if consumo < 0:
        raise ValueError('El consumo debe ser positivo')
    meses.append(mes)
    consumos.append(consumo)

consumo_total = sum(consumos)
indice_max = consumos.index(max(consumos))
indice_min = consumos.index(min(consumos))

print('Registro de Consumo Energético:')
for mes, consumo in zip(meses, consumos):
    print(f'{mes.capitalize()}: {consumo} kW')

print(f'Consumo total: {consumo_total} kW')
print(f'Mes de mayor consumo: {meses[indice_max].capitalize()}')
print(f'Mes de menor consumo: {meses[indice_min].capitalize()}')
```

### 🌐 Mini Reto 6 · Infraestructura TIC en el Territorio
- **Objetivo:** listar componentes tecnológicos por etapa usando listas anidadas.
- **Conceptos:** listas de listas, ciclos anidados, formato de salida.
- **Código base:**

```python
infraestructura_tic = [
    ['Infraestructura de Red', ['Torres de telecomunicaciones', 'Fibra óptica', 'Antenas 5G', 'Routers', 'Switches']],
    ['Centros de Datos', ['Servidores', 'Sistemas de respaldo', 'Sistemas de enfriamiento']],
    ['Servicios Digitales', ['Plataformas web', 'Aplicaciones móviles', 'Soluciones en la nube']]
]

for etapa, componentes in infraestructura_tic:
    print(f'\nCOMPONENTES PARA {etapa.upper()}:')
    for componente in componentes:
        print(f'- {componente}')
```

### 🔌 Mini Reto 7 · Consumo Energético con Diccionarios
- **Objetivo:** almacenar consumos por mes en un diccionario para facilitar consultas.
- **Conceptos:** diccionarios, método `.items()`, validación de datos.
- **Código base:**

```python
consumos = {}
cantidad = int(input('¿Cuántos registros desea ingresar? '))

for _ in range(cantidad):
    mes = input('Mes: ').capitalize()
    valor = float(input('Consumo kW: '))
    if valor <= 0:
        raise ValueError('El consumo debe ser positivo')
    consumos[mes] = valor

print('\nResumen de consumo:')
for mes, valor in consumos.items():
    print(f'{mes}: {valor} kW')
```

### 🔢 Mini Reto 8 · Métricas con NumPy
- **Objetivo:** obtener estadísticas del consumo energético anual.
- **Conceptos:** arreglos de NumPy, operaciones vectorizadas (`np.sum`, `np.mean`, `np.max`, `np.min`).
- **Código base:**

```python
import numpy as np

consumos_array = np.array([310.5, 287.0, 295.2, 312.4, 278.9, 301.0,
                           319.5, 305.7, 290.2, 298.4, 311.3, 299.8])

total_consumo = np.sum(consumos_array)
consumo_promedio = np.mean(consumos_array)
consumo_maximo = np.max(consumos_array)
consumo_minimo = np.min(consumos_array)

print(f'Total: {total_consumo:.2f} kW')
print(f'Promedio mensual: {consumo_promedio:.2f} kW')
print(f'Máximo: {consumo_maximo:.2f} kW')
print(f'Mínimo: {consumo_minimo:.2f} kW')
```

### 🎲 Mini Reto 9 · Simulación Aleatoria de Consumos
- **Objetivo:** generar consumos sintéticos para analizar escenarios.
- **Conceptos:** `np.random.uniform`, comprensión de diccionarios, conteo con `np.count_nonzero`.
- **Código base:**

```python
import numpy as np

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

consumos = np.random.uniform(250, 400, size=12)
registros = dict(zip(meses, consumos))

consumo_alto = np.count_nonzero(consumos > 350)

for mes, valor in registros.items():
    print(f'{mes}: {valor:.2f} kW')
print(f'Valores por encima de 350 kW: {consumo_alto}')
```

### 🌍 Mini Reto 10 · Muestreo y Visualización de Fuentes de Energía
- **Objetivo:** simular combinaciones ciudad-energía y graficar la frecuencia por fuente.
- **Conceptos:** `np.random.choice`, `collections.Counter`, gráfico de barras con `matplotlib`.
- **Código base:**

```python
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena',
            'Manizales', 'Pereira', 'Bucaramanga', 'Cúcuta', 'Ibagué']
energias = ['Hidráulica', 'Solar', 'Eólica', 'Biomasa', 'Geotérmica', 'Carbón', 'Gas Natural', 'Diesel']

n_muestra = 100
muestra_ciudades = np.random.choice(ciudades, size=n_muestra)
muestra_energias = np.random.choice(energias, size=n_muestra)

frecuencia = Counter(muestra_energias)

plt.figure(figsize=(10, 3))
plt.bar(frecuencia.keys(), frecuencia.values(), color='cadetblue')
plt.title('Frecuencia de Uso por Tipo de Energía')
plt.xlabel('Tipo de Energía')
plt.ylabel('Número de Proyectos')
plt.xticks(rotation=15)
plt.tight_layout()
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### 📊 Reto Final · Diagnóstico de Cobertura Energética
- **Objetivo:** simular proyectos energéticos en municipios colombianos, calcular métricas clave y visualizarlas.
- **Conceptos:**
  - Selección consistente de departamento y municipio mediante `np.random.choice`.
  - Uso de `np.random.randint` para generación, consumo y población.
  - Cálculo de balance (`generación - consumo`), energía per cápita y estado del proyecto.
  - Construcción de estructuras de datos (diccionario de listas) y visualización con `matplotlib` y `pandas`.
- **Fragmentos destacados:**

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 10
lista_departamentos, lista_municipios = [], []

for _ in range(n):
    depto = np.random.choice(list(colombia.keys()))
    municipio = np.random.choice(colombia[depto])
    lista_departamentos.append(depto)
    lista_municipios.append(municipio)

generacion = np.random.randint(5000, 20000, size=n)
consumo = np.random.randint(3000, 18000, size=n)
poblacion = np.random.randint(500, 1000, size=n)

balance = generacion - consumo
energia_per_capita = generacion / poblacion
estado = ['Sostenible' if b >= 0 else 'Crítico' for b in balance]

dicc_proyectos = {
    'Departamento': lista_departamentos,
    'Municipio': lista_municipios,
    'Generacion': generacion,
    'Consumo': consumo,
    'Balance': balance,
    'Energia per Capita': energia_per_capita,
    'Estado': estado
}

df = pd.DataFrame(dicc_proyectos)
ax = df.set_index('Municipio')[['Generacion', 'Consumo']].plot(kind='bar', figsize=(12, 5))
ax.set_xlabel('Ciudades')
ax.set_ylabel('Energía (kW)')
ax.set_title('Generación y Consumo por Ciudad')
for container in ax.containers:
    ax.bar_label(container)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

Este documento reúne la síntesis de los conceptos introductorios y de los ejercicios prácticos abordados en el Bootcamp para facilitar su consulta y reutilización.

## 5. Misión 3 · Visualización y Análisis Exploratorio de Datos

La misión 3 introduce un flujo completo de análisis exploratorio de datos (EDA) utilizando pandas, seaborn, matplotlib y plotly para trabajar con información de emprendimientos.

### 5.1 Preparación del Entorno
- **Librerías clave:** `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `plotly.express`.
- **Estilos recomendados:** `plt.style.use('fivethirtyeight')` para gráficos de matplotlib y `sns.set_theme(style='whitegrid')` para seaborn.
- **Fuente de datos:** el archivo `Emprendimiento.xlsx` alojado en GitHub se carga directamente con `pd.read_excel(url)`.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = 'https://github.com/juliandariogiraldoocampo/analisis_taltech/raw/refs/heads/main/explorador/Emprendimiento.xlsx'
df = pd.read_excel(url)
```

### 5.2 Clasificación de Variables y Gráficas Básicas
- **Categórica nominal:** `Exporta (Sí/No)` se analiza con `value_counts()` y `sns.countplot` para mostrar la distribución de exportadores.
- **Categórica ordinal:** se crea `Nivel Ingresos` comparando ingresos contra la media más una desviación estándar y se grafica con `countplot`.
- **Numérica discreta:** se emplean gráficos de barras con `hue` para contrastar departamentos y niveles de ingreso.
- **Numérica continua:** se resumen ingresos con `describe()` y se inspeccionan outliers mediante `sns.boxplot`.

### 5.3 Proceso de EDA
- **Dimensiones y tipos:** `df.shape`, `df.info()` y `df.describe()` brindan panorama de filas/columnas y estadísticas básicas.
- **Conteos categóricos:** se recorre `df.select_dtypes(include='object')` para calcular frecuencias absolutas y relativas.
- **Histogramas:** `df[vbles_numericas].hist(bins=10)` permite observar la distribución de cada métrica numérica.
- **Boxplots:** se genera un subplot por variable para detectar asimetrías y valores extremos.
- **Ranking departamental:** `sns.barplot` resume la cantidad de registros por departamento ordenados.

### 5.4 Visualización Multivariable
- **Dispersión enriquecida:** `sns.scatterplot` con tamaño (`size`) y color (`hue`) expone la relación entre número de emprendimientos, ingresos y exportaciones.
- **FacetGrid:** segmenta la distribución de ingresos según exportación o nivel, facilitando comparaciones por subgrupos.
- **Visualización interactiva:** con `plotly.express` se replican histogramas y gráficos de dispersión filtrando cuantiles para reducir el impacto de valores extremos.

### 5.5 Matrices de Correlación
- **Heatmap estático:** `sns.heatmap(df.corr(numeric_only=True), annot=True)` visualiza la fuerza y sentido de correlaciones.
- **Heatmap interactivo:** `px.imshow` ofrece una alternativa navegable.
- **Métodos disponibles:**
  - `pearson` (por defecto) para relaciones lineales en datos normales.
  - `spearman` para relaciones monótonas y datos ordinales.
  - `kendall` para muestras pequeñas y robustez adicional.

### 5.6 Camino al Proyecto Final
- **Entornos virtuales:** se recomienda crear un `venv` por proyecto (`python -m venv .venv`), activarlo y seleccionar el intérprete desde VS Code. Ante restricciones de PowerShell se puede usar `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` temporalmente.
- **Gestión de dependencias:** instalar paquetes dentro del entorno (`pip install streamlit openpyxl`) y generar `requirements.txt` con `pip freeze > requirements.txt`.
- **Ejecución de aplicaciones:** correr Streamlit mediante `streamlit run app.py` (o `py -m streamlit run app.py`).

### 5.7 Dashboard en Streamlit para Zonas No Interconectadas
- **Carga y limpieza:** se leen datos CSV desde GitHub, se normalizan acentos y se convierten columnas numéricas que llegan como texto.
- **Transformaciones:**
  - Filtrado de departamentos (excluyendo San Andrés y Providencia).
  - Agrupaciones por departamento/municipio (`groupby`) y pivotes por año (`pivot_table`).
  - Cálculo de indicadores anuales y variaciones porcentuales (`delta`).
- **Interfaz Streamlit:**
  - Configuración de página con `st.set_page_config` y estilos personalizados.
  - Métricas clave usando `st.metric` en columnas y paneles expandibles (`st.expander`) para tablas detalladas.
- **Fragmento base:**

```python
col3.metric('2023', round(tot_ac_23, 2), f'{round(delta_23, 2)}%', border=True)
col4.metric('2024', round(tot_ac_24, 2), f'{round(delta_24, 2)}%', border=True)
col5.metric('2025', round(tot_ac_25, 2), f'{round(delta_25, 2)}%', border=True)
```

### 5.8 Recursos Adicionales
- Ejemplo de lectura de archivos Parquet remotos con `pd.read_parquet` para ampliar las fuentes de datos del proyecto.
- Referencias a material complementario sobre estructuras de almacenamiento y análisis exploratorio proporcionado durante la misión.
