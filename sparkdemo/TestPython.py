import datetime
from pyspark.sql import *
from pyspark.sql.types import *

print datetime.datetime.now().isoformat()

print datetime.datetime.now().date()

spark = SparkSession.builder.appName("Test").getOrCreate()

a = [('Alice', 1), ('Alice', 2), ('Alice', 3), ('yechao', 4)]
print spark.createDataFrame(a).collect()
print spark.createDataFrame(a, ['name', 'age']).collect()
schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])
df3 = spark.createDataFrame(a, schema)
print df3.collect()
df3.createOrReplaceTempView("table")
df4 = spark.sql("select name as tname,age as tage from table where name like 'Alice'")
print df4.collect()
