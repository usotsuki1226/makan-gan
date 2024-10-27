import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x400')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()

cuisines = ["American", "Italian", "Asian", "Mexican"]
skibidi = []

def print_selection():
    skibidi.clear()
    if var1.get() != 0:
        skibidi.append(cuisines[0])  # American
    if var2.get() != 0:
        skibidi.append(cuisines[1])  # Italian
    if var3.get() != 0:
        skibidi.append(cuisines[2])  # Asian
    if var4.get() != 0:
        skibidi.append(cuisines[3])  # Mexican
    l.config(text=f'Selected: {skibidi}')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

c1 = tk.Checkbutton(window, text='American', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='Italian', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Asian', variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='Mexican', variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()

button = tk.Button(window, text='Show Selection', command=print_selection)
button.pack(pady=10)

window.mainloop()
