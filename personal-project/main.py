from tkinter import *
import requests

BUTTON_FONT = ("Arial", 20)
WELCOME_TEXT_FONT = ("Arial", 25, "bold")
BG_COLOR ="CadetBlue1"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
WEATHER_API_KEY = "4cab9d0c1ef82b6abd55a5de96e416a3"
MY_LAT = 42.314938
MY_LONG = -83.036362

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API_KEY
}

def start_button():
    canvas.grid_remove()
    start_button.grid_remove()
    welcome_text.grid_remove()

    shirt_image = PhotoImage(file="Images/shirt.png")
    pants_image = PhotoImage(file="Images/pants.png")
    shoes_image = PhotoImage(file="Images/shoes.png")

    weather_info_label = Label(
        text="This text will be for the info on the weather currently",
        font=WELCOME_TEXT_FONT
    )

    quit_button.config(width=2, height=1)

    shirt_button = Button(
        width=8,
        height=4,
        padx=5,
        pady=5,
        text="Start",
        font=BUTTON_FONT,
        highlightthickness=0,
        image=shirt_image
    )

    pants_button = Button(
        width=8,
        height=4,
        padx=5,
        pady=5,
        text="Start",
        font=BUTTON_FONT,
        highlightthickness=0,
        image=pants_image
    )

    shoes_button = Button(
        width=8,
        height=4,
        padx=5,
        pady=5,
        text="Start",
        font=BUTTON_FONT,
        highlightthickness=0,
        image=shoes_image
    )

    weather_info_label.grid(row=0, column=0, columnspan=3)
    shirt_button.grid(row=1, column=1)
    pants_button.grid(row=2, column=1)
    shoes_button.grid(row=3, column=1)
    quit_button.grid(row=4, column=2)


    # data = requests.get(url=WEATHER_API_URL, params=params)
    # weather_data_json = data.json()
    #
    # print(weather_data_json)

def quit_button():
    window.quit()


window = Tk()
window.title("Weather App")
window.config(bg=BG_COLOR)

canvas = Canvas(
    width=500,
    height=500,
    bg=BG_COLOR,
    highlightthickness=0
)

start_button = Button(
    width=10,
    height=2,
    padx=5,
    pady=5,
    text="Start",
    font=BUTTON_FONT,
    highlightthickness=0,
    command=start_button
)
quit_button = Button(
    width=10,
    height=2,
    padx=5,
    pady=5,
    text="Quit",
    font=BUTTON_FONT,
    highlightthickness=0,
    command=quit_button
)

welcome_text = Label(
    text="Weather App",
    font=WELCOME_TEXT_FONT,
    bg=BG_COLOR
)

main_menu_image = PhotoImage(file="Images/weather_image_mainmenu.png")
canvas.create_image(250, 250, image=main_menu_image)

canvas.grid(row=1, column=0, columnspan=2)
start_button.grid(row=2, column=0)
quit_button.grid(row=2, column=1)
welcome_text.grid(row=0, column=0, columnspan=2)

window.mainloop()