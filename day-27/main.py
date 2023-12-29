import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100, pady=200)

# Label
label = tkinter.Label(text="I am a Label",font=("Arial",24, "bold"))
label["text"] = "New Text"
label.config(text="New Text")
# label.place(x=100,y=200)
label.grid(column=0, row=0)
window.config(padx=50, pady=50)

# Button
def button_clicked():
    label.config(text=entry.get())


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry

entry = tkinter.Entry(width=10)
# entry.pack()
entry.grid(column=3, row=2)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)




window.mainloop()
