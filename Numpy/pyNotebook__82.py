# Databricks notebook source
# MAGIC %md
# MAGIC ##Numpy 
# MAGIC * udemy-Kurs <br>
# MAGIC https://www.udemy.com/course/python-datascience-bootcamp/learn/lecture/21235108#overview
# MAGIC

# COMMAND ----------

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [i ** 2 for i in x]  ##-- for i - loop
print(y) 

# COMMAND ----------

# MAGIC %matplotlib inline
# MAGIC import matplotlib.pyplot as plt
# MAGIC
# MAGIC plt.plot(x, y)
# MAGIC plt.show()

# COMMAND ----------


##-- "list-comprehension" ist nicht sehr performant 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [i ** 2 for i in x]  ##-- for i - loop
print(y) 

# COMMAND ----------

## Python Numpy "Berechnungen"
import numpy as np

x = np.array( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] )
print(x)
print( type(x) )  ##-- zeigt den "Datentyp" an


# COMMAND ----------

y = x - 2
print(y)

# COMMAND ----------

y = x ** 2
print(y)
