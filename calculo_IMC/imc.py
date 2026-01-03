# recebe altura e peso e calcula o IMC do usuario

def calcula_imc(altura, peso):
    imc = peso / (altura ** 2)
    return imc

while True:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcula_imc(altura, peso)
    print(f"Seu IMC é: {imc:.2f}")

    continuar = input("Deseja calcular outro IMC? (s/n): ")
    if continuar.lower() != "s":
        break
