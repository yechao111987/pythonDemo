import datetime
from pyspark.sql import *
from pyspark.sql.types import *

print datetime.datetime.now().isoformat()

print datetime.datetime.now().date()

spark = SparkSession.builder.appName("Test").getOrCreate()

a = [('Alice', 1), ('Alice', 2), ('Alice', 3), ('yechao', 4), ('yechao', 6)]
# print spark.createDataFrame(a).collect()
# print spark.createDataFrame(a, ['name', 'age']).collect()
schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])
df3 = spark.createDataFrame(a, schema)
arrays = df3.collect()
df3 = df3.withColumn("age", df3.age / df3.count() * 100)
print df3.collect()
list = []
for array in arrays:
    print array
    list.append(array["name"])
    print array["name"]
print list

#
# # print df3.collectAsList()
# df3.createOrReplaceTempView("table")
# df4 = spark.sql("select name as tname,age as tage from table where name like 'Alice'")
# print df4.collect()
# print df4.columns  # result is the columns names
# simple_columns = ["name", "address", "phone"]
# df5 = df3.select([i for i in set(df3.columns) & set(simple_columns)]).fillna("0")
# print df5.collect()
#
# # join
# a1 = [('Alice', 1), ('Alice', 2), ('Alice', 3), ('yechao', 4)]
# a2 = [('Alice', 55), ('haha', 66)]
# df11 = spark.createDataFrame(a1, schema)
# df12 = spark.createDataFrame(a2, schema)
# df13 = df11.join(df12, 'name').select('name')
# # print df13.collectAsList()
