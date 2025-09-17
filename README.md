# 🏁 ETL Pipeline - Datos Deportivos Le Mans

## 🚀 Descripción del Proyecto

Este es un pipeline ETL (Extract, Transform, Load) especializado para el procesamiento de datos históricos de carreras de Le Mans. El proyecto implementa una arquitectura modular robusta que transforma datos en bruto de carreras automovilísticas en información estructurada y analizable.

### ✨ Características Principales

- **🔄 Pipeline ETL Completo**: Extracción, transformación y carga automatizada
- **📊 Análisis Específico de Automovilismo**: Categorización por velocidad, resistencia y eficiencia
- **💾 Persistencia Dual**: Almacenamiento en SQLite y CSV para máxima compatibilidad
- **🛡️ Manejo Robusto de Errores**: Continuidad ante fallos individuales con logging detallado
- **⚙️ Configuración Centralizada**: Gestión de rutas y parámetros en un solo lugar
- **📈 Campos Calculados Inteligentes**: Métricas automáticas para análisis avanzado

## 🏗️ Arquitectura del Proyecto

```text
ProyectoETL - sports/
├── 📂 app/                           # Módulos del pipeline (compilados)
│   ├── Config/                       # Configuración centralizada
│   ├── Extract/                      # Extracción de datos
│   ├── Load/                         # Carga y persistencia
│   ├── Transform/                    # Transformaciones de datos
│   └── Visualize/                    # Visualización (futuro)
├── 📂 Config/                        # Configuración del proyecto
│   ├── __init__.py
│   └── config.py                     # Rutas y parámetros centralizados
├── 📂 Extract/                       # Módulo de extracción
│   ├── __init__.py
│   ├── SportsExtract.py             # Extractor de datos CSV
│   └── Files/
│       └── data.csv                 # Datos fuente de Le Mans
├── 📂 Transform/                     # Módulo de transformación
│   ├── __init__.py
│   └── SportsTransformer.py         # Transformador especializado
├── 📂 Load/                          # Módulo de carga
│   ├── __init__.py
│   └── SportsLoader.py              # Loader dual (SQLite + CSV)
├── 📂 Output/                        # Destinos de datos procesados
│   ├── sports_data.db               # Base de datos SQLite
│   └── sports_data_processed.csv    # CSV procesado
├── 🐍 main.py                        # Orquestador principal del pipeline
├── 📋 requirements.txt               # Dependencias Python
├── 🔒 .env                          # Variables de entorno (Supabase)
└── 📖 README.md                     # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.13**: Lenguaje principal del proyecto
- **Pandas 2.3.2**: Manipulación y análisis de datos
- **NumPy 2.3.2**: Operaciones numéricas y arrays
- **SQLite3**: Base de datos local integrada
- **Supabase**: Base de datos en la nube (configurada)

## 📋 Requisitos del Sistema

- **Python**: 3.10 o superior (recomendado 3.13)
- **Sistema Operativo**: Windows (rutas optimizadas)
- **RAM**: Mínimo 512MB para datasets pequeños
- **Almacenamiento**: 100MB libres para datos y outputs

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/MiguelBonilla-sys/ProyectoETL---sports.git
cd ProyectoETL---sports
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Verificar Estructura de Datos

Asegúrate de que tu archivo CSV en `Extract/Files/data.csv` contenga las siguientes columnas:

- `Year`: Año de la carrera
- `Drivers`: Nombres de los conductores
- `Class`: Clase del vehículo
- `Team`: Equipo participante
- `Car`: Modelo del automóvil
- `Tyre`: Marca de neumáticos
- `Laps`: Número de vueltas completadas
- `Km`: Kilómetros recorridos
- `Mi`: Millas recorridas
- `Series`: Serie de competición
- `Driver_nationality`: Nacionalidad del conductor
- `Team_nationality`: Nacionalidad del equipo
- `Average_speed_kmh`: Velocidad promedio en km/h
- `Average_speed_mph`: Velocidad promedio en mph
- `Average_lap_time`: Tiempo promedio por vuelta

## 🎯 Uso del Pipeline

### Ejecución Básica

```bash
python main.py
```

Este comando ejecutará todo el pipeline ETL con salida detallada:

```text
============================================================
🏁 ETL PIPELINE - DATOS DEPORTIVOS LE MANS 🏁
============================================================

==================== PASO 1: EXTRACCIÓN DE DATOS ====================
📂 Archivo fuente: Extract\Files\data.csv
✅ Datos extraídos exitosamente
📊 Filas extraídas: 228
📋 Columnas encontradas: 15

==================== PASO 2: TRANSFORMACIÓN DE DATOS ====================
📊 Iniciando limpieza de datos...
🔧 Normalizando datos...
➕ Agregando campos calculados...
✅ Transformación completada

==================== PASO 3: CARGA DE DATOS ====================
💾 Guardando en base de datos SQLite...
📄 Guardando en archivo CSV...
✅ Carga completada exitosamente
```

### Ejecución por Módulos

También puedes ejecutar cada etapa por separado:

```python
from Extract.SportsExtract import Extractor
from Transform.SportsTransformer import SportsTransformer
from Load.SportsLoader import Loader

# Solo extracción
extractor = Extractor('Extract/Files/data.csv')
df = extractor.extract()

# Solo transformación
transformer = SportsTransformer(df)
df_clean = transformer.transform()

# Solo carga
loader = Loader(df_clean)
loader.to_sqlite()
loader.to_csv('mi_archivo.csv')
```

## 🔧 Configuración Avanzada

### Personalizar Rutas (`Config/config.py`)

```python
class Config:
    # Rutas personalizadas
    INPUT_PATH = r'mi_carpeta\mis_datos.csv'
    OUTPUT_DIR = r'mi_output'
    SQLITE_DB_PATH = r'mi_output\mi_base.db'
    
    # Categorías personalizadas
    SPEED_CATEGORIES = {
        'bins': [0, 80, 120, 160, float('inf')],
        'labels': ['Lento', 'Moderado', 'Rápido', 'Muy Rápido']
    }
```

### Variables de Entorno (`.env`)

El proyecto incluye configuración para Supabase como base de datos en la nube:

```env
DATABASE_URL=postgresql://usuario:password@host:puerto/database
ENVIRONMENT=production
DEBUG=False
```

## 📊 Campos Calculados Automáticos

El transformer genera automáticamente:

### 📅 Década

- Agrupa años en décadas (1920s, 1930s, etc.)
- Útil para análisis temporales

### 🏃 Categorías de Velocidad

- **Slow**: 0-100 km/h
- **Medium**: 100-150 km/h  
- **Fast**: 150-200 km/h
- **Very Fast**: >200 km/h

### 🏁 Categorías de Resistencia

- **Short**: 0-100 vueltas
- **Medium**: 100-150 vueltas
- **Long**: 150-200 vueltas
- **Ultra Long**: >200 vueltas

### ⚡ Eficiencia

- **Km_per_Lap**: Distancia promedio por vuelta
- Métrica clave para evaluar configuraciones de circuito

## 📈 Outputs Generados

### 1. Base de Datos SQLite (`Output/sports_data.db`)

- Tabla `sports_results` con todos los datos transformados
- Índices automáticos para consultas rápidas
- Compatible con cualquier herramienta de análisis SQL

### 2. Archivo CSV Procesado (`Output/sports_data_processed.csv`)

- Formato universal para análisis en Excel, R, Python
- Incluye todos los campos originales + calculados
- Codificación UTF-8 para caracteres especiales

## 🐛 Manejo de Errores

El pipeline incluye manejo robusto de errores:

- **Datos Faltantes**: Conversión automática a NaN
- **Duplicados**: Eliminación automática con reporte
- **Archivos Corruptos**: Mensajes claros de error
- **Rutas Inexistentes**: Creación automática de directorios
- **Permisos de Escritura**: Fallback a directorio actual

## 🧪 Validación de Datos

### Estadísticas Automáticas

```python
# El transformer proporciona estadísticas detalladas
transformer = SportsTransformer(df)
df_clean = transformer.transform()
stats = transformer.get_summary_stats()
print(stats)
```

### Verificaciones Incluidas

- ✅ Rango de años válidos (1920-2025)
- ✅ Velocidades realistas (>0 km/h)
- ✅ Número de vueltas positivas
- ✅ Consistencia entre kilómetros y millas

## 🌟 Casos de Uso

### 1. Análisis Histórico de Le Mans

```python
# Evolución de velocidades por década
df_analysis = df_clean.groupby('Decade')['Average_speed_kmh'].mean()
```

### 2. Comparación de Equipos

```python
# Rendimiento por equipo
team_performance = df_clean.groupby('Team').agg({
    'Average_speed_kmh': 'mean',
    'Laps': 'mean',
    'Year': 'count'
})
```

### 3. Análisis de Eficiencia

```python
# Mejores configuraciones de neumáticos
tyre_efficiency = df_clean.groupby('Tyre')['Km_per_Lap'].mean().sort_values(ascending=False)
```

## 🚀 Roadmap y Futuras Funcionalidades

### Versión Actual (Development Branch)

- ✅ Pipeline ETL básico funcional
- ✅ Transformaciones específicas de automovilismo
- ✅ Persistencia dual SQLite + CSV
- ✅ Configuración centralizada

### Próximas Versiones

- 📊 **Módulo de Visualización**: Gráficos automáticos con matplotlib/plotly
- 🌐 **API REST**: Endpoints para consultas en tiempo real
- 📱 **Dashboard Web**: Interfaz interactiva con Streamlit
- 🔄 **ETL Incremental**: Procesamiento de actualizaciones automáticas
- 📡 **Integración Supabase**: Carga automática a la nube
- 🤖 **ML Pipeline**: Predicciones de rendimiento de carreras

## 🤝 Contribución

### Cómo Contribuir

1. **Fork** el repositorio
2. Crear una **branch** de feature: `git checkout -b feature/nueva-funcionalidad`
3. **Commit** los cambios: `git commit -m 'Add: nueva funcionalidad'`
4. **Push** a la branch: `git push origin feature/nueva-funcionalidad`
5. Abrir un **Pull Request**

### Estándares de Código

- **PEP 8**: Seguir convenciones de Python
- **Docstrings**: Documentar todas las funciones
- **Type Hints**: Usar anotaciones de tipo cuando sea posible
- **Tests**: Incluir pruebas unitarias para nuevas funcionalidades

### Estructura de Branches

- `main`: Código estable en producción
- `development`: Desarrollo activo (branch actual)
- `release`: Preparación de releases
- `feature/*`: Nuevas funcionalidades
- `bugfix/*`: Corrección de errores

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **Miguel Bonilla** - [@MiguelBonilla-sys](https://github.com/MiguelBonilla-sys)

## 🙏 Agradecimientos

- Datos históricos de Le Mans proporcionados por fuentes públicas
- Comunidad Python por las excelentes librerías de análisis de datos
- Contribuidores del proyecto y testers beta

## 📞 Soporte

¿Tienes preguntas o necesitas ayuda?

- 📧 **Email**: Abrir un issue en GitHub
- 📋 **Issues**: [GitHub Issues](https://github.com/MiguelBonilla-sys/ProyectoETL---sports/issues)
- 📖 **Documentación**: Este README y comentarios en el código
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/MiguelBonilla-sys/ProyectoETL---sports/discussions)

---

⭐ **¡Si este proyecto te resulta útil, considera darle una estrella en GitHub!** ⭐

