"""    
    ../spark-2.4.3-bin-hadoop2.7/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 /home/rsi-psd-vm/Documents/rsi-psd-project/sparkProcessor.py localhost:9092 subscribe probes
"""
from __future__ import print_function

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
# from pyspark.sql.functions import desc
from pyspark.sql.functions import approxCountDistinct
from tbIntegration import processGraph2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
        Usage: file.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        sys.exit(-1)

    bootstrapServers = sys.argv[1]
    subscribeType = sys.argv[2]
    topics = sys.argv[3]

    spark = SparkSession\
        .builder\
        .appName("ProbeCapture")\
        .getOrCreate()

    kafka = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .load()\
        .selectExpr("CAST(value AS STRING)")

    spl = split(kafka['value'], '#')

    dfAll = kafka\
        .withColumn('mac', spl.getItem(0))\
        .withColumn('vendor', spl.getItem(1))\
        .withColumn('ssid', spl.getItem(2))\
        .withColumn('ts', spl.getItem(3))\
        .drop('value')
    
    dfNotBroadcast = dfAll.filter(dfAll.ssid != 'BROADCAST')\
        .groupBy('vendor')\
        .agg(approxCountDistinct('mac').alias('macsDistinct'))


    query = dfNotBroadcast\
        .writeStream\
        .outputMode('complete')\
        .foreach(processGraph2)\
        .start()
        # .format('console')\

    query.awaitTermination()
