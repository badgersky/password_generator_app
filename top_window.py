import customtkinter as ctk
from utils import decrypt_password
import csv


class TopLevelWindow(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.geometry('400x200')
        self.title('DisplayPasswords')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)


if __name__ == '__main__':
    pass
