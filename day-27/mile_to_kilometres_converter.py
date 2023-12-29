import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometres Converter")
window.minsize(width=400,height=400)
window.config(padx=50,pady=50)

def button_clicked():
    miles = float(input.get())
    kilometres = round(1.60934 * miles, 2)

    kilometres_value.config(text=f"{kilometres}")


input = tkinter.Entry(width=20)
input.grid(column=1,row=0)


kilometres_value = tkinter.Label(text=0,font=("Arial",15, "normal"))
kilometres_value.grid(column=1, row=1)
kilometres_value.config(pady=20,padx=20)

miles_label = tkinter.Label(text="Miles", font=("Arial",15, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(pady=20,padx=20)

kilometres_label = tkinter.Label(text="Kilometres", font=("Arial",15, "normal"))
kilometres_label.grid(column=2, row=1)
kilometres_label.config(pady=20,padx=20)


is_equal_to = tkinter.Label(text="is equal to", font=("Arial",15, "normal"))
is_equal_to.config(pady=20,padx=20)
is_equal_to.grid(column=0, row=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
# button.config(pady=20,padx=20)
button.grid(column=1, row=2)







window.mainloop()