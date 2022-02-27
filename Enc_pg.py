from Rsa import *
from Fernet import *
from Npad import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk, filedialog
import tkinter.font as tkFont
import os

user_rsa = Rsa()
user_fernet = MyFernet()
np = Npad()

class EncWin:

    def __init__(self, root):

        def assign_file_path(filepath):
            fpath_lbl["text"] = filepath

        def enc_btn_command():
            if fpath_lbl["text"] == "Filepath":
                tkinter.messagebox.showerror(title="No chosen file", message="Choose a file to encrypt")
            elif gen_key_lbl["text"] == "Generate a key":
                tkinter.messagebox.showerror(title="No key generated", message="Generate a key first")
            else:
                chosen_file = open(fpath_lbl["text"], "r")
                key = gen_key_lbl["text"]
                content = chosen_file.read()
                content_enc = user_fernet.enc_using_fernet(content, Fernet(key))
                tkinter.messagebox.showinfo(title='Choose a file', message='Create a file to write to')
                new_file = filedialog.asksaveasfile(title="Save file", defaultextension=".txt",
                                                    filetypes=(("Text files", "*.txt"),))
                tkinter.messagebox.showinfo(title='Success', message='Encryption Complete')
                print(new_file)
                if new_file:
                    f = open(new_file.name, "wb")
                    f.write(content_enc)
                    f.close()

        def gen_key_btn_command():
            key = user_fernet.create_fernet_key()
            gen_key_lbl['text'] = key
            tkinter.messagebox.showwarning("",
                                           "Key has been copied to clipboard, make sure to save the key and not share with anyone")
            root.clipboard_clear()
            root.clipboard_append(key)

        def enc_np_btn_command():
            file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
            if file:
                filepath = os.path.abspath(file.name)
            if filepath:
                assign_file_path(filepath)

        root.title("Message Encryption")

        width = 672
        height = 356
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        enc_np_btn = tk.Button(root)
        enc_np_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        enc_np_btn["font"] = ft
        enc_np_btn["fg"] = "#000000"
        enc_np_btn["justify"] = "center"
        enc_np_btn["text"] = "Encrypt Notepad File"
        enc_np_btn["relief"] = "ridge"
        enc_np_btn.place(x=50, y=230, width=158, height=45)
        enc_np_btn["command"] = enc_np_btn_command

        crt_msg_btn = tk.Button(root)
        crt_msg_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        crt_msg_btn["font"] = ft
        crt_msg_btn["fg"] = "#000000"
        crt_msg_btn["justify"] = "center"
        crt_msg_btn["text"] = "Create Message"
        crt_msg_btn["relief"] = "ridge"
        crt_msg_btn.place(x=470, y=230, width=158, height=45)

        gen_key_lbl = tk.Label(root)
        gen_key_lbl["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=11)
        gen_key_lbl["font"] = ft
        gen_key_lbl["fg"] = "#333333"
        gen_key_lbl["justify"] = "center"
        gen_key_lbl["text"] = "Generate a key"
        gen_key_lbl.place(x=170, y=60, width=421, height=47)

        gen_key_btn = tk.Button(root)
        gen_key_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        gen_key_btn["font"] = ft
        gen_key_btn["fg"] = "#000000"
        gen_key_btn["justify"] = "center"
        gen_key_btn["text"] = "Generate Key"
        gen_key_btn["relief"] = "ridge"
        gen_key_btn.place(x=60, y=130, width=150, height=48)
        gen_key_btn["command"] = gen_key_btn_command

        fpath_lbl = tk.Label(root)
        fpath_lbl["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        fpath_lbl["font"] = ft
        fpath_lbl["fg"] = "#333333"
        fpath_lbl["justify"] = "left"
        fpath_lbl["text"] = "Filepath"
        fpath_lbl.place(x=50, y=280, width=328, height=30)

        enc_btn = tk.Button(root)
        enc_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        enc_btn["font"] = ft
        enc_btn["fg"] = "#000000"
        enc_btn["justify"] = "center"
        enc_btn["text"] = "Encrypt"
        enc_btn["relief"] = "ridge"
        enc_btn.place(x=220, y=230, width=87, height=45)
        enc_btn["command"] = enc_btn_command

        GLabel_66 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=11)
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#333333"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "Key"
        GLabel_66.place(x=60, y=60, width=109, height=47)



if __name__ == "__main__":
    root = tk.Tk()
    app = EncWin(root)
    root.mainloop()