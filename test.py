from cryptography.fernet import Fernet

def create_fernet_key():
    key = Fernet.generate_key()
    return key

def enc_using_fernet(msg, fernet):
    encrypted_msg = fernet.encrypt(msg.encode())
    return encrypted_msg


def dec_using_fernet(enc_msg, fernet):
    # enc_msg = str.encode(enc_msg)
    decrypted_msg = fernet.decrypt(enc_msg).decode()
    return decrypted_msg

# Using key to encrypt & decrypt messages

chosen_file = open('Msg.txt', "r")
content = chosen_file.read()

chosen_file = open('Enc_Msg.txt', "r")
enc_content = chosen_file.read()


key = create_fernet_key()
msg = 'hello'
encryption = enc_using_fernet(content, Fernet(key))
decryption = dec_using_fernet(encryption, Fernet(key))
print(type(encryption))
print(type(enc_content))

