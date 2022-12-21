import tkinter

# Grid and pack can't used with pack

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("My First GUI Program")
window.config(padx=10, pady=100)  # adds some space

my_label = tkinter.Label()
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_button = tkinter.Button(text="click me!")
my_button.grid(column=1, row=1)

my_new_button = tkinter.Button(text="click me!")
my_new_button.grid(column=2, row=0)

entry = tkinter.Entry()
entry.grid(column=3, row=2)



window.mainloop()
