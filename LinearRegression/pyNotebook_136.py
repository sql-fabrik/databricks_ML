# Databricks notebook source
# MAGIC %md
# MAGIC "quadrierter" Abstand ...

# COMMAND ----------

# MAGIC %matplotlib inline
# MAGIC %config InlInlineBackend.figure_formats = ['png']
# MAGIC %config  InlineBackend.rc = {"figure.figsize": (5.0, 3.0)}
# MAGIC
# MAGIC import numpy  as np
# MAGIC import pandas as pd
# MAGIC
# MAGIC import matplotlib.pyplot  as plt
# MAGIC import seaborn as sns
# MAGIC

# COMMAND ----------

line_y = 3

xs = [1, 2, 3, 4]
ys = [1, 5, 5, 1]

points = sns.scatterplot(x = xs, y = ys, s = 100)
lineR  = sns.lineplot(x = [0, 5], y = [line_y, line_y], color = "red")

# COMMAND ----------

# MAGIC %md
# MAGIC E = Sigma( y_observation - y_prediction)²

# COMMAND ----------

line_y = 2

xs = [1, 2, 3, 4]
ys = [1, 5, 5, 1]

points = sns.scatterplot(x = xs,  y = ys, s = 100)
lineR  = sns.lineplot(x = [0, 5], y = [line_y, line_y], color = "red")
lineP1 = sns.lineplot(x = [1, 1], y = [1     , line_y], color = "black")
lineP2 = sns.lineplot(x = [2, 2], y = [line_y,      5], color = "black")


# COMMAND ----------

## wenn line_y = 1 dann E = 25
## wenn line_y = 2 dann E = 20
## wenn line_y = 3 dann E = 16
## wenn line_y = 4 dann E = 20
## ...
