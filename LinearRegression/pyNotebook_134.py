# Databricks notebook source
# DBTITLE 1,load from csv
# Matplotlib config
%matplotlib inline
%config  InlineBackend.figure_formats = ['png']
%config  InlineBackend.rc = {"figure.figsize": (5.0, 3.0)}

import numpy  as np
import pandas as pd

import matplotlib.pyplot  as plt
import seaborn as sns

df_sData = pd.read_csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
df_sData # 53940 rows × 11 columns

# COMMAND ----------

# DBTITLE 1,"format" Feature-Column
xs = df_sData["carat"].to_numpy().reshape(-1, 1)
print(xs.shape)

# COMMAND ----------

# DBTITLE 1,"format" Label-Column
ys = df_sData["price"].to_numpy().reshape(-1, 1)
print(ys.shape)

# COMMAND ----------

# DBTITLE 1,model - train
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# model.fit?
# model.fit(X, y, sample_weight=None)
# X : {array-like, sparse matrix} of shape (n_samples, n_features)  Training data
# y : array-like of shape (n_samples,) or (n_samples, n_targets)    Target values
model.fit(xs, ys)


# COMMAND ----------

# DBTITLE 1,model - predict
## model.predict input as an array !!
## input-Values for LinePlot
x_pred = np.array([0.1, 3])
y_pred = model.predict( x_pred.reshape(-1, 1))  


# COMMAND ----------

# DBTITLE 1,Scatterplot
# Show scatterplot
sp = sns.scatterplot(x="carat", y="price", data=df_sData.sample(500))
ax = sns.lineplot(x = x_pred, y = y_pred.reshape(-1), color = "red")
##sns.scatterplot(x="carat", y="price", data=df)  ##-- !! optik
##sns.scatterplot(x = "carat", y = "price", data=df_sData.sample( len(df_sData) ))  ## len(df) --> "full-Sample" 

plt.title("Diamonds")
plt.xlabel("ct.")
plt.ylabel("USD")
##sns.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ---
