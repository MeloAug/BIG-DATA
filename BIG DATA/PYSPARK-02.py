import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

#1. Iniciar a sessão do Spark (o ponto de entrada do seu codigio)
spark = SparkSession.builder\
    .appName("ExemploExplicativo")\
    .getOrCreate()

#2. Criar dados de exemplo (uma lista de tuplas)
dados = [
    ("Ana", "TI", 8500),
    ("Bruno", "TI", 9200),
    ("Carlos", "Marketing", 5000)
]

#Definir as colunas
colunas = ["Nome", "Departamento", "Salario"]

#3. Criar o DataFrame do spark
df = spark.createDataFrame(dados, schema=colunas)

print("----DataFrame Original ----")
df.show()

#4. Filtrar funcionamento do departamento de TI
df_ti = df.filter(col("Departamento") == "TI")

print("--- Apenas Funcionarios de TI ---")
df_ti.show()

#5. Agrupar po departamento e calculara média salarial
df_media = df.groupBy("Departamento").agg(avg("Salario").alias("Media_Salarial"))

print("--- Média Salarial por Departamento ---")
df_media.show()

#encerra a sessão do Spark para liberar memoria
spark.stop()