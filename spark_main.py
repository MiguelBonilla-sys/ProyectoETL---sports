import os
from app.Config.spark_config import create_spark
from app.Extract.spark_extract import SparkExtractor
from app.Transform.spark_transform import SparkSportsTransformer
from app.Load.spark_load import SparkLoader  # y opcional write_sqlite_jdbc
from app.Config.config import Config

def print_step(n, title): print(f"\n{'='*20} PASO {n}: {title} {'='*20}")

def main():
    print_step(0, "Inicialización Spark")
    spark = create_spark()

    print_step(1, "Extracción")
    df_raw = SparkExtractor(spark, Config.INPUT_PATH).extract_csv()

    print_step(2, "Transformación")
    transformer = SparkSportsTransformer(df_raw)
    df_tx = transformer.clean_data()
    df_tx = transformer.normalize_data()
    df_tx = transformer.add_calculated_fields()

    print_step(3, "Carga (CSV y SQLite)")
    out_dir = Config.OUTPUT_DIR if hasattr(Config, "OUTPUT_DIR") else "app/Output"
    loader = SparkLoader(df_tx)
    
    # Cargar en CSV
    loader.to_csv(out_dir)
    
    # Cargar en SQLite usando pandas (más simple que JDBC)
    import os
    sqlite_spark_path = os.path.join(out_dir, "sports_data_spark.db")
    loader.to_sqlite(sqlite_spark_path, Config.SQLITE_TABLE)

    print("\nSpark ETL completado exitosamente")
    spark.stop()

if __name__ == "__main__":
    main()