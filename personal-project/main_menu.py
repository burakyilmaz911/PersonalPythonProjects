from tkinter import *


class MainMenu:
    def __int__(self):
        self.window = Tk()
        self.window.title("Weather App")

        self.canvas = Canvas(width=800, height=800)

        self.start_button = Button()
        self.quit_button = Button()

        self.welcome_text = Label(text="Weather App")

        self.main_menu_image = PhotoImage(file="Images/weather_image_mainmenu.png")
        self.canvas.create_image(400, 400, image=self.main_menu_image)

        self.canvas.grid(row=1, column=0, columnspan=2)
        self.start_button.grid(row=2, column=0)
        self.quit_button.grid(row=2, column=1)
        self.welcome_text.grid(row=0, column=0, columnspan=2)
