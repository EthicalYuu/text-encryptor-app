import tkinter as tk
from Rsa import *
from Fernet import *
from Npad import *
import tkinter.messagebox
from tkinter import filedialog
import tkinter.font as tkFont
import os

user_rsa = Rsa()
user_fernet = MyFernet()
np = Npad()

class DecWin:

    def __init__(self, root):

        def assign_file_path(filepath):
            fpath_lbl["text"] = filepath

        def dec_np_btn_command():
            file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
            if file:
               filepath = os.path.abspath(file.name)
            if filepath:
               assign_file_path(filepath)

        def dec_btn_command():
            if fpath_lbl["text"] == "Filepath":
                tkinter.messagebox.showerror(title="No chosen file", message="Choose a file to encrypt")
            elif not key_entry.get():
                tkinter.messagebox.showerror(title="No entered key", message="Enter a key first")
            elif len(key_entry.get()) != 44:
                tkinter.messagebox.showerror(title="Key Error", message="Something's wrong with the length of your key")
            else:
                chosen_file = open(fpath_lbl["text"], "rb")
                key = key_entry.get()
                content = chosen_file.read()
                content_enc = user_fernet.dec_using_fernet(content, Fernet(key))
                tkinter.messagebox.showinfo(title='Choose a file', message='Create a file to write to')
                new_file = filedialog.asksaveasfile(title="Save file", defaultextension=".txt",
                                                    filetypes=(("Text files", "*.txt"),))
                tkinter.messagebox.showinfo(title='Success', message='Decryption Complete')
                if new_file:
                    new_file.write(str(content_enc))
                    new_file.close()

        def r_from_btn_cmd():
            file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
            if file:
                filepath = os.path.abspath(file.name)
            if filepath:
                f = open(filepath, 'r')
                key = f.read()
                key_entry.delete(0, tk.END)
                key_entry.insert(0, key)


        #setting title
        root.title("Message Decryption")
        #setting window size
        width=672
        height=356
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        dec_np_btn=tk.Button(root)
        dec_np_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=11)
        dec_np_btn["font"] = ft
        dec_np_btn["fg"] = "#000000"
        dec_np_btn["justify"] = "center"
        dec_np_btn["text"] = "Decrypt Notepad File"
        dec_np_btn["relief"] = "ridge"
        dec_np_btn.place(x=50,y=230,width=158,height=45)
        dec_np_btn["command"] = dec_np_btn_command

        read_from_btn=tk.Button(root)
        read_from_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=11)
        read_from_btn["font"] = ft
        read_from_btn["fg"] = "#000000"
        read_from_btn["justify"] = "center"
        read_from_btn["text"] = "Read key from .txt file"
        read_from_btn["relief"] = "ridge"
        read_from_btn.place(x=470,y=230,width=158,height=45)
        read_from_btn["command"] = r_from_btn_cmd

        key_lbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        key_lbl["font"] = ft
        key_lbl["fg"] = "#333333"
        key_lbl["justify"] = "center"
        key_lbl["text"] = "Key"
        key_lbl.place(x=60,y=60,width=110,height=47)

        fpath_lbl=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        fpath_lbl["font"] = ft
        fpath_lbl["fg"] = "#333333"
        fpath_lbl["justify"] = "center"
        fpath_lbl["text"] = "Filepath"
        fpath_lbl.place(x=50,y=280,width=328,height=30)

        dec_btn=tk.Button(root)
        dec_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=11)
        dec_btn["font"] = ft
        dec_btn["fg"] = "#000000"
        dec_btn["justify"] = "center"
        dec_btn["text"] = "Decrypt"
        dec_btn["relief"] = "ridge"
        dec_btn.place(x=220,y=230,width=87,height=45)
        dec_btn["command"] = dec_btn_command

        key_entry=tk.Entry(root)
        key_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=11)
        key_entry["font"] = ft
        key_entry["fg"] = "#333333"
        key_entry["justify"] = "center"
        key_entry["text"] = "Enter the key"
        key_entry.place(x=170,y=60,width=421,height=47)


if __name__ == "__main__":
    root = tk.Tk()
    app = DecWin(root)
    root.mainloop()
