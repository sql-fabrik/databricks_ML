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

##  display(dbutils.fs.ls('/databricks-datasets/Rdatasets/data-001/csv/ggplot2/'))

#df_csvFile = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/diamonds.csv.bz2")
#len(df_csvFile)  ##-- 53940
#df_csvFile # 53940 rows × 10 columns

df_sData = pd.read_csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
df_sData # 53940 rows × 11 columns

# COMMAND ----------

# DBTITLE 1,display Table
display(df_sData)  ## show as "Table"

# COMMAND ----------

# DBTITLE 1,Scatterplot
# Show scatterplot
##sns.scatterplot(x="carat", y="price", data=df.sample(500))
##sns.scatterplot(x="carat", y="price", data=df)  ##-- !! optik
sns.scatterplot(x = "carat", y = "price", data=df_sData.sample( len(df_sData) ))  ## len(df) --> "full-Sample" 


plt.title("Diamonds")
plt.xlabel("ct.")
plt.ylabel("USD")
# sns.show()

# COMMAND ----------

# DBTITLE 1,"format" Feature-Column
xs = df_sData["carat"].to_numpy().reshape(-1, 1)
print(xs.shape)

# COMMAND ----------

ys = df_sData["price"].to_numpy().reshape(-1, 1)
print(ys.shape)

# COMMAND ----------

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# model.fit?
# model.fit(X, y, sample_weight=None)
# X : {array-like, sparse matrix} of shape (n_samples, n_features)  Training data
# y : array-like of shape (n_samples,) or (n_samples, n_targets)    Target values
model.fit(xs, ys)


# COMMAND ----------

## 'predictedPrice' = a * 'inputCarat' + b
print(model.coef_)       ##--> a
print(model.intercept_)  ##--> b

# COMMAND ----------

# MAGIC %md
# MAGIC ### Ergebnis = "Geradengleichung"
# MAGIC Preis = 7756.42561797 * Gewicht_in_Carat + (-2256.36058005)

# COMMAND ----------

# DBTITLE 1,"handmade" Function
## Create Function
def get_Price(carat):
    return 7756.42561797 * carat - 2256.36058005

## Exec Function
print( get_Price(1) )
print( get_Price(2) )
print( get_Price(3) )


# COMMAND ----------

# DBTITLE 1,model.predict
## model.predict input as an array !!
model.predict(
  np.array([
             [1]
           , [2]
           , [3]
           ])
)  

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

LRyValue = model.predict( xs )  ## all Diamonds (input "carat")

print(LRyValue.reshape(-1,1))  ## (Linear Regression "y" Value) = "predicted y"
print(LRyValue.shape)

# COMMAND ----------

## combine "data" and "predictions"  -->  allData
allData = np.column_stack( (df_sData, LRyValue) )
print(allData)


# COMMAND ----------

##LRyValue.write.mode("overwrite").saveAsTable("Diamond_predictions")
df_allData = spark.createDataFrame(allData)
df_allData.write.mode("overwrite").saveAsTable("Diamonds_allData")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *, CAST(_12 as int) as pred_Price
# MAGIC FROM   Diamonds_allData
# MAGIC WHERE  _1 in (1,2,3,4, 5, 53936, 53937, 53938)
# MAGIC ORDER  by _1 asc
# MAGIC LIMIT  100
