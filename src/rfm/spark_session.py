from pyspark.sql import SparkSession

def get_spark(app_name="RFM"):
    return (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .getOrCreate()
    )
