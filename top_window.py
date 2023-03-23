import customtkinter as ctk
from utils import decrypt_password
import csv
from tkinter import messagebox


class TopLevelWindow(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.geometry('500x200')
        self.title('DisplayPasswords')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # finding password by platform name
        text = 'Password for:'
        self.to_what_label = ctk.CTkLabel(self, text=text)
        self.to_what_label.grid(column=0, row=0, padx=20, pady=10, sticky='w')

        self.to_what_textbox = ctk.CTkTextbox(self, height=30)
        self.to_what_textbox.grid(column=1, row=0, padx=20, pady=10, sticky='nsew')

    @staticmethod
    def load_from_csv():
        rows = []
        with open('passwords.csv', 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        return rows

    def validate_password_for_input(self):
        password_for = self.to_what_textbox.get('0.0', 'end')
        if password_for.strip() == '':
            messagebox.showerror('error', '"Password for:" cannot be empty')
        else:
            passwords = self.load_from_csv()
            for password in passwords:
                if password_for.strip() != password[0]:
                    messagebox.showerror('error', '"There is no password for that platform"')


if __name__ == '__main__':
    pass
