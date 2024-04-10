# Databricks notebook source
# MAGIC %md
# MAGIC ##Mehrdimensionale Arrays

# COMMAND ----------

import numpy as np

## Matrix
xs = np.array([ [1, 2, 3, 4, 5]   ## Einrücken ...
              , [1, 2, 3, 4, 5] 
              , [4, 5, 6, 7, 8] 
              ])
print(xs)

# COMMAND ----------

print(xs.shape)   ##-  zeigt dann "zeilen" & "spalten"

# COMMAND ----------

## vs "Tuple"
xt = np.array( [1, 2, 3, 4, 5] )
print(xt.shape)  

# COMMAND ----------

## zugreifen auf "Teile" der Matrix
xs = np.array([ [1, 2, 3, 4, 5]   ## Einrücken ...
              , [1, 2, 3, 4, 5] 
              , [4, 5, 6, 7, 8] 
              ])
print(xs[2])  ## --> zeigt 3.Zeile (zaehlung beginnt bei 0)

# COMMAND ----------

print(xs[:,1])  ## --> zeigt 2.Spalte

# COMMAND ----------

print(xs[2,4])
print(xs[2, 2:5])

# COMMAND ----------

## update in der Matrix
xs[0, 0] = 11
xs[:, 3] = 15
xs[:, 2] = np.array([101, 102, 103])

print(xs)
