import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:8679@localhost:5432/database1')
df = pd.read_sql_query('select * from customer_segments',con=engine)
df.where(df['index'] == 20, inplace=True)
print(df.head(25))