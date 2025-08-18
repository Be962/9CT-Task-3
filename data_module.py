import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset.csv')
df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)
year = df.iloc[:,5]
average = df.iloc[:, 3]

def show_plot(year, average):
    plt.title('Runs Per Wicket (RPW) through time')
    plt.xlabel('Years')
    plt.ylabel('Average')
    plt.plot(year, average)
    plt.show()

def filter():
    start_years = 0
    end_years = 0
    while start_years < 1901 or start_years > 2025:
        start_years = int(input('What year would you like to start as? (1901-2025)'))
    while end_years < 1901 or end_years > 2025 and end_years < start_years:
        end_years = int(input('What year would you like to end as? '))
    end_years = end_years - 1907
    start_years = start_years - 1901
    year = df.iloc[start_years:end_years, 5]
    average = df.iloc[start_years:end_years, 3]
    show_plot(year, average)

filter()