import random

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@123456789!@#$%^&*()_+='

def gerarSenha():
    senha = ''
    for i in range(10):
        senha += random.choice(caracteres)
    return senha

print(gerarSenha())