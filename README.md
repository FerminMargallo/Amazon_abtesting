# Proyecto de A/B Testing en Amazon

Proyecto de análisis de datos para evaluar el impacto de dos variantes (grupo **A** y grupo **B**) en métricas de conversión y comportamiento de usuarios dentro de un contexto de e-commerce.

## Objetivo

Construir un flujo reproducible de análisis que permita:

- limpiar y estandarizar datos de navegación y compra,
- realizar un análisis exploratorio inicial,
- comprobar supuestos estadísticos,
- contrastar hipótesis entre grupos de experimento.

## Dataset

El repositorio incluye tres versiones del dataset en la carpeta `Data/`:

- `data_raw.csv`: datos originales sin procesar.
- `data_limpios.csv`: datos con limpieza y estandarización básica.
- `data_limpios_nonulos.csv`: datos preparados para análisis estadístico (sin nulos en variables clave y con imputaciones puntuales).

Variables relevantes observadas en el dataset:

- Grupo experimental (`group`),
- Conversión (`conversion`),
- Categoría y producto,
- Valor de compra (`total_value`),
- Datos de sesión (`device`, `session_duration`, `browser`, `referral_source`),
- Variables demográficas (`region`, `customer_age`, `customer_gender`).

## Estructura del proyecto

```text
Amazon_abtesting/
├── Data/
│   ├── data_raw.csv
│   ├── data_limpios.csv
│   └── data_limpios_nonulos.csv
├── notebooks/
│   ├── eda_preliminar.ipynb
│   ├── limpieza.ipynb
│   ├── nulos.ipynb
│   └── ab_testing.ipynb
├── src/
│   ├── sp_limpieza.py
│   ├── sp_eda.py
│   └── sp_abtest.py
└── README.md
```

## Flujo de trabajo sugerido

1. **Inspección inicial** del dataset (`data_raw.csv`).
2. **Limpieza y normalización** de formato y tipos de datos (`sp_limpieza.py` + notebook `limpieza.ipynb`).
3. **Análisis exploratorio** para entender distribución, nulos y duplicados (`sp_eda.py` + `eda_preliminar.ipynb`).
4. **Preparación final** para contraste de hipótesis (`nulos.ipynb`).
5. **A/B testing** con tests no paramétricos y validaciones de supuestos (`sp_abtest.py` + `ab_testing.ipynb`).

## Funciones principales

### `src/sp_limpieza.py`

- `minus(df)`: convierte a minúsculas las columnas de texto.
- `comas(df)`: sustituye comas por puntos e intenta convertir a numérico.
- `espacios(df)`: reemplaza espacios por guiones bajos en variables categóricas.

### `src/sp_eda.py`

- `eda_preliminar(df)`: muestra muestra aleatoria, dimensiones, nulos, duplicados y estadísticas descriptivas.

### `src/sp_abtest.py`

- `exploracion_df_abtesting(df, col_control)`: resumen descriptivo por grupo.
- `normalidad(df, lista_metricas)`: test de Shapiro-Wilk para normalidad.
- `homocedasticidad(df, col_control, lista_metricas)`: test de Levene para igualdad de varianzas.
- `mannwhitneyu(df, col_control, lista_metricas)`: contraste no paramétrico entre grupos.

## Cómo ejecutar el proyecto

### 1) Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install pandas scipy jupyter
```

### 3) Abrir notebooks

```bash
jupyter notebook
```

Luego puedes ejecutar los notebooks en este orden:

1. `notebooks/limpieza.ipynb`
2. `notebooks/eda_preliminar.ipynb`
3. `notebooks/nulos.ipynb`
4. `notebooks/ab_testing.ipynb`

## Ejemplo rápido de uso (módulos `src/`)

```python
import pandas as pd
from src.sp_eda import eda_preliminar
from src.sp_abtest import normalidad, homocedasticidad, mannwhitneyu

# Carga de datos
_df = pd.read_csv("Data/data_limpios_nonulos.csv")

# Exploración inicial
eda_preliminar(_df)

# Contrastes
metricas = ["session_duration", "total_value"]
normalidad(_df, metricas)
homocedasticidad(_df, "group", metricas)
mannwhitneyu(_df, "group", metricas)
```

## Próximas mejoras recomendadas

- Añadir `requirements.txt` o `pyproject.toml` para reproducibilidad.
- Incorporar tests automáticos para funciones estadísticas.
- Estandarizar mensajes de salida y corrección de textos en resultados.
- Publicar conclusiones finales del experimento en una sección de resultados.

## Autoría

Proyecto académico/práctico de análisis de datos orientado a experimentación A/B.

