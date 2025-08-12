import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(20, 16), dpi=(100))
ax = fig.add_subplot(111)
root = tk.Tk()
root.title('RPW through time')


df = pd.read_csv('Dataset.csv')
df = df.drop(['Won', 'Tied', 'Draw', 'Balls', 'Column1'], axis=1)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def generate_and_update():
    get_entry_text()
    trigger_update()



def update_graph(Year, Average):
    ax.clear()  # Clear existing plot
    ax.plot(Year, Average)  # Plot new data
    canvas.draw()  # Redraw the canvas

def get_entry_text():
    global start_year
    global end_year
    start_year = start_year_get.get()
    end_year = end_year_get.get()
    print(f'{start_year}-{end_year}')

def trigger_update():
    Year = df.iloc[start_year:end_year, 5]
    Average = df.iloc[start_year:end_year, 3]
    update_graph(Year, Average)

update_button = tk.Button(master=root, text="Update Graph", command=generate_and_update)
update_button.pack(side=tk.BOTTOM)

start_year_get = tk.Entry(root, width=30)
start_year_get.pack(pady=20, side=tk.TOP)

end_year_get = tk.Entry(root, width=20)
end_year_get.pack(pady=20, side=tk.TOP)

root.mainloop()