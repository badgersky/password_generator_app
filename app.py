import customtkinter as ctk
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        self.geometry('550x220')
        self.title('PasswordGenerator')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # password
        self.password_label = ctk.CTkLabel(self, text='Password:')
        self.password_label.grid(column=0, row=0, padx=20, pady=10, sticky='w')

        self.password_textbox = ctk.CTkTextbox(self, height=30)
        self.password_textbox.grid(column=1, row=0, padx=20, pady=10, sticky='nsew', columnspan=2)

        # password to what
        self.to_what_label = ctk.CTkLabel(self, text='Password to what?:')
        self.to_what_label.grid(column=0, row=1, padx=20, pady=10, sticky='w')

        self.to_what_textbox = ctk.CTkTextbox(self, height=30)
        self.to_what_textbox.grid(column=1, row=1, padx=20, pady=10, sticky='nsew', columnspan=2)

        # password length
        self.password_length_label = ctk.CTkLabel(self, text='Password length:')
        self.password_length_label.grid(column=0, row=2, padx=20, pady=10, sticky='w')

        self.password_length_textbox = ctk.CTkTextbox(self, height=30)
        self.password_length_textbox.grid(column=1, row=2, padx=20, pady=10, sticky='nsew', columnspan=2)

        # generate password button
        self.generate_password_button = ctk.CTkButton(self, text='GeneratePassword', command=self.display_password)
        self.generate_password_button.grid(column=0, row=3, padx=20, pady=10, sticky='w')

        # save to json
        self.save_to_jason_button = ctk.CTkButton(self, text='SavePassword', command=self.save_to_json)
        self.save_to_jason_button.grid(column=2, row=3, padx=20, pady=10, sticky='w')

        # copy to clipboard
        self.copy_to_clipboard_button = ctk.CTkButton(self, text='CopyToClipboard', command=self.copy_to_clipboard)
        self.copy_to_clipboard_button.grid(column=1, row=3, padx=20, pady=10)

    @staticmethod
    def generate_password(length):
        max_length = 40
        min_length = 10

        length = min(length, max_length)
        length = max(length, min_length)
        special_characters = '!@#$%^&*()_-<>?'
        all_characters = ascii_lowercase + ascii_uppercase + digits + special_characters
        password = ''.join(choice(all_characters) for _ in range(length - 4))
        password += choice(ascii_lowercase) + choice(ascii_uppercase) + choice(digits) + choice(special_characters)
        return password

    def display_password(self):
        try:
            length = int(self.password_length_textbox.get('0.0', 'end'))
        except ValueError:
            length = 10
        self.password_textbox.delete('0.0', 'end')
        password = self.generate_password(length)
        self.password_textbox.insert('0.0', f'{password}')

    def save_to_json(self):
        pass

    def copy_to_clipboard(self):
        pass

    def run_app(self):
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.run_app()
