#UI WIP

import tkinter as tk
from tkinter import *
r = tk.Tk()
r.title('Test GUI')
button = tk.Button(r, text = "STOP", width = 100, height=40,command = r.destroy)
button.pack()


r.mainloop()