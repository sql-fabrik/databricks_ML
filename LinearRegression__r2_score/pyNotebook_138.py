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
##df_fromTbl = sqlContext.table("diamonds_alldata")
df_fromTbl = sqlContext.sql("""
                             SELECT *               
                             FROM   diamonds_alldata 
                             WHERE  ID in (10, 34950, 48400, 9310, 14660, 25453, 26108, 26933) ORDER by carat 
                             """)

df_fromTbl.show()
