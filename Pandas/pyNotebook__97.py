# Databricks notebook source
import pandas as pd

df = pd.read_csv("https://itschulungen.blob.core.windows.net/databricks-ml/GlobalLandTemperaturesByMajorCity.csv.bz2")
df.head()

# COMMAND ----------

## Aufgabe 1:
## wieviele Datensätze aus Spanien "Spain"

len( df[df["Country"] == "Spain"] )
df[df["Country"] == "Spain"].count()
##--  result 3239 rows

# COMMAND ----------

## Aufgabe 2:
## erstelle Variable df_germany
## ?? niedrigste Temperatur & höchste Temperatur ( Column: "AverageTemperature")
df_germany = df[df["Country"] == "Germany"]
df_germany.head(3)

# COMMAND ----------

## Aufgabe 3:
## welches Land (Germany | France) hatte die höhere MaximalTemperatur ?

## df[df["Country"] == "France"].nlargest(3, "AverageTemperature")  ## ok
df[ (df["Country"] == "France") | (df["Country"] == "Germany")].nlargest(5, "AverageTemperature")


# COMMAND ----------

## Aufgabe 4:
## wie oft hab es in Berlin "ungemütliches Wetter" ( Temp. < -9 C° | Temp. > 22 C°) ?
## wenn möglich nur eine Zeile Code

# COMMAND ----------

## Aufgabe 5:
## was ist die tiefste Temperatur, die in "China"
## nur eine Zeile Code 
