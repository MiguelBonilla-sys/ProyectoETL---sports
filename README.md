# 🏁 ETL Pipeline - Datos Deportivos Le Mans

Pipeline ETL especializado para el procesamiento y análisis de datos de carreras de Le Mans con arquitectura modular robusta.

## 📋 Descripción del Proyecto

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) completo diseñado específicamente para procesar datos históricos de las famosas carreras de Le Mans. El sistema utiliza una arquitectura modular estricta que permite la ingesta, transformación y persistencia de datos deportivos con logging detallado y manejo robusto de errores.

### 🎯 Características Principales

- **Extracción automática** de datos CSV desde archivos fuente
- **Transformaciones especializadas** para datos de automovilismo
- **Persistencia dual** en SQLite (primario) y CSV (respaldo)
- **Categorización inteligente** de velocidad y resistencia
- **Logging visual** con emojis e indicadores de progreso
- **Manejo robusto de errores** con recuperación automática
- **Estadísticas detalladas** de procesamiento

## 🏗️ Arquitectura del Sistema

```
ProyectoETL-sports/
├── 📁 app/
│   ├── 📁 Config/           # Configuración centralizada
│   │   ├── config.py        # Rutas y parámetros del sistema
│   │   └── __init__.py
│   ├── 📁 Extract/          # Módulo de extracción de datos
│   │   ├── SportsExtract.py # Lector CSV con manejo de errores
│   │   ├── Files/           # Directorio de archivos fuente
│   │   │   └── data.csv     # Datos de carreras de Le Mans
│   │   └── __init__.py
│   ├── 📁 Transform/        # Módulo de transformación
│   │   ├── SportsTransformer.py # Lógica de transformación específica
│   │   └── __init__.py
│   ├── 📁 Load/             # Módulo de carga de datos
│   │   ├── SportsLoader.py  # Persistencia dual SQLite/CSV
│   │   └── __init__.py
│   ├── 📁 Output/           # Destinos finales de datos
│   │   ├── sports_data.db   # Base de datos SQLite
│   │   └── sports_data_processed.csv # CSV procesado
│   └── 📁 Visualize/        # Módulo de visualización (en desarrollo)
├── 📄 main.py               # Orquestador principal del pipeline
├── 📄 requirements.txt      # Dependencias del proyecto
├── 📄 README.md             # Este archivo
└── 📄 LICENSE               # Licencia del proyecto
```
