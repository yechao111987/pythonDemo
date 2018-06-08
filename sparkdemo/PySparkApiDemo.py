import datetime
from pyspark.sql import *
from pyspark.sql.types import *

# get spark_context
spark_context = SparkSession.builder.appName("apiTest").getOrCreate()

# create DataFrame
# test1:
list = [('Alice', 1), ('Alice', 2), ('Alice', 3), ('yechao', 4), ('yechao', 6)]
df = spark_context.createDataFrame(list)
print df.collect()
# test2:
schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])
df2 = spark.createDataFrame(list, schema)
print(df2.collect())
# test3:
df3 = spark.createDataFrame(list, ['name', 'age'])
print df3.collect()

# withColumn: add a column or replace a column with a new value
df3 = df3.withColumn("age", df3.age / df3.count() * 100)
print df3.collect()
