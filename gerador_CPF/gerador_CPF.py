from random import randint

# Parte 1 - Gerar 9 umeros randomicamente
def gerador_cpf():
    cpf = []
    for _ in range(9):
        numero = randint(0, 9)
        cpf.append(numero)
    return cpf


'''
Parte 2 - Multiplicar cada um dos 9 numeros gerados pelo contador que inicia em 10
e decrementa 1 a cada loop, o resultado é atribuido a variavel total_soma,
depois multiplica o total por 10 e extrai o modulo da divisão por 11. 

Se for menor ou igual a 9, o valor é mantido, se for maior, é substituido por zero. 
'''
def calculo_primeiro_digito(cpf):
    total_soma = 0
    contador_regressivo = 10
    
    for numero in cpf:
        total_soma += numero * contador_regressivo
        contador_regressivo -= 1
    
    digito_1 = (total_soma * 10) % 11
    return digito_1 if digito_1 <= 9 else 0 


'''
Parte 3 - O processo do passo 2 é repetido, mas acrescentando o primeiro digito verificador obtido
após os calculos realizados, devido a isso o contador_regressivo inicia em 11. 
'''
def calculo_segundo_digito(cpf):
    total_soma = 0
    contador_regressivo = 11 
    
    for numero in cpf:
        total_soma += numero * contador_regressivo
        contador_regressivo -= 1

    digito_2 = (total_soma * 10) % 11
    return digito_2 if digito_2 <= 9 else 0


# ===== Chamada as funções =====

# 1 Gera os 9 primeiros numeros
cpf_gerado = gerador_cpf()

# 2 Calcula o primeiro dgito
digito1 = calculo_primeiro_digito(cpf_gerado)

# 3 Adiciona o digito encontrado a lista antes de prosseguir
cpf_gerado.append(digito1)

# 4 Calcula o segundo digito, lista possui 10 itens. 
digito2 = calculo_segundo_digito(cpf_gerado)

# 5 Adiciona o segundo digito a lista final
cpf_gerado.append(digito2)
    
# Transforma a lista de numeros em uma string
cpf_formatado = ''.join(map(str, cpf_gerado))
print(f"CPF Gerado: {cpf_formatado}")