# 🏴󠁧󠁢󠁥󠁮󠁧󠁿 BD_LigaPremier

> Proyecto de análisis de datos de la Premier League: extracción, exploración, visualización y predicción mediante machine learning.

---

## 📋 Descripción del proyecto

**BD_LigaPremier** es un proyecto de análisis de datos enfocado en la Premier League de Inglaterra. A través de una pipeline completa de ciencia de datos, el proyecto extrae información actualizada desde la API de **API-Football**, la almacena en una base de datos **SQLite** local y la analiza mediante una serie de notebooks de Jupyter progresivos, que cubren desde la exploración inicial hasta la construcción de modelos predictivos.

El objetivo es generar insights estadísticos sobre equipos, partidos y tendencias de la liga, culminando en un reporte ejecutivo con los hallazgos más relevantes.

---

## 🗂️ Estructura del proyecto

```
BD_LigaPremier/
│
├── scripts/
│   └── extractor.py              # Extrae datos de API-Football y los persiste en SQLite
│
├── data/
│   └── premier_league.db         # Base de datos SQLite con los datos de la liga
│
├── notebooks/
│   ├── 01_Extraccion_Datos.ipynb     # Conexión a la API y carga inicial de datos
│   ├── 02_Exploracion_Datos.ipynb    # Limpieza de datos y análisis exploratorio (EDA)
│   ├── 03_Visualizaciones.ipynb      # Gráficos estadísticos con seaborn y plotly
│   ├── 04_Analisis_Equipos.ipynb     # Análisis estadístico por equipo
│   ├── 05_Analisis_Partidos.ipynb    # Análisis de partidos y tendencias de temporada
│   ├── 06_MachineLearning.ipynb      # Modelos de predicción con scikit-learn
│   └── 07_Reporte_Final.ipynb        # Conclusiones y resumen ejecutivo
│
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación del proyecto
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3.10+** | Lenguaje principal del proyecto |
| **pandas** | Manipulación y análisis de datos tabulares |
| **SQLite** | Almacenamiento local de los datos extraídos |
| **requests** | Consumo de la API-Football |
| **seaborn** | Visualizaciones estadísticas |
| **plotly** | Gráficos interactivos |
| **matplotlib** | Gráficos base y personalización visual |
| **scikit-learn** | Modelos de machine learning y predicción |
| **Jupyter Notebook** | Entorno de análisis interactivo |

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/BD_LigaPremier.git
cd BD_LigaPremier
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API key

Este proyecto consume datos de [API-Football](https://www.api-football.com/). Debes obtener una API key gratuita o de pago en su sitio web y configurarla antes de ejecutar el extractor.

Puedes definirla como variable de entorno:

```bash
# En macOS/Linux
export API_FOOTBALL_KEY="tu_api_key_aqui"

# En Windows (PowerShell)
$env:API_FOOTBALL_KEY="tu_api_key_aqui"
```

O bien editarla directamente en `scripts/extractor.py` en la variable correspondiente.

---

## 🚀 Ejecución

### Paso 1 — Extraer los datos

Antes de abrir cualquier notebook, ejecuta el script de extracción para poblar la base de datos:

```bash
python scripts/extractor.py
```

Esto generará (o actualizará) el archivo `data/premier_league.db` con los datos más recientes de la liga.

### Paso 2 — Lanzar Jupyter

```bash
jupyter notebook
```

### Paso 3 — Ejecutar los notebooks en orden

Los notebooks están diseñados para ejecutarse de forma **secuencial**. Cada uno depende de los datos o resultados generados por el anterior:

| Orden | Notebook | Descripción |
|:---:|---|---|
| 1️⃣ | `01_Extraccion_Datos.ipynb` | Conexión a la API y carga inicial en la base de datos |
| 2️⃣ | `02_Exploracion_Datos.ipynb` | Limpieza, revisión de nulos, estadísticas descriptivas y EDA |
| 3️⃣ | `03_Visualizaciones.ipynb` | Gráficos de distribución, comparativas y tendencias |
| 4️⃣ | `04_Analisis_Equipos.ipynb` | Ranking, rendimiento ofensivo/defensivo y comparativas por equipo |
| 5️⃣ | `05_Analisis_Partidos.ipynb` | Análisis de resultados, localía, racha y tendencias de temporada |
| 6️⃣ | `06_MachineLearning.ipynb` | Modelos de clasificación y predicción de resultados |
| 7️⃣ | `07_Reporte_Final.ipynb` | Síntesis de hallazgos y resumen ejecutivo |

> ⚠️ **Nota:** Se recomienda ejecutar todas las celdas de cada notebook de principio a fin (`Kernel > Restart & Run All`) antes de pasar al siguiente.

---

## 📊 Principales análisis

- Rendimiento ofensivo y defensivo de cada equipo durante la temporada.
- Estadísticas de localía vs. visitante y su impacto en los resultados.
- Tendencias de goles, rachas de victorias y estadísticas de tarjetas.
- Modelos predictivos para anticipar el resultado de un partido (victoria local, empate, victoria visitante).
- Identificación de variables con mayor peso estadístico en la predicción.

---

## 👥 Autores

| Nombre | Rol |
|---|---|
| **[Tu nombre aquí]** | Análisis de datos, modelado y visualización |

¿Quieres contribuir? Abre un *issue* o un *pull request*. ¡Las contribuciones son bienvenidas!

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

<p align="center">
  Desarrollado con ⚽ y 🐍 · Premier League Data Analysis
</p>
