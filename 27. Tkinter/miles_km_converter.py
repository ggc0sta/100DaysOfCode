import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Miles to Km Converter")
window.config(pady=20, padx=20)

l_miles = tkinter.Label(text="Miles")
l_miles.grid(column=2, row=0)

l_km = tkinter.Label(text="Km")
l_km.grid(column=2, row=1)

l_equal = tkinter.Label(text="is equal to")
l_equal.grid(column=0, row=1)

l_converted_km = tkinter.Label(text="0")
l_converted_km.grid(column=1, row=1)

entry = tkinter.Entry(width=10)
# entry.insert(END, string="0")
entry.grid(column=1, row=0)


def convert():
    miles = float(entry.get())
    km = round(miles * 1.60934, 1)
    l_converted_km.config(text=f"{km}")
    return


button = tkinter.Button(text="Calculate")
button.config(command=convert)
button.grid(column=1, row=2)

window.mainloop()
