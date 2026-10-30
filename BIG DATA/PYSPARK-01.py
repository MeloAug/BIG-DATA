from pyspark.sql import SparkSession 

spark = SparkSession.builder.appname("Empresa").getOrCreate()

#Ler um arquivo (ex: CSV):

df = spark.read.option("header", True).csv("tweets.csv")

df.show() #Mostra as primeiras linhas
df.printSchema() # Mostra os tipos de dados das colunas

# Contar os registros:
df.count()