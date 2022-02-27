from Rsa import *
from Fernet import *
from Npad import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import tkinter.font as tkFont
import os

window = tk.Tk()

user_rsa = Rsa()
user_fernet = MyFernet()
np = Npad()

# my_public_key, my_private_key = user_rsa.create_pair_of_keys()
# other_public_key, other_private_key = user_rsa.create_pair_of_keys()

def generate_key():
    key = user_fernet.create_fernet_key()
    generated_key_lbl['text'] = key
    tkinter.messagebox.showwarning("", "Key has been copied to clipboard, make sure to save the key and not share with anyone")
    window.clipboard_clear()
    window.clipboard_append(key)

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file:
        filepath = os.path.abspath(file.name)
    print(filepath)


                                                                             # 1) Create a key to be used in encrypting data
# encrypted_key = user_rsa.encrypt_key(key, other_public_key)                # 2) Encrypt the key using other's PU-
# key = Rsa.decrypt_key(encrypted_key, other_private_key)                    # 3) Send encrypted key over network
# enc = user_fernet.enc_using_fernet(message, key)                             # 4) Other decrypts the encrypted key and gets the key
# np.create_write_notepad('enc', str(enc))                                     # 5) Other decrypts the encrypted key and gets the key

main_frame = tk.Frame()
main_frame.pack(padx=30, pady=20)

frame1 = tk.Frame(master=main_frame)
frame1.pack(pady=(0, 10))

key_lbl = tk.Label(master=frame1, text='key',
                   width=10, height=2, borderwidth=3,
                   relief='groove', font=('Arial', 13))
key_lbl.pack(side=tk.LEFT)

generated_key_lbl = tk.Label(master=frame1, text='Generate a key',
                            width=50, height=3, font=('Arial', 13))
generated_key_lbl.pack(side=tk.LEFT)

frame2 = tk.Frame(master=main_frame)
frame2.pack(side=tk.LEFT)

generate_btn = tk.Button(master= frame2, text='Generate Key',
                         command= generate_key, width=12, height=2,
                         font=('Arial', 10))
generate_btn.pack(pady=(0, 10))

frame3 = tk.Frame(master=main_frame)
frame3.pack()

enc_np_btn = tk.Button(master=frame3, text='Encrypt Notepad File',
                       width=20, height=2, font=('Arial', 10),
                       command=open_file)
enc_np_btn.pack(side=tk.LEFT)

msg_btn = tk.Button(master=frame3, text='Create a message',
                       width=20, height=2, font=('Arial', 10))
msg_btn.pack(padx=(40, 0))

window.minsize(650, 175)
# np.create_write_notepad('enc', str(key))

# window.title('Hello Python')
# window.geometry("600x250")
# window.mainloop()

# Gets the requested values of the height and widht.


# windowWidth = 600
# windowHeight = 400
# # Gets both half the screen width/height and window width/height
# positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
# positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
#
# # Positions the window in the center of the page.
# window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))

window.mainloop()



