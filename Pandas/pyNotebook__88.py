# Databricks notebook source
# MAGIC %md
# MAGIC ##Pandas
# MAGIC
# MAGIC Verarbeiten von "strukturierten" Daten

# COMMAND ----------

import pandas as pd

df = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/teilnehmer.txt")  ## read_csv --> dataFrame

df.head()  ## die "ersten" Zeilen

# COMMAND ----------

## df      ## "alle" Zeilen
df
