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

## check multi-feature correlation

sp = sns.scatterplot(x="carat", y="x", data=df_sData.sample(50000))
##sp = sns.scatterplot(x="carat", y="x", data=df_sData.sample(50000))
##sp = sns.scatterplot(x="carat", y="y", data=df_sData.sample(50000))
##sp = sns.scatterplot(x="carat", y="z", data=df_sData.sample(50000))


# COMMAND ----------

# DBTITLE 1,sql - count 0
# MAGIC %sql
# MAGIC -- count "NULL"  and  "0"  values
# MAGIC -- --> Table: default.diamonds_alldata
# MAGIC SELECT 'x_size__0'  as info
# MAGIC      , count(*)     as cnt
# MAGIC FROM   default.diamonds_alldata
# MAGIC WHERE  x_size = 0  
# MAGIC UNION
# MAGIC SELECT 'y_size__0'  as info
# MAGIC      , count(*)     as cnt
# MAGIC FROM   default.diamonds_alldata
# MAGIC WHERE  y_size = 0  
# MAGIC UNION
# MAGIC SELECT 'z_size__0'  as info
# MAGIC      , count(*)     as cnt
# MAGIC FROM   default.diamonds_alldata
# MAGIC WHERE  z_size = 0  
# MAGIC UNION
# MAGIC SELECT '_size__0'  as info
# MAGIC      , count(*)     as cnt
# MAGIC FROM   default.diamonds_alldata
# MAGIC WHERE  x_size = 0
# MAGIC   and  y_size = 0
# MAGIC   and  z_size = 0  
# MAGIC
# MAGIC  --  WHERE  x_size is NULL  
# MAGIC  ---- 
