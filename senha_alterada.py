senha = input()
nova = input()
coincide = 0

if len(senha) > len(nova):
    menor = nova
    maior = senha
elif len(nova) > len(senha):
    menor = senha
    maior = nova
else:
    menor = senha
    maior = nova

for i in range(len(menor)):
    if menor[i] == maior[i]:
        coincide += 1
        print(f"'{menor[i]}' posição {i+1}")

if coincide == 0:
    print('Senha alterada')
else:
    print('Senha NÃO alterada')
