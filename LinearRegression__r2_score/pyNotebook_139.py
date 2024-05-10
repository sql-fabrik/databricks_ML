# Databricks notebook source
# MAGIC %matplotlib inline
# MAGIC %config  InlineBackend.figure_formats = ['png']
# MAGIC %config  InlineBackend.rc = {"figure.figsize": (5.0, 3.0)}
# MAGIC
# MAGIC import numpy  as np
# MAGIC import pandas as pd
# MAGIC
# MAGIC import matplotlib.pyplot  as plt
# MAGIC import seaborn as sns
# MAGIC
# MAGIC ## df_sData = pd.read_csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
# MAGIC ## df_sData # 53940 rows × 11 columns

# COMMAND ----------

# DBTITLE 1,SELECT columns
##df_rowsTbl = sqlContext.table("diamonds_alldata")
df_rowsTbl = sqlContext.sql("""
                             SELECT carat, price             
                             FROM   diamonds_alldata 
                             """)

df_rowsTbl.show()

# COMMAND ----------

# DBTITLE 1,model.fit
from sklearn.linear_model import LinearRegression

xs = df_rowsTbl.select(df_rowsTbl["carat"]).toPandas().values.reshape(-1, 1)
ys = df_rowsTbl.select(df_rowsTbl["price"]).toPandas().values.reshape(-1, 1)
print(xs.shape)
print(ys.shape)

##sns.scatterplot(x = xs, y = ys)

model = LinearRegression()
model.fit(xs, ys)

y_pred = model.predict(xs)

# COMMAND ----------

# DBTITLE 1,2_score
from sklearn.metrics import r2_score

r2_score(ys, y_pred)


# COMMAND ----------

## oder ...
model.score(xs, ys)
