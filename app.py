import tkinter
import customtkinter
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class App:

    def __init__(self):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('green')

        self.root = customtkinter.CTk()
        self.root.geometry('500x500')

        self.generate_password_button = customtkinter.CTkButton(
            master=self.root,
            text='GeneratePassword',
            command=self.display_password
            )
        self.generate_password_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def generate_password(self):
        special_characters = '!@#$%^&*()_-<>?'
        all_characters = ascii_lowercase + ascii_uppercase + digits + special_characters
        return ''.join(choice(all_characters) for _ in range(15))

    def display_password(self):
        password = self.generate_password()
        print(password)

    def run_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run_app()
