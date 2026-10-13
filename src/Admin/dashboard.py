import tkinter as tk
from tkinter import ttk 

WIDTH = 600
HEIGHT = 800

window = tk.Tk()
window.title('Manager Dashboard')
window.config(padx=50, pady=10)

header = tk.Label(text='DASHBOARD', font=('Arial', 50)).grid(row=1, column=0)

window.mainloop()

