# 🏁 ETL Pipeline - Le Mans 24h Race Data Analysis

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.2-green.svg)](https://pandas.pydata.org/)
[![PySpark](https://img.shields.io/badge/PySpark-3.5.0-red.svg)](https://spark.apache.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12.2-orange.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un pipeline ETL completo y modular para procesar y visualizar datos históricos de las 24 Horas de Le Mans, con capacidades avanzadas de análisis y generación automática de gráficos. Incluye implementaciones tanto en Pandas como en PySpark para manejo eficiente de datasets de cualquier tamaño.

## 📋 Tabla de Contenidos

- [🎯 Características](#-características)
- [🏗️ Arquitectura](#️-arquitectura)
- [🚀 Instalación](#-instalación)
- [💻 Uso](#-uso)
- [📊 Visualizaciones](#-visualizaciones)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🔧 Configuración](#-configuración)
- [📈 Datos](#-datos)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia](#-licencia)

## 🎯 Características

### ✨ Pipeline ETL Completo
- **🔄 Extracción**: Ingesta automática de datos CSV desde Kaggle
- **⚙️ Transformación**: Limpieza, normalización y generación de campos calculados
- **💾 Carga**: Persistencia dual en SQLite y CSV para máxima compatibilidad
- **📊 Visualización**: Generación automática de análisis gráficos con Seaborn
- **⚡ Procesamiento Dual**: Implementaciones en Pandas y PySpark para diferentes escalas de datos

### 🎨 Análisis Visual Avanzado
- **Análisis de Velocidad**: Evolución temporal y categorización por rendimiento
- **Análisis de Resistencia**: Correlaciones entre vueltas y eficiencia
- **Análisis Temporal**: Progreso tecnológico a través de las décadas
- **Dashboard Resumen**: Vista consolidada con métricas clave

### 🏗️ Arquitectura Modular
- **Separación clara de responsabilidades** entre Extract, Transform, Load y Visualize
- **Configuración centralizada** para fácil mantenimiento
- **Logging detallado** con indicadores visuales (emojis)
- **Manejo robusto de errores** con fallbacks automáticos

### ⚡ Capacidades de PySpark
- **Procesamiento distribuido** para datasets masivos (> 1GB)
- **Optimización automática** de consultas y transformaciones
- **Escalabilidad horizontal** en clusters de múltiples nodos
- **Compatibilidad total** con el pipeline ETL existente
- **Rendimiento superior** para operaciones complejas de big data

## 🏗️ Arquitectura

```
ProyectoETL-sports/
├── app/
│   ├── Extract/          # 📥 Módulo de extracción
│   │   ├── SportsExtract.py
│   │   └── Files/        # 📂 Datos fuente
│   │       └── data.csv
│   ├── Transform/        # ⚙️ Módulo de transformación
│   │   └── SportsTransformer.py
│   ├── Load/            # 💾 Módulo de carga
│   │   └── SportsLoader.py
│   ├── Visualize/       # 📊 Módulo de visualización
│   │   ├── SportsVisualizer.py
│   │   └── Charts/      # 🖼️ Gráficas generadas
│   ├── Config/          # ⚙️ Configuración
│   │   └── config.py
│   └── Output/          # 📤 Resultados finales
│       ├── sports_data.db              # Base de datos SQLite (Pandas)
│       ├── sports_data_processed.csv   # CSV procesado (Pandas)
│       ├── sports_data_spark.db        # Base de datos SQLite (Spark)
│       └── sports_data_spark.csv       # CSV procesado (Spark)
├── main.py              # 🚀 Pipeline ETL principal (Pandas)
├── mainV.2.py          # 📊 Script de visualización
├── spark_main.py       # ⚡ Pipeline ETL con Apache Spark
└── requirements.txt     # 📦 Dependencias
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.13+
- Git

### 1. Clonar el repositorio
```bash
git clone https://github.com/MiguelBonilla-sys/ProyectoETL---sports.git
cd ProyectoETL---sports
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar datos
Descarga el dataset desde [Kaggle](https://www.kaggle.com/datasets/erykwitkowski/lemans-24h-race-winners) y colócalo en:
```
app/Extract/Files/data.csv
```

## 💻 Uso

### 🚀 Pipeline ETL Completo (Pandas)
```bash
python main.py
```
**Descripción**: Script principal que ejecuta el pipeline ETL completo usando Pandas para procesar datos de Le Mans.
- **Extracción**: Lee datos CSV desde `app/Extract/Files/data.csv`
- **Transformación**: Limpia, normaliza y agrega campos calculados (décadas, categorías de velocidad/resistencia)
- **Carga**: Guarda resultados en SQLite (`sports_data.db`) y CSV (`sports_data_processed.csv`)
- **Salida**: Proporciona estadísticas detalladas del proceso y tiempo de ejecución

### 📊 Solo Visualización
```bash
python mainV.2.py
```
**Descripción**: Script especializado para generar visualizaciones desde datos ya procesados.
- **Prerrequisito**: Requiere ejecutar `main.py` primero para crear la base de datos
- **Funcionalidad**: Genera 4 tipos de análisis gráficos (velocidad, resistencia, temporal, dashboard)
- **Salida**: Guarda gráficas en formato PNG en `app/Visualize/Charts/`
- **Validación**: Verifica automáticamente que la base de datos existe antes de proceder

### ⚡ Pipeline ETL con PySpark
```bash
python spark_main.py
```
**Descripción**: Versión alternativa del pipeline ETL usando PySpark para procesamiento distribuido.
- **Tecnología**: Utiliza PySpark (Python API de Apache Spark) para manejo de big data
- **Proceso**: Mismo flujo ETL pero optimizado para datasets más grandes
- **Salida**: Genera `sports_data_spark.csv` y `sports_data_spark.db`
- **Ventajas**: Mejor rendimiento para datasets masivos y procesamiento paralelo

### 🔄 Comparación de Scripts Main

| Script | Tecnología | Uso Recomendado | Salida |
|--------|------------|-----------------|---------|
| `main.py` | Pandas | Datasets pequeños-medianos (< 1GB) | `sports_data.db`, `sports_data_processed.csv` |
| `mainV.2.py` | Pandas + Seaborn | Solo visualización (requiere datos procesados) | Gráficas PNG en `Charts/` |
| `spark_main.py` | PySpark | Datasets grandes (> 1GB) o procesamiento distribuido | `sports_data_spark.db`, `sports_data_spark.csv` |

### 📋 Flujo de Trabajo Recomendado

1. **Para análisis básico**: `python main.py` → `python mainV.2.py`
2. **Para big data**: `python spark_main.py` → `python mainV.2.py`
3. **Solo visualización**: `python mainV.2.py` (si ya tienes datos procesados)

### Ejemplo de salida:
```
🏁 ETL PIPELINE - DATOS DEPORTIVOS LE MANS 🏁
============================================================

==================== PASO 1: EXTRACCIÓN DE DATOS ====================
📂 Archivo fuente: app\Extract\Files\data.csv
✅ Extracción exitosa:
   📊 Filas extraídas: 229
   📋 Columnas: 15
   📅 Rango de años: 1923 - 2023

==================== PASO 2: TRANSFORMACIÓN DE DATOS ====================
🚀 INICIANDO TRANSFORMACIÓN DE DATOS
📊 Iniciando limpieza de datos...
✅ Filas finales después de limpieza: 227
🔧 Normalizando datos...
✅ Datos normalizados correctamente
➕ Agregando campos calculados...
✅ Campos calculados agregados: Decade, Speed_Category, Endurance_Category

==================== PASO 3: CARGA DE DATOS ====================
💾 Guardando en base de datos SQLite...
✅ Datos guardados en la base de datos SQLite
💾 Guardando CSV de respaldo...
✅ Carga completada exitosamente
```

## 📊 Visualizaciones

El módulo de visualización genera 4 tipos de análisis:

### 1. 🏃‍♂️ Análisis de Velocidad (`speed_analysis.png`)
- Distribución por categorías de velocidad
- Evolución temporal de velocidades promedio
- Box plots por década
- Histograma de distribución

### 2. 🏁 Análisis de Resistencia (`endurance_trends.png`)
- Categorización por resistencia (vueltas)
- Correlación vueltas vs velocidad
- Evolución de vueltas promedio
- Análisis de eficiencia (Km/vuelta)

### 3. ⏰ Análisis Temporal (`temporal_analysis.png`)
- Participantes por década
- Diversidad de equipos
- Progreso tecnológico
- Heatmap de categorías

### 4. 📈 Dashboard Resumen (`summary_dashboard.png`)
- Estadísticas generales
- Top 10 equipos
- Timeline de participaciones
- Métricas consolidadas

## 📁 Estructura del Proyecto

### Módulos Principales

#### 🔄 Extract (`app/Extract/`)
- **`SportsExtract.py`**: Clase `Extractor` para lectura de archivos CSV
- **`Files/`**: Directorio para datos fuente

#### ⚙️ Transform (`app/Transform/`)
- **`SportsTransformer.py`**: Clase `SportsTransformer` con lógica específica:
  - Limpieza y normalización de datos
  - Generación de campos calculados (décadas, categorías, eficiencia)
  - Validación y estadísticas

#### 💾 Load (`app/Load/`)
- **`SportsLoader.py`**: Clase `Loader` con persistencia dual:
  - SQLite (principal)
  - CSV (respaldo)

#### 📊 Visualize (`app/Visualize/`)
- **`SportsVisualizer.py`**: Clase `SportsVisualizer` para análisis gráfico
- **`Charts/`**: Directorio de gráficas generadas

#### ⚙️ Config (`app/Config/`)
- **`config.py`**: Configuración centralizada de rutas y parámetros

## 🔧 Configuración

Edita `app/Config/config.py` para personalizar:

```python
class Config:
    # Rutas de entrada
    INPUT_PATH = r'app\Extract\Files\data.csv'
    
    # Rutas de salida
    OUTPUT_DIR = r'app\Output'
    SQLITE_DB_PATH = r'app\Output\sports_data.db'
    CSV_OUTPUT_PATH = r'app\Output\sports_data_processed.csv'
    
    # Visualización
    CHARTS_OUTPUT_DIR = r'app\Visualize\Charts'
    CHART_THEMES = 'whitegrid'
    
    # Categorización
    SPEED_CATEGORIES = {
        'bins': [0, 100, 150, 200, float('inf')],
        'labels': ['Slow', 'Medium', 'Fast', 'Very Fast']
    }
```

## 📈 Datos

### Fuente
**Dataset**: [Le Mans 24h Race Winners](https://www.kaggle.com/datasets/erykwitkowski/lemans-24h-race-winners)

### Schema de Datos Esperado
```
Year, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, 
Driver_nationality, Team_nationality, Average_speed_kmh, 
Average_speed_mph, Average_lap_time
```

### Campos Calculados Generados
- **`Decade`**: Agrupación temporal (1920, 1930, etc.)
- **`Speed_Category`**: Slow, Medium, Fast, Very Fast
- **`Endurance_Category`**: Short, Medium, Long, Ultra Long
- **`Km_per_Lap`**: Métrica de eficiencia

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Convenciones del Proyecto
- Usa el patrón de logging con emojis existente
- Mantén la separación modular ETL
- Documenta nuevas transformaciones
- Sigue el patrón de manejo de errores establecido

## 🛠️ Desarrollo

### Agregar Nuevas Transformaciones
```python
# En SportsTransformer.py
def new_transformation(self):
    print("🔧 Aplicando nueva transformación...")
    # Tu lógica aquí
    print("✅ Transformación completada")
    return self.df
```

### Agregar Nuevas Visualizaciones
```python
# En SportsVisualizer.py
def create_new_analysis(self):
    print("📊 Generando nuevo análisis...")
    # Tu código de visualización
    output_path = os.path.join(self.output_dir, 'new_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Nuevo análisis guardado en: {output_path}")
```

## 📊 Métricas del Proyecto

- **Líneas de código**: ~800
- **Cobertura de tests**: En desarrollo
- **Tiempo de ejecución**: ~10-15 segundos
- **Formatos de salida**: SQLite, CSV, PNG

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Miguel Bonilla** - [@MiguelBonilla-sys](https://github.com/MiguelBonilla-sys)

---

⭐ **¡Dale una estrella si este proyecto te fue útil!**