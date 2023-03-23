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

        # password
        self.password_label = ctk.CTkLabel(self, text='Password:')
        self.password_label.grid(column=0, row=0, padx=20, pady=10, sticky='w')

        self.password_textbox = ctk.CTkTextbox(self, height=30)
        self.password_textbox.grid(column=1, row=0, padx=20, pady=10, sticky='nsew', columnspan=2)

        # password for what
        self.to_what_label = ctk.CTkLabel(self, text='Password for:')
        self.to_what_label.grid(column=0, row=1, padx=20, pady=10, sticky='w')

        self.to_what_textbox = ctk.CTkTextbox(self, height=30)
        self.to_what_textbox.grid(column=1, row=1, padx=20, pady=10, sticky='nsew')

        # find password
        self.find_password_button = ctk.CTkButton(self, text='FindPassword', command=self.display_password)
        self.find_password_button.grid(column=0, row=2, padx=20, pady=10, sticky='w')

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
            self.password_textbox.delete('0.0', 'end')
            return False
        else:
            return True

    def display_password(self):
        if self.validate_password_for_input():
            rows = self.load_from_csv()
            password_for = self.to_what_textbox.get('0.0', 'end')
            for row in rows:
                if password_for.strip() == row[0]:
                    enc_password = decrypt_password(row[1])
                    self.password_textbox.delete('0.0', 'end')
                    self.password_textbox.insert('0.0', text=enc_password)


if __name__ == '__main__':
    pass
