digitos = ''

numero = int(input('Digite um numero '))
base = int(input('digite a base para conversão de 1 a 10 '))
n = numero
if base == 1:
    resto = numero * base
    digitos = str(resto)
else:
    while n > 0:
        resto = n % base
        digitos = str(resto) + digitos
        n //= base

print(digitos)