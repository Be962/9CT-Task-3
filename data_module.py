import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(20, 16), dpi=(100))
ax = fig.add_subplot(111)
root = tk.Tk()
def sort_data():
    global Average
    global Year
    df = pd.read_csv('Dataset.csv')
    df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)
    Average = df.iloc[int(start_years):int(end_years), 3]
    Year = df.iloc[int(start_years):int(end_years), 5]

def get_years():
    global start_years
    global end_years
    get_start_years = tk.Entry(root, width=40)
    get_start_years.pack(pady=20, padx=20)
    get_end_years = tk.Entry(root, width=40)
    get_end_years.pack(pady=20, padx=20)
    start_years = get_start_years.get()
    end_years = get_end_years.get()

def show_graph():
    plt.title('Runs Per Wicket (RPW) over time')
    plt.xlabel('Years')
    plt.ylabel('RPW')
    plt.plot(Year, Average)
    plt.show()

def tkinter_show_graph():
    root.title('Runs Per Wicket')
    root.geometry('800x450')
    get_start_years = tk.Entry(root, width=40)
    get_start_years.pack(pady=20, padx=20)
    get_end_years = tk.Entry(root, width=40)
    get_end_years.pack(pady=20, padx=20)
    ax.set_title('Runs Per Wicket (RPW) over time')
    ax.set_xlabel('Years')
    ax.set_ylabel('RPW')
    ax.plot(Year, Average)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    years_display = tk.Label(root, text=f'Years: {start_years}-{end_years}')  
    years_display.pack()
    years_display.config(text=f'Years: {start_years}-{end_years}')
    fig.canvas.draw_idle()
    print('drew graph')

while True:
    get_years()
    sort_data()
    tkinter_show_graph()