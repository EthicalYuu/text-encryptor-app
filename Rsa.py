import rsa

# RSA creating keys, encrypting & decrypting messages

class Rsa:
    def create_pair_of_keys(self):
        publicKey, privateKey = rsa.newkeys(512)
        return publicKey, privateKey

    def encrypt_key(self, key, publicKey):
        encMessage = rsa.encrypt(key.encode(), publicKey)
        return encMessage

    def decrypt_key(self, encrypted_msg, privateKey):
        decMessage = rsa.decrypt(encrypted_msg, privateKey).decode()
        return decMessage