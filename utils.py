from cryptography.fernet import Fernet


def encrypt_password(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    dec_password = fernet.encrypt(password.encode())
    return key + dec_password


def decrypt_password(dec_password):
    key = dec_password[:44]
    fernet = Fernet(key)
    dec_password = dec_password[44:]
    password = fernet.decrypt(dec_password)
    return password
