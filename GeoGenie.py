import tkinter as tk
import requests, json
from tkinter import *

# Submit, get IP and display output in text box to user
def submit():
    ipEnt = ent.get()

    r = requests.get('http://ip-api.com/json/' + ipEnt)

    city = r.json()['city'] + " " + r.json()['regionName'] + " " + r.json()['zip'] + " " + r.json()['country']

    output = tk.Text(root, borderwidth=0, width=50, height=10)
    output.insert(1.0, city)
    output.pack(pady=(5, 5))
    

# Setup root window
root = tk.Tk()
root.title("Geo Genie by Joe B.")
root.geometry("400x200+0+0")
root.resizable(False, False)

# Entry box
ent = tk.Entry(root, borderwidth=0)
ent.pack(pady=(5, 5))

# Submit button
subbtn = tk.Button(root, text="Submit", command=submit, borderwidth=1)
subbtn.pack(pady=(5, 5))

root.mainloop()
