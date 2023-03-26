import csv
from tkinter import messagebox
import customtkinter as ctk
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
from utils import encrypt_password
import pyperclip
from top_window import TopLevelWindow


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        self.geometry('600x270')
        self.title('PasswordGenerator')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # password
        self.password_label = ctk.CTkLabel(self, text='Password:')
        self.password_label.grid(column=0, row=0, padx=20, pady=10, sticky='w')

        self.password_textbox = ctk.CTkTextbox(self, height=30)
        self.password_textbox.grid(column=1, row=0, padx=20, pady=10, sticky='nsew', columnspan=2)

        # password for what
        self.to_what_label = ctk.CTkLabel(self, text='Password for:')
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
        self.generate_password_button.grid(column=0, row=3, padx=20, pady=10, sticky='nsew')

        # copy to clipboard
        self.copy_to_clipboard_button = ctk.CTkButton(self, text='CopyPassword', command=self.copy_to_clipboard)
        self.copy_to_clipboard_button.grid(column=1, row=3, padx=20, pady=10, sticky='nsew')

        # save to json
        self.save_to_jason_button = ctk.CTkButton(self, text='SavePassword', command=self.save_to_csv)
        self.save_to_jason_button.grid(column=1, row=4, padx=20, pady=10, sticky='nsew')

        # display all_passwords
        self.display_passwords_window = ctk.CTkButton(
            self,
            text='FindPassword',
            command=self.open_toplevel_window
            )
        self.display_passwords_window.grid(column=0, row=4, padx=20, pady=10, sticky='nsew')
        self.toplevel_window = None

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

    def save_to_csv(self):
        if self.validate_input():
            password_for, enc_password = self.validate_input()
            path = 'passwords.csv'
            with open(path, 'a', newline='') as file:
                row = (password_for, enc_password)
                writer = csv.writer(file)
                writer.writerow(row)
                self.to_what_textbox.delete('0.0', 'end')
                self.password_textbox.delete('0.0', 'end')
                self.password_length_textbox.delete('0.0', 'end')

    def validate_input(self):
        password = self.password_textbox.get('0.0', 'end')
        password_for = self.to_what_textbox.get('0.0', 'end')[:-1].lower()
        if password.strip() == '':
            messagebox.showerror('error', '"Generate password first"')
            return False
        if password_for.strip() == '':
            messagebox.showerror('error', '"Password for:" cannot be empty')
            return False
        enc_password = encrypt_password(password).decode()
        return password_for, enc_password

    def copy_to_clipboard(self):
        password = self.password_textbox.get('0.0', 'end')
        if password.strip() == '':
            pass
        else:
            pyperclip.copy(password.strip())

    def open_toplevel_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow()
        else:
            self.toplevel_window.focus()


if __name__ == '__main__':
    app = App()
    app.mainloop()
