# Databricks notebook source
# MAGIC %md
# MAGIC Numpy Operationen

# COMMAND ----------

import numpy as np

xs = np.array([ [1, 2, 3, 4, 5]   ## Einrücken ...
              , [1, 2, 3, 4, 5] 
              , [4, 5, 6, 7, 8] 
              ])
print(xs.min())
print(xs.max())
print(xs.mean())  ##-- = SQL.AVG()
## zeigt die Werte für die "gesamte" Matrix

# COMMAND ----------

## -->  xs.min?  ## zeigt die Hilfe leider nur bei Jupyter-Notebooks

# COMMAND ----------

print(xs.max(axis=0))
print(xs.max(axis=1))

# COMMAND ----------

xt = np.array([1, 2, 3, 4, 5, 3, 2, 1])
print(xt.argmax())  ## --> zeigt die Position des "Max"-Wertes

# COMMAND ----------

## weiter im Folder "Pandas"
## -------------------------
