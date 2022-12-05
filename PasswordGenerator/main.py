import random

CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()-_.'
password = ''

TAMANHO_PASSWORD = input("Qual o tamanho da senha desejada? min[8] max[25]: ")

try:
    TAMANHO_PASSWORD = int(TAMANHO_PASSWORD)

    if TAMANHO_PASSWORD < 8 or TAMANHO_PASSWORD > 25:
        print("\nSó são aceitos números de 8 a 25.\n")
    else:
        while len(password) < TAMANHO_PASSWORD:
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
