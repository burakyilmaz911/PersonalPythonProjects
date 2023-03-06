from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=200, height=100)

# # Label
#
# label = Label(text="Label", font=("Arial", 24, "bold"))
# label.grid(row=0, column=0)
#
#
# def button_clicked():
#     user_input = input.get()
#     label.config(text=user_input)
#
#
# button = Button(text="click me", command=button_clicked)
# button.grid(row=1, column=1)
#
# button2 = Button(text="I am button 2")
# button2.grid(row=0, column=2)
#
# input = Entry(width=10)
# input.grid(row=2, column=3)
#

def calculate_clicked():
    km_converted = float(entry.get()) * 1.6
    kilometers.config(text=km_converted)

entry = Entry()
entry.grid(row=0, column=1)

entry_text = Label(text="Miles")
entry_text.grid(row=0, column=2)

equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

kilometers = Label(text="0")
kilometers.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(row=2, column=1)




window.mainloop()
