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
# MAGIC df_sData # 53940 rows × 11 columns

# COMMAND ----------

# MAGIC %md
# MAGIC ## multi-feature
# MAGIC Geradengleichung: <br>
# MAGIC price = ( a * 'inputCarat' + b * 'x_Size' ) + c
# MAGIC

# COMMAND ----------

from sklearn.linear_model import LinearRegression

model = LinearRegression()

X_train = df_sData[["carat", "x"]].to_numpy().reshape(-1, 2)
y_train = df_sData[["price"]].to_numpy().reshape(-1, 1)

## print(y_train.shape)
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# COMMAND ----------

X_pred = np.array(
    [[1.01, 6.3]
    ,[1.02, 6.4]
    ]
)

y_pred = model.predict(X_pred)
print(y_pred)

## refer to Id 13492, 13493
