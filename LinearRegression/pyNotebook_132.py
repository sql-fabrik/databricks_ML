# Databricks notebook source
# MAGIC %md
# MAGIC ##Context
# MAGIC
# MAGIC [kaggle source: https://www.kaggle.com/datasets/shivam2503/diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds)                                               <br>
# MAGIC <br>
# MAGIC diamont dataset contains the prices and other attributes of almost 54,000 diamonds.                                 <br>
# MAGIC * price price in US dollars (\$326--\$18,823)                                                                       <br>
# MAGIC * carat weight of the diamond (0.2--5.01)                                                                           <br>
# MAGIC * cut quality of the cut (Fair, Good, Very Good, Premium, Ideal)                                                    <br>
# MAGIC * color diamond colour, from J (worst) to D (best)                                                                  <br>
# MAGIC * clarity a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))         <br>
# MAGIC * depth total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)                                          <br>
# MAGIC * table width of top of diamond relative to widest point (43--95)                                                   <br>
# MAGIC * x length in mm (0--10.74)                                                                                         <br>
# MAGIC * y width in mm (0--58.9)                                                                                           <br>
# MAGIC * z depth in mm (0--31.8)                                                                                           <br>
# MAGIC ---
# MAGIC more [databricks-datasets.html](https://docs.databricks.com/en/discover/databricks-datasets.html)                        <br>

# COMMAND ----------

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

# DBTITLE 1,model - get return-Values
## 'predictedPrice' = a * 'inputCarat' + b
print(model.coef_)       ##--> a
print(model.intercept_)  ##--> b

# COMMAND ----------

# MAGIC %md
# MAGIC ### Ergebnis = "Geradengleichung"
# MAGIC Preis = 7756.42561797 * Gewicht_in_Carat + (-2256.36058005)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC
