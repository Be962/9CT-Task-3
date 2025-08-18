import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset.csv')
df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)
year = df.iloc[:,5]
average = df.iloc[:, 3]

def setup():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('Dataset.csv')
    df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)
    year = df.iloc[:,5]
    average = df.iloc[:, 3]
    return year, average

def show_plot(year, average):
    plt.title('Runs Per Wicket (RPW) through time')
    plt.xlabel('Years')
    plt.ylabel('Average')
    plt.plot(year, average)
    plt.show()

def filter():
    start_years = 0
    end_years = 3000
    while start_years < 1950 or start_years > 2024:
        start_years = int(input('What year would you like to start as? (1950-2025) '))
    while ((end_years < 1950 or end_years > 2025) or end_years <= start_years) or end_years == 0:
        end_years = int(input('What year would you like to end as? (1950-2025) '))
    end_years = end_years - 1945
    start_years = start_years - 1946
    year = df.iloc[start_years:end_years, 5]
    average = df.iloc[start_years:end_years, 3]
    show_plot(year, average)

def show_other_stats():
    stddf = df['Ave'].std()
    stddf = stddf.round(4)
    overall_average = df['Runs'].sum() / df['Wkts'].sum()
    overall_average = overall_average.round(4)
    return stddf, overall_average

# print(show_other_stats)