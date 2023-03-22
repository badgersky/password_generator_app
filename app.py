import tkinter
import customtkinter as ctk
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        self.geometry('450x200')
        self.title('PasswordGenerator')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # password
        self.password_label = ctk.CTkLabel(self, text='Password:')
        self.password_label.grid(column=0, row=0, padx=20, pady=10, sticky='w')

        self.password_textbox = ctk.CTkTextbox(self, height=30)
        self.password_textbox.grid(column=1, row=0, padx=20, pady=10, sticky='nsew')

        # password to what
        self.to_what_label = ctk.CTkLabel(self, text='Password to what?:')
        self.to_what_label.grid(column=0, row=1, padx=20, pady=10, sticky='w')

        self.to_what_textbox = ctk.CTkTextbox(self, height=30)
        self.to_what_textbox.grid(column=1, row=1, padx=20, pady=10, sticky='nsew')

        # password length
        self.password_length_label = ctk.CTkLabel(self, text='Password length:')
        self.password_length_label.grid(column=0, row=2, padx=20, pady=10, sticky='w')

        self.password_length_textbox = ctk.CTkTextbox(self, height=30)
        self.password_length_textbox.grid(column=1, row=2, padx=20, pady=10, sticky='nsew')

        # generate password button
        self.generate_password_button = ctk.CTkButton(self, text='GeneratePassword', command=self.display_password)
        self.generate_password_button.grid(column=0, row=3, padx=20, pady=10, sticky='w')

    @staticmethod
    def generate_password(length):
        max_length = 25
        min_length = 10

        length = min(length, max_length)
        length = max(length, min_length)
        special_characters = '!@#$%^&*()_-<>?'
        all_characters = ascii_lowercase + ascii_uppercase + digits + special_characters
        return ''.join(choice(all_characters) for _ in range(length))

    def display_password(self):
        try:
            length = int(self.password_length_textbox.get('0.0', 'end'))
        except ValueError:
            length = 10
        self.password_textbox.delete('0.0', 'end')
        password = self.generate_password(length)
        self.password_textbox.insert('0.0', f'{password}')

    def run_app(self):
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.run_app()
