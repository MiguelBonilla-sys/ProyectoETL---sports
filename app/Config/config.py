class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    # Rutas de entrada
    INPUT_PATH = r'app\Extract\Files\data.csv'
    
    # Rutas de salida
    OUTPUT_DIR = r'app\Output'
    SQLITE_DB_PATH = r'app\Output\sports_data.db'
    CSV_OUTPUT_PATH = r'app\Output\sports_data_processed.csv'
    
    # Configuración de base de datos
    SQLITE_TABLE = 'sports_results'
    
    # Configuración de transformación
    SPEED_CATEGORIES = {
        'bins': [0, 100, 150, 200, float('inf')],
        'labels': ['Slow', 'Medium', 'Fast', 'Very Fast']
    }
    
    ENDURANCE_CATEGORIES = {
        'bins': [0, 100, 150, 200, float('inf')],
        'labels': ['Short', 'Medium', 'Long', 'Ultra Long']
    }