import tkinter
import customtkinter


class App:

    def __init__(self):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('green')

        self.root = customtkinter.CTk()
        self.root.geometry('500x500')

        self.generate_password_button = customtkinter.CTkButton(
            master=self.root,
            text='GeneratePassword',
            command=self.generate_password
            )
        self.generate_password_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def generate_password(self):
        print('password')

    def run_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run_app()
