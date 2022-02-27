from Rsa import *
from Fernet import *
from Npad import *
import tkinter as tk
import tkinter.font as tkFont
from Main_page import enc_send_command, dec_rec_command

user_rsa = Rsa()
user_fernet = MyFernet()
np = Npad()

class home_pg:

    def __init__(self, root):
        width = 672
        height = 356
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        enc_send_btn = tk.Button(root)
        enc_send_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=13)
        enc_send_btn["font"] = ft
        enc_send_btn["justify"] = "center"
        enc_send_btn["text"] = "Encrypt / Sender"
        enc_send_btn["relief"] = "ridge"
        enc_send_btn.place(x=261, y=90, width=150, height=66)
        enc_send_btn["command"] = enc_send_command

        GButton_570 = tk.Button(root)
        GButton_570["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=13)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Decrypt / Reciever"
        GButton_570["relief"] = "ridge"
        GButton_570.place(x=261, y=180, width=150, height=66)
        GButton_570["command"] = dec_rec_command


if __name__ == "__main__":
    root = tk.Tk()
    app = home_pg(root)
    root.mainloop()