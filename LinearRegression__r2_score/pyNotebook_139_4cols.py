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
# MAGIC df_sData = pd.read_csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
# MAGIC ## df_sData # 53940 rows × 11 columns

# COMMAND ----------

# MAGIC %md
# MAGIC ## multi-feature
# MAGIC Geradengleichung: <br>
# MAGIC price = ( a * 'inputCarat' + b * 'x_Size' + c * 'y_size' + d * 'z_size') + e
# MAGIC

# COMMAND ----------

# DBTITLE 1,SELECT columns
##df_rowsTbl = sqlContext.table("diamonds_alldata")
df_rowsTbl = sqlContext.sql("""
                             SELECT carat, x_size, y_size, z_size  -- features 
                                  , price                          -- label
                             FROM   diamonds_alldata 
                             """)

df_rowsTbl.show()

# COMMAND ----------

# DBTITLE 1,model.fit
from sklearn.linear_model import LinearRegression

model = LinearRegression()

X_train = df_sData[["carat", "x", "y", "z"]].to_numpy().reshape(-1, 4)
y_train = df_sData[["price"]].to_numpy().reshape(-1, 1)
#print(X_train.shape)
#print(y_train.shape)

model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# COMMAND ----------

# DBTITLE 1,model.score
model.score(X_train, y_train)

