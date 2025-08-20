# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Setup/prepping the dataset

df = pd.read_csv('Dataset.csv')
df = df.drop(['Won', 'Tied', 'Draw', 'Column1'], axis=1)
year = df.iloc[:,6]
average = df.iloc[:,4]


def setup():        # Put the setup into a function that can be used in main.py, to make it tidier
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('Dataset.csv')
    df = df.drop(['Won', 'Tied', 'Draw', 'Column1'], axis=1)
    year = df.iloc[:,6]
    average = df.iloc[:, 4]
    return year, average

def show_plot(year, average): # Gets year and average input, plots graph using those parameters.
    plt.title('Runs Per Wicket (RPW) through time')
    plt.xlabel('Years')
    plt.ylabel('Average')
    plt.plot(year, average)
    plt.grid() # Adds grid lines
    plt.show()

def filter(): # 
    start_years = 0
    end_years = 3000
    while start_years < 1946 or start_years > 2024:
        start_years = int(input('What year would you like to start as? (1950-2025) '))
    while ((end_years < 1946 or end_years > 2025) or end_years <= start_years) or end_years == 0:
        end_years = int(input('What year would you like to end as? (1950-2025) '))
    end_years = end_years - 1945 # Because the indexing does not have 2025 rows, the input year needs to be converted into the row number
    start_years = start_years - 1946
    year = df.iloc[start_years:end_years, 6]  # Sets the new year and average to use the input years
    average = df.iloc[start_years:end_years, 4]
    show_plot(year, average) # Plots the new year and average

def show_other_stats():
    stddf = df['Ave'].std() # Finds the standard deviation of the 'Ave' column
    stddf = stddf.round(4) # Rounds to 4 for tidiness
    overall_average = df['Runs'].sum() / df['Wkts'].sum() # Overall average is all 'Runs' divided by all 'Wkts'
    overall_average = overall_average.round(4) # Rounds to 4 for tidiness
    overall_rpo = df['Runs'].sum() / df['Balls'].sum() # Runs per ball is all 'Runs' divided by alls 'Balls' 
    overall_rpo = overall_rpo * 6 # Times by 6 to make it runs per over
    overall_rpo = overall_rpo.round(4) # Rounds to 4 for tidiness
    return stddf, overall_average, overall_rpo # Returns to be used in main.py
