from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import udf, split, col,regexp_replace
import os
import findspark
if __name__ == "__main__":
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 pyspark-shell'
    findspark.find()
    spark = SparkSession.builder.appName("Kafka_Read_Up_Coming_Match").getOrCreate()
    kafka_params = {
        "kafka.bootstrap.servers": "localhost:9092",
        "subscribe": "UpComingMatch_Topic" 
    }

    df = spark.readStream.format("kafka") \
        .options(**kafka_params) \
        .load()
    df = df.selectExpr("CAST(value AS STRING)")
    df=df.select("value")
    df = df.withColumn("value", regexp_replace(df["value"], '"', ''))    
    column_names = [
    "Match_Date", "League", "Home_Team", "Away_Team", "Home_Player1", "Home_Player2",
    "Home_Player3", "Home_Player4", "Home_Player5", "Home_Player6", "Home_Player7",
    "Home_Player8", "Home_Player9", "Home_Player10", "Home_Player11", "Away_Player1",
    "Away_Player2", "Away_Player3", "Away_Player4", "Away_Player5", "Away_Player6",
    "Away_Player7", "Away_Player8", "Away_Player9", "Away_Player10", "Away_Player11",
    "Home_Kit1", "Home_Kit2", "Home_Kit3", "Home_Kit4", "Home_Kit5", "Home_Kit6",
    "Home_Kit7", "Home_Kit8", "Home_Kit9", "Home_Kit10", "Home_Kit11", "Away_Kit1",
    "Away_Kit2", "Away_Kit3", "Away_Kit4", "Away_Kit5", "Away_Kit6", "Away_Kit7",
    "Away_Kit8", "Away_Kit9", "Away_Kit10", "Away_Kit11"
]
    split_col = split(df["value"], ",")
    for i, col_name in enumerate(column_names):
        df = df.withColumn(col_name, split_col.getItem(i))
    df = df.drop("value")
    query = df.writeStream\
            .format("csv")\
            .outputMode("append")\
            .option("checkpointLocation", "./output/checkpoint") \
            .option("path", "./output/csv") \
            .trigger(processingTime='3 seconds')\
            .option("encoding", "UTF-8")\
            .option("header", "true")\
            .start()
    # query = df.writeStream\
    #         .format("csv")\
    #         .outputMode("append")\
    #         .option("checkpointLocation", "hdfs://localhost:9000/output/checkpoint") \
    #         .option("path", "hdfs://localhost:9000/output/csv") \
    #         .trigger(processingTime='3 seconds')\
    #         .option("encoding", "UTF-8")\
    #         .option("header", "true")\
    #         .start()
    


    query.awaitTermination()