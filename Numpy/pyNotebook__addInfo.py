# Databricks notebook source
import numpy as np

## originalData 3 Columns and 5 Rows
origData = np.array([ 
                      [ 1,  2,  3]
                    , [ 4,  5,  6]
                    , [ 7,  8,  9]
                    , [10, 11, 12]
                    , [13, 14, 15]
                    ])            

## new Column4
newCol4 = np.array([16, 17, 18, 19, 20])
# newColT = newCol4.reshape(-1,1)  ## reshape = not necessary

## "add" the 4th Column to originalData
newData = np.column_stack( (origData, newCol4 ) )

## print the Result
print(newData)


# COMMAND ----------

col3 = newData[:,2]   ## --> 3.Spalte
col4 = newData[:,3]

delta = (col4 - col3).reshape(-1,1)
print(delta)
