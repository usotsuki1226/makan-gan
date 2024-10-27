import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x400')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
x = []
y = [1, 2, 3, 4]

def update_label():
    l.config(text=f'Current x: {x}')

def penis():
    if var1.get() != 0:
        if 1 not in x:
            x.append(1)
    else:
        if 1 in x:
            x.remove(1)

    if var2.get() != 0:
        if 2 not in x:
            x.append(2)
    else:
        if 2 in x:
            x.remove(2)

    update_label()

def hehe():
    l.config(text=f'{set(x)&set(y)}')

c1 = tk.Checkbutton(window, 
                    text='gaga', 
                    variable=var1, 
                    onvalue=True, 
                    offvalue=False, 
                    command=penis)
c1.pack()

c2 = tk.Checkbutton(window, text='daga', 
                    variable=var2, 
                    onvalue=True, 
                    offvalue=False, 
                    command=penis)
c2.pack()

button = tk.Button(window, text='Press Me', command=hehe)
button.pack(pady=10)

window.mainloop()
