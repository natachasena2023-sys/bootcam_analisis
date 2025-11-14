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

---
Este resumen compila los conceptos fundamentales para iniciar el trabajo en Colab y comprender los elementos esenciales de Python dentro del Bootcamp.
