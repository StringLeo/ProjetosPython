import random

CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()-_.'
password = ''

tamanhoPassword = input("Qual o tamanho da senha desejada? min[8] max[25]: ")

try:
    tamanhoPassword = int(tamanhoPassword)

    if tamanhoPassword < 8 or tamanhoPassword > 25:
        print("\nSó são aceitos números de 8 a 25.\n")
    else:
        while len(password) < tamanhoPassword:
            RandomChar = random.choice(CHAR)

            if RandomChar not in password:
                password += RandomChar
            else:
                continue
        print(f'Senha gerada com sucesso: {password}')
except ValueError:
    print("Por favor, Digitar somente números.")
finally:
    print("Programa encerrado.")
