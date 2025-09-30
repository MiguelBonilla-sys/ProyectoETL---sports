from pyspark.sql import DataFrame, functions as F, types as T
from pyspark.sql.functions import when, col, isnan, isnull

TEXT_COLS = ['Drivers','Team','Car','Tyre','Series','Driver_nationality','Team_nationality']
NUM_COLS = ['Year','Laps','Km','Mi','Average_speed_kmh','Average_speed_mph','Average_lap_time']

def safe_cast_to_double(df, column_name):
    """Convierte una columna a double de manera segura, manejando valores malformados"""
    return df.withColumn(
        column_name,
        when(col(column_name).rlike("^[+-]?\\d*\\.?\\d+$"), col(column_name).cast("double"))
        .otherwise(None)
    )

class SparkSportsTransformer:
    def __init__(self, df: DataFrame):
        self.df = df

    def clean_data(self) -> DataFrame:
        # eliminar filas completamente nulas
        df = self.df.na.drop(how="all").dropDuplicates()
        self.df = df
        return self.df

    def normalize_data(self) -> DataFrame:
        df = self.df
        # columnas de texto: trim y title-case simple
        for col in TEXT_COLS:
            if col in df.columns:
                df = df.withColumn(col, F.initcap(F.trim(F.col(col).cast("string"))))
        # columnas numéricas usando conversión segura
        for col_name in NUM_COLS:
            if col_name in df.columns:
                df = safe_cast_to_double(df, col_name)
        # limpiar Class usando conversión segura
        if "Class" in df.columns:
            df = df.withColumn("Class", F.regexp_replace(F.col("Class").cast("string"), ">", ""))
            df = safe_cast_to_double(df, "Class")
        self.df = df
        return self.df

    def add_calculated_fields(self) -> DataFrame:
        df = self.df
        if "Year" in df.columns:
            df = df.withColumn("Decade", (F.floor(F.col("Year")/10)*10).cast("int"))
        if "Average_speed_kmh" in df.columns:
            df = df.withColumn(
                "Speed_Category",
                F.when(F.col("Average_speed_kmh") <= 100, F.lit("Slow"))
                 .when(F.col("Average_speed_kmh") <= 150, F.lit("Medium"))
                 .when(F.col("Average_speed_kmh") <= 200, F.lit("Fast"))
                 .otherwise(F.lit("Very Fast"))
            )
        if "Laps" in df.columns:
            df = df.withColumn(
                "Endurance_Category",
                F.when(F.col("Laps") <= 100, F.lit("Short"))
                 .when(F.col("Laps") <= 150, F.lit("Medium"))
                 .when(F.col("Laps") <= 200, F.lit("Long"))
                 .otherwise(F.lit("Ultra Long"))
            )
        if "Km" in df.columns and "Laps" in df.columns:
            df = df.withColumn("Km_per_Lap", F.round(F.col("Km")/F.col("Laps"), 2))
        self.df = df
        return self.df

    def transform(self) -> DataFrame:
        return self.add_calculated_fields(
        ) if (self.normalize_data() or True) and (self.clean_data() or True) else self.df