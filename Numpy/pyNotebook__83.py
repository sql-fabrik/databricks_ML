# Databricks notebook source
import numpy as np

x = np.array( [1, 2, 3, 4, 5, 6, 7, 8, 9] )
print(x + 2)

# COMMAND ----------

print(np.zeros(10))
print(np.ones(10))

# COMMAND ----------

print(np.arange(1, 10, 1))  ## erster Wert bis (nicht includiert) letzter Wert in Schrittweite 1

# COMMAND ----------

## auch als "Vektor"-Operation
xs = np.array([1, 5, 9])
print(xs + np.arange(1, 4, 1))

# COMMAND ----------

## besser lesbar
xs = np.array([1, 5, 9])
xt = np.arange(1, 4, 1)
print(xs)
print(xt)
print(xs + xt)

print(xs <= xt)

# COMMAND ----------

## Array Shape  MUSS  passen  !!
xs = np.array([1, 5, 9])
xt = np.arange(1, 5, 1)  ## !! hier ist ein Wert zu viel !
print(xs)
print(xt)
#print(xs + xt)

# COMMAND ----------

## Array list-slizing
xs = np.array([1, 5, 9])
xt = np.arange(1, 5, 1)[:3]   ## "händische Anpassung"
print(xs)
print(xt)
print(xs + xt)
