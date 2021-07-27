import tkinter as tk
import requests, json
from tkinter import *

# Submit, get IP and display output in text box to user
def submit():
    ipEnt = ent.get()

    r = requests.get('http://ip-api.com/json/' + ipEnt)

    city = r.json()['city'] + " " + r.json()['regionName'] + " " + r.json()['zip'] + " " + r.json()['country'] + " " + r.json()['org'] + " " + r.json()['isp']

    output = tk.Text(root, borderwidth=0, width=50, height=10, background="#000000", foreground="#ff0000", highlightthickness=0)
    output.insert(1.0, city)
    output.pack(pady=(5,5))
    

# Setup root window
root = tk.Tk()
root.title("Geo Genie")
root.geometry("240x200+0+0")
root.resizable(False, False)
root.config(background="#000000")

# Entry box
ent = tk.Entry(root, borderwidth=0, relief="raised", background="#000000", foreground="#ff0000", highlightthickness=1, highlightbackground="#ff0000")
ent.pack()

# Submit button
subbtn = tk.Button(root, text="Submit", command=submit, borderwidth=1, relief="flat", background="#000000", foreground="#ff0000", activebackground="#ff0000", activeforeground="#000000", highlightthickness=1, highlightbackground="#ff0000")
subbtn.pack(pady=(5,5))

root.mainloop()
