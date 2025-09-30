from pyspark.sql import DataFrame, SparkSession

class SparkExtractor:
    def __init__(self, spark: SparkSession, file_path: str):
        self.spark = spark
        self.file_path = file_path

    def extract_csv(self) -> DataFrame:
        return (
            self.spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(self.file_path)
        )