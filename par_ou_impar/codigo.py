# Verifica se numero é par ou impar usando 

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    if numero.lower() == 'sair':
        break
    if numero.isdigit():
        numero = int(numero)
        if numero % 2 == 0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
    else:
        print("Por favor, digite um número válido.")
