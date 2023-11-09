import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_graph():
    data = table.get_children()
    x_data = [table.item(item, 'values')[0] for item in data]
    y_data = [table.item(item, 'values')[1] for item in data]
    plt.figure(figsize=(5, 4))
    plt.plot(x_data, y_data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Data Plot')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def add_data():
    x_value = x_entry.get()
    y_value = y_entry.get()
    if x_value and y_value:
        table.insert('', 'end', values=(x_value, y_value))
        x_entry.delete(0, 'end')
        y_entry.delete(0, 'end')


root = tk.Tk()
root.title("Data Table and Graph Plotter")

data_frame = tk.Frame(root)
data_frame.pack(pady=10)
x_label = tk.Label(data_frame, text="X Value:")
x_label.grid(row=0, column=0)
x_entry = tk.Entry(data_frame)
x_entry.grid(row=0, column=1)
y_label = tk.Label(data_frame, text="Y Value:")
y_label.grid(row=1, column=0)
y_entry = tk.Entry(data_frame)
y_entry.grid(row=1, column=1)
add_button = tk.Button(data_frame, text="Add Data", command=add_data)
add_button.grid(row=2, column=0, columnspan=2)


table_frame = tk.Frame(root)
table_frame.pack(padx=10)
table = ttk.Treeview(table_frame, columns=("X Value", "Y Value"), show="headings")
table.heading("X Value", text="X Value")
table.heading("Y Value", text="Y Value")
table.pack()

graph_frame = tk.Frame(root)
graph_frame.pack(pady=10)

plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack()

root.mainloop()
