import os
import pandas as pd
from pyspark.sql import DataFrame

class SparkLoader:
    def __init__(self, df: DataFrame):
        self.df = df

    def to_parquet(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        self.df.coalesce(1).write.mode("overwrite").parquet(os.path.join(output_dir, "sports_data.parquet"))

    def to_csv(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        # Usar collect() y pandas para evitar problemas con winutils.exe
        pandas_df = self.df.toPandas()
        output_path = os.path.join(output_dir, "sports_data_spark.csv")
        pandas_df.to_csv(output_path, index=False)
        print(f"Datos guardados en: {output_path}")
        
from pyspark.sql import DataFrame

def write_sqlite_jdbc(df: DataFrame, db_path: str, table: str, sqlite_jdbc_jar: str):
    """Escribe un DataFrame de Spark a SQLite usando JDBC"""
    spark = df.sparkSession
    spark._jsc.addJar(sqlite_jdbc_jar)
    
    # Crear directorio si no existe
    import os
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    df.write.format("jdbc").mode("overwrite").options(
        url=f"jdbc:sqlite:{db_path}",
        dbtable=table,
        driver="org.sqlite.JDBC",
    ).save()
    print(f"Datos guardados en SQLite: {db_path}, tabla: {table}")

class SparkLoader:
    def __init__(self, df: DataFrame):
        self.df = df

    def to_parquet(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        self.df.coalesce(1).write.mode("overwrite").parquet(os.path.join(output_dir, "sports_data.parquet"))

    def to_csv(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        # Usar collect() y pandas para evitar problemas con winutils.exe
        pandas_df = self.df.toPandas()
        output_path = os.path.join(output_dir, "sports_data_spark.csv")
        pandas_df.to_csv(output_path, index=False)
        print(f"Datos guardados en: {output_path}")

    def to_sqlite(self, db_path: str, table: str, sqlite_jdbc_jar: str = None):
        """Carga el DataFrame a SQLite usando pandas (más simple que JDBC)"""
        import sqlite3
        
        # Convertir DataFrame de Spark a pandas
        pandas_df = self.df.toPandas()
        
        # Crear directorio si no existe
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
        
        # Conectar a SQLite y escribir datos
        conn = sqlite3.connect(db_path)
        pandas_df.to_sql(table, conn, if_exists='replace', index=False)
        conn.close()
        
        print(f"Datos guardados en SQLite: {db_path}, tabla: {table}")