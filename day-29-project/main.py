from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_information():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        empty_field = messagebox.askretrycancel(title="Oops",
                                                message="One or more message boxes are empty, please try again")
    else:
        data_file = open("data.txt", "a")
        data_file.write(f"Website/Game: {website}\nEmail: {email_username}\nPassword: {password}\n\n")
        data_file.close()

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website/Game")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "theyilmaz2000@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_information)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
