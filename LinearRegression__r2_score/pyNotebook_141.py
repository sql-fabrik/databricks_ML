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
# MAGIC ########### loop
# MAGIC ## df_sData = df_sData.sample(frac = 1)

# COMMAND ----------

# DBTITLE 1,SELECT columns
##df_rowsTbl = sqlContext.table("diamonds_alldata")
df_rowsTbl = sqlContext.sql("""
                             SELECT carat     -- features 
                                  , price     -- label
                             FROM   diamonds_alldata 
                             """)

df_rowsTbl.show()

# COMMAND ----------

df_train = df_sData.iloc[:40000]
df_test  = df_sData.iloc[40000:]

# COMMAND ----------

# DBTITLE 1,model.fit
from sklearn.linear_model import LinearRegression

X_train = df_train[["carat"]].to_numpy().reshape(-1, 1)
y_train = df_train[["price"]].to_numpy().reshape(-1, 1)
#print(X_train.shape)
#print(y_train.shape)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# COMMAND ----------

# DBTITLE 1,model.score
model.score(X_train, y_train)


# COMMAND ----------

# DBTITLE 1,model.predict
X_test = df_test[["carat"]].to_numpy().reshape(-1, 1)
y_test = df_test[["price"]].to_numpy().reshape(-1, 1)

model.score(X_test, y_test)
##  -1.051...

##  das war wohl nix :-(
##  "die Sortierung" in der Liste.

# COMMAND ----------

# DBTITLE 1,loop  with "sample(frac = 1)
df_rand = df_sData.sample(frac = 1)
