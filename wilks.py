from tkinter import *


root = Tk()
root.geometry("600x200")
root.title("Wilks Calculator")
root.grid_columnconfigure((0,1), weight=1)


Entry3 = Entry(root)
weight = Entry(root)
total = Entry(root)

def selected():
    if clicked.get() == "Male":
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863E-06
        f = -1.291E-08

    else:
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 4.731582E-05
        f = -9.054E-08

    ans = (float(total.get()) * 500 //(a + b * float(weight.get()) + c * float(weight.get())**2 + d * float(weight.get())**3 + e * float(weight.get())**4 + f * float(weight.get())**5))
    ans1 = Label(root, text=ans)
    ans1.grid(row=6, column=1)

Label3 = Label(root, text="Gender")
Label4 = Label(root, text="Bodyweight KG")
Label5 = Label(root, text="Lifted weight")
Label6 = Label(root, text="Wilks: ")



Label3.grid(row=3, column=0)
Label4.grid(row=4, column=0)
weight.grid(row=4, column=1)
Label5.grid(row=5, column=0)
total.grid(row=5, column=1)
Label6.grid(row=6, column=0)

options = [
    "Male",
    "Female",
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
#drop = ttk.Combobox(root, value=options)
#drop.current(0)
#drop.bind("<<ComboboxSelected>>", comboclick)
drop.grid(row=3, column=1)


button = Button(root, text="Calculate", command=selected)
button.grid(row=8, column=1)

root.mainloop()