import duckdb

#Conecta a uma instãncia do Duckdb em memoria [15]
con = duckdb.connect(database=':memory:')

#Consulta SQL lendo diretamente o arquivo Parquet [12, 15]
query_parquet = """
SELECT
    customer_id,
    COUNT(order_id) AS total_pedidos,
    ROUND(SUM(amount), 2) AS valor_total
FROM 'orders.parquet'
WHERE status = 'completed'
GROUP BY customer_id
ORDER BY valor_total DESC
"""
df_resultado_parquet = con.execute(query_parquet).fetchdf()
print("---Resultado DuckDB(Consulta Direta em Parquet)---")
print(df_resultado_parquet)