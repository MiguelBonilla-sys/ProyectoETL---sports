from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def create_spark(app_name: str = "SportsETL_Spark", shuffle_partitions: int = 4) -> SparkSession:
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions))
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark