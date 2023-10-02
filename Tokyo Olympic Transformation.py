# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "*******key******",
"fs.azure.account.oauth2.client.secret": '*******key******',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/***key***/oauth2/token"}


dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicdatakn.dfs.core.windows.net/", # contrainer@storageaccountname
mount_point = "/mnt/tokyoolymic",
extra_configs = configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/tokyoolymic"

# COMMAND ----------

spark

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/coaches.csv")
gender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/gender.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/teams.csv")

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------


coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

gender.show()

     

# COMMAND ----------

gender.printSchema()
     

# COMMAND ----------

gender = gender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("Male").cast(IntegerType()))\
        .withColumn("Total",col("Total").cast(IntegerType()))

# COMMAND ----------

medals.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).select("Team/NOC","Gold").show()

# COMMAND ----------


# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = gender.withColumn(
    'Avg_Female', gender['Female'] / gender['Total']
).withColumn(
    'Avg_Male', gender['Male'] / gender['Total']
)
average_entries_by_gender.show()

# COMMAND ----------

athletes.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/tokyoolymic/transformed-data/tf_athletes")
coaches.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/tf_coaches")
gender.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/tf_gender")
medals.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/tf_medals")
teams.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/tf_teams")

# COMMAND ----------


