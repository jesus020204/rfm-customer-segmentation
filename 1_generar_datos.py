import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)

num_records = 50000
clientes = [fake.uuid4() for _ in range(5000)]
productos = [fake.ean(length=8) for _ in range(100)]

data = {
    'transaccion_id': [fake.uuid4() for _ in range(num_records)],
    'cliente_id': np.random.choice(clientes, num_records),
    'producto_id': np.random.choice(productos, num_records),
    'fecha_transaccion': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
    'monto': np.round(np.random.uniform(10.0, 500.0, num_records), 2)
}

df = pd.DataFrame(data)

indices_fechas = df.sample(frac=0.05, random_state=1).index
df.loc[indices_fechas, 'fecha_transaccion'] = df.loc[indices_fechas, 'fecha_transaccion'] + timedelta(days=3650)

indices_nulos = df.sample(frac=0.03, random_state=2).index
df.loc[indices_nulos, 'monto'] = np.nan

indices_negativos = df.sample(frac=0.02, random_state=3).index
df.loc[indices_negativos, 'monto'] = df.loc[indices_negativos, 'monto'] * -1

df.to_csv('transacciones_ecommerce_raw.csv', index=False)