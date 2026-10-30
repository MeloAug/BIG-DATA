from pyspark.sql import SparkSession

#Inicializa a sessão do Spark
spark = SparkSession.builder.appNam("PySpark Exemple").geOrCreate()

#cria o Dataframe e executa filtros e agrupações 
data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
df_spark = spark.createDataFrame(data,["Name", "Age"])

#Filtragem de daos [26]

df_spark_filtered = df_spark.filter(df_spark["Age"] > 30)
df_spark_filtered.show