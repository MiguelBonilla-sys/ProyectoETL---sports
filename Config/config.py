class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = r'Extract\Files\sports.csv'
    SQLITE_DB_PATH = r'Extract\Files\sports_data.db'
    SQLITE_TABLE = 'sports_results'