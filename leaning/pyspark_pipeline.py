from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Create Spark Session
spark = SparkSession.builder \
    .appName("Kafka-PySpark") \
    .getOrCreate()

# Define Schema
schema = StructType().add("message", StringType())

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "pyspark-topic") \
    .load()

# Convert Kafka Message
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write to Console
query = parsed_df.writeStream.outputMode("append").format("console").start()
query.awaitTermination()
