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

        self.textbox = customtkinter.CTkTextbox(self.root, width=200, height=20)
        self.textbox.pack(pady=150, padx=0)

    @staticmethod
    def generate_password():
        special_characters = '!@#$%^&*()_-<>?'
        all_characters = ascii_lowercase + ascii_uppercase + digits + special_characters
        return ''.join(choice(all_characters) for _ in range(15))

    def display_password(self):
        self.textbox.delete('0.0', 'end')
        password = self.generate_password()
        self.textbox.insert('0.0', f'{password}')

    def run_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run_app()
