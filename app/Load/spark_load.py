import os
from pyspark.sql import DataFrame

class SparkLoader:
    def __init__(self, df: DataFrame):
        self.df = df

    def to_parquet(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        self.df.coalesce(1).write.mode("overwrite").parquet(os.path.join(output_dir, "sports_data.parquet"))

    def to_csv(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        (self.df.coalesce(1)
            .write.mode("overwrite")
            .option("header", True)
            .csv(os.path.join(output_dir, "sports_data_csv")))
        
from pyspark.sql import DataFrame

def write_sqlite_jdbc(df: DataFrame, db_path: str, table: str, sqlite_jdbc_jar: str):
    spark = df.sparkSession
    spark._jsc.addJar(sqlite_jdbc_jar)  # o usa --jars al ejecutar spark-submit
    df.write.format("jdbc").mode("overwrite").options(
        url=f"jdbc:sqlite:{db_path}",
        dbtable=table,
        driver="org.sqlite.JDBC",
    ).save()