from data_module import filter, show_plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset.csv')
df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)
year = df.iloc[:,5]
average = df.iloc[:, 3]

while True:
    choice = input('What would you like to choose? \n 1. Show the full data \n 2. Filter then show data \n ')
    if choice == str(1):
        show_plot(year, average)
    if choice == str(2):
        filter()