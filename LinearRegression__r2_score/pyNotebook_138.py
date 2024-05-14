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

# DBTITLE 1,filter by Id
##df_rowsTbl = sqlContext.table("diamonds_alldata")
df_rowsTbl = sqlContext.sql("""
                             SELECT *             
                             FROM   diamonds_alldata 
                             WHERE  Id in (10, 9310, 14660, 25453, 26108, 26933, 34950, 48400) 
                             ORDER  by carat
                             """)

df_rowsTbl.show()

# COMMAND ----------

xs = df_rowsTbl.select(df_rowsTbl["carat"]).toPandas().values.reshape(-1,)
ys = df_rowsTbl.select(df_rowsTbl["price"]).toPandas().values.reshape(-1,)
##print(xs.shape)
##print(ys.shape)

sns.scatterplot(x = xs, y = ys)
##----
x_line = [0.2  ,  3.5]
y_line = [500  ,17500]
sns.lineplot(x = x_line, y = y_line, color="red")
##----


# COMMAND ----------

# DBTITLE 1,avg
df_avgTbl = sqlContext.sql("""
                             SELECT avg(price)  as avg_price
                             FROM   diamonds_alldata 
                             WHERE  Id in (10, 9310, 14660, 25453, 26108, 26933, 34950, 48400) 
                             """)

df_avgTbl.show()

# COMMAND ----------

xs = df_rowsTbl.select(df_rowsTbl["carat"]).toPandas().values.reshape(-1,)
ys = df_rowsTbl.select(df_rowsTbl["price"]).toPandas().values.reshape(-1,)
##print(xs.shape)
##print(ys.shape)

sns.scatterplot(x = xs, y = ys)
##----
x_line = [0.2  ,  3.5]
y_line = [500  ,17500]
sns.lineplot(x = x_line, y = y_line, color="red")
##----
x_avg  = x_line 
y_avg  = [7466 , 7466]
sns.lineplot(x = x_avg, y = y_avg, color="blue")


# COMMAND ----------

# DBTITLE 1,extra sample linewidth
data = { 'x': [1, 2, 3, 4,  5]
       , 'y': [2, 4, 6, 8, 10]}

# Create the lineplot
sns.lineplot(data=data, x='x', y='y', color='black', linewidth=1)


# COMMAND ----------

# DBTITLE 1,Scatter Plot with Lines
xs = df_rowsTbl.select(df_rowsTbl["carat"]).toPandas().values.reshape(-1,)
ys = df_rowsTbl.select(df_rowsTbl["price"]).toPandas().values.reshape(-1,)
##print(xs.shape)
##print(ys.shape)

sns.scatterplot(x = xs, y = ys)
##----
x_line = [0.2  ,  3.5]
y_line = [500  ,17500]
sns.lineplot(x = x_line, y = y_line, color="red")
##----
x_avg  = x_line 
y_avg  = [7466 , 7466]
sns.lineplot(x = x_avg, y = y_avg, color="blue")
##----
x_d1   = [0.59, 0.59]
x_d2   = [1.52, 1.52]
x_d3   = [2.24, 2.24]
x_d4   = [3.00, 3.00]

y_d1   = [ 1968, 7466]
y_d2   = [ 5916, 7466]
y_d3   = [15375, 7466]
y_d4   = [16970, 7466]

sns.lineplot(x = x_d1, y = y_d1, color='black', linewidth=3)
sns.lineplot(x = x_d2, y = y_d2, color='black', linewidth=3)
sns.lineplot(x = x_d3, y = y_d3, color='black', linewidth=3)
sns.lineplot(x = x_d4, y = y_d4, color='black', linewidth=3)

# COMMAND ----------

# MAGIC %md
# MAGIC R² Score
# MAGIC
# MAGIC R² = 1  wenn Modell die Daten "perfekt" beschreibt            <br>
# MAGIC R² = 0  wenn Modell die Daten "durchschnittlich" beschreibt   <br>
# MAGIC R² < 0  wenn Modell die Daten "noch schlechter" beschreibt    <br>
# MAGIC
