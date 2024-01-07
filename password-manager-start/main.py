import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for l in range(nr_letters) ]
    password_list += [random.choice(symbols) for l in range(nr_symbols) ]
    password_list += [random.choice(numbers) for l in range(nr_numbers) ]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": username,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields!")
    else:
        try:
            with open("data.json","r") as file:
                # Reading the old data
                data = json.load(file)
                # Updating the old data
                data.update(new_data)
        except FileNotFoundError:
            pass
        finally:
            with open("data.json","w") as file:
                # Saving the updated data
                json.dump(new_data, file, indent=4)
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found")
    else:
        if website not in data:
            messagebox.showerror(title="Oops", message=f"No details for the {website} found")
        else:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)

logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry()
website_entry.grid(column=1,row=1,sticky="EW")
website_entry.focus()

username_entry = Entry()
username_entry.insert(0, "dummy@test.com")
username_entry.grid(column=1,row=2,columnspan=2,sticky="EW")

password_entry = Entry()
password_entry.grid(column=1,row=3,sticky="EW")


search_button = Button(text="Search",command=find_password)
search_button.grid(column=2,row=1,sticky="EW")

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3,sticky="EW")

add_button = Button(text="Add",width=36, command=save_password)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")


window.mainloop()