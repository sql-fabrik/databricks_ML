# Databricks notebook source
## Exkurs: Daten plotten
%matplotlib inline  ##-- zeigt das Chart "im Resultbereich des Notebooks"

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [6, 7, 8])
plt.show()


# COMMAND ----------

import numpy as np
xs = np.arange(-3, 3, 0.1)
ys = xs ** 3 - xs ** 2 + 7

plt.plot(xs, ys)
plt.show()

# COMMAND ----------

plt.scatter(xs, ys)
plt.show()
