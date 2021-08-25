# Password manager with python
from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip

# SETTING UP THE WINDOW
window = Tk()
window.title("Password Manager With Python")
window.config(padx=50, pady=50)

# SETTING UP THE CANVAS
canvas = Canvas(width=200, height=200)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=0, column=1)

# LABEL
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# INPUT
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
email_username_input = Entry(width=35)
email_username_input.insert(0, "test@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)


# GENERATE PASSWORD
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'f', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    gen_password = "".join(password_list)
    password_input.insert(0, gen_password)
    # pyperclip.copy(gen_password)


# GENERATE PASSWORD BUTTON
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)


# SEARCH EMAIL AND PASSWORD FUNCTIONALITY
def search_email_and_password():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    try:
        website = data[website_input.get()]
        website_email = website["email"]
        website_password = website["password"]
        messagebox.showinfo(title=website["email"], message=f"Email: {website_email}\nPassword: {website_password}")
    except KeyError as err_message:
        messagebox.showinfo(title="Error", message=f"No website with name: {err_message} found")


# SAVING PASSWORD TO FILE...
def save_to_file():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {website: {"email": email_username, "password": password}}

    # Validation
    password_length = len(password)
    website_length = len(website)

    if password_length == 0 or website_length == 0:
        messagebox.showinfo(title="Invalid credential", message="Please all fields are required")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ADD BUTTON
add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

# SEARCH BUTTON
search_button = Button(text="Search", command=search_email_and_password)
search_button.grid(row=1, column=2)

window.mainloop()

# Further improvements
# DELETE EMAIL AND PASSWORD
# EDIT EMAIL AND PASSWORD
