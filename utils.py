from cryptography.fernet import Fernet


def encrypt(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    dec_password = fernet.decrypt(password.encode())
    return key + dec_password


def decrypt(dec_password):
    key = dec_password[:44]
    fernet = Fernet(key)
    dec_password = dec_password[44:]
    password = fernet.decrypt(dec_password)
    return password
