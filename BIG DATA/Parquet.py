#python.exe -m pip install deltalake 
#python.exe -m pip install pqarquet
#python.exe -m pip install pyarrow
import pandas as pd 
from deltalake import write_deltalake

#criando conjuntos de dados de exemplo
df_orders = pd.DataFrame({
    'order_id': [4,8],
    'customer_id': [9,11],
    'amount': [250.0, 450.5],
    'status': ['completed', 'completed']
})

print(df_orders)

#1. Salva em formato parquet colunar usando pyarrow e compressão Snappy
df_orders.to_parquet('orders.parquet', engine='pyarrow', compression='snappy')
#2. Grava em tabela delta lake com particionamento por status
write_deltalake('./my_delta_table', df_orders, partition_by=['status'], mode='overwrite')