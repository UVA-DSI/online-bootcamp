#import dependencies
import pandas as pd
import matplotlib
#import data and save to variable
df = pd.read_csv('andre.csv')
#clean data
df = df[df.Year > 1976]
df = df[df.Year < 1994]
#make visualization
df.hist("H", bins=100)
matplotlib.pyplot.show()