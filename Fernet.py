from cryptography.fernet import Fernet
import base64
class MyFernet:
    # Creating a key to send using RSA

    def create_fernet_key(self):
        key = Fernet.generate_key()
        return key
        fernet = Fernet(key)
        return fernet

    # Using key to encrypt & decrypt messages

    def enc_using_fernet(self, msg, fernet):
         encrypted_msg = fernet.encrypt(msg.encode())
         return encrypted_msg

    def dec_using_fernet(self, enc_msg, fernet):
        # enc_msg = str.encode(enc_msg)
        decrypted_msg = fernet.decrypt(enc_msg).decode()
        return decrypted_msg

