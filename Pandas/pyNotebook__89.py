# Databricks notebook source
import pandas as pd

df = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/teilnehmer-semicolon.csv").  ## read_csv --> dataFrame

df.head()  ## die "ersten" Zeilen

# COMMAND ----------

##  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html


# COMMAND ----------

df = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/teilnehmer-semicolon.csv", sep=";")  ## read_csv --> dataFrame

df.head()  ## die "ersten" Zeilen

# COMMAND ----------

df = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/teilnehmer2.tsv", sep="\t" )  ## tabulator separated

df.head()  ## die "ersten" Zeilen
