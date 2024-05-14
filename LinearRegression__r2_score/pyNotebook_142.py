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
# MAGIC
# MAGIC ## instead of ...
# MAGIC ## df_sData = df_sData.sample(frac = 1)

# COMMAND ----------

# DBTITLE 1,train_test_split
from sklearn.model_selection import train_test_split

train_test_split([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10], train_size = 0.8)
##train_test_split([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10], [81, 82, 83, 84, 85, 86, 87, 88, 89 ,810], train_size = 0.8)

# COMMAND ----------

# DBTITLE 1,train_test_split to variables
train, test = train_test_split([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10], train_size = 0.8)
print(train)
print(test)

# COMMAND ----------

from sklearn.linear_model import LinearRegression

X = df_sData[["carat"]].to_numpy().reshape(-1, 1)
y = df_sData[["price"]].to_numpy().reshape(-1, 1)
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 42)
print(X_train.shape)
print(y_train.shape)


# COMMAND ----------

# DBTITLE 1,model.fit
model = LinearRegression()
model.fit(X_train, y_train)

# COMMAND ----------

# DBTITLE 1,model.score
model.score(X_train, y_train)

