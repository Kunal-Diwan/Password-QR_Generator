import random

char = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"

def generate_password(length):
    return "".join(random.choice(char) for _ in range(length))
