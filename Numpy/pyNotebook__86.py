# Databricks notebook source
# MAGIC %md
# MAGIC Shape and ReShape 

# COMMAND ----------

import numpy as np

xs = np.array([ [1, 2, 3, 4, 5]   ## Einrücken ...
              , [1, 2, 3, 4, 5] 
              , [4, 5, 6, 7, 8] 
              ])
print(xs)

# COMMAND ----------

print(xs.reshape(-1))  ## --> alle Werte "in einer Zeile" / -1 als WildCard

# COMMAND ----------

print(xs.reshape(5, 3))
print("----")
print(xs.reshape(5, -1))

# COMMAND ----------

print(xs.reshape(-1, 1))  ## alle Werte "in einer Spalte" / jeder Eintrag ist in "einer Zeile"

# COMMAND ----------


