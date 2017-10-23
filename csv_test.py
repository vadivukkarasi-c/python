import pandas as pd
import numpy as np
data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
print(data.head())
df=pd.dataframes('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
data.to_csv("C:/Users/Trumatics/Desktop/python/python/samplefile.csv")
df = pd.read_csv('C:/Users/Trumatics/Desktop/python/python/samplefile.csv')
print(df.head())