"""
Estre programa recebe um numero digitado pelo usuario 
e verifica se o mesmo é um CPF válido. 
"""

# Esta funcao pede o CPF e confirma se foi digitado somente numeros 
def solicita_CPF():

    while True:
        
        entrada = input('Digite o CPF sem pontuação: ').strip()
        try:
            numero = int(entrada) # Tenta converter o valor digitado para int
            return numero # se funcionar, retorno o CPF
        except ValueError:
            print('Erro! Por favor, digite somente os numeros do CPF.')

# Esta funcao transforma a variavel int em uma lista com os digitos separados. 
def prepara_cpf(cpf_int):

    cpf_str = str(cpf_int)

    lista_de_digitos = [int(digito) for digito in cpf_str]

    return lista_de_digitos

# Esta funcao faz o calculo para o primeiro digito verificardor 
def calcula_primeiro_digito_verificador():
    
    total_soma = 0 # soma as multiplicacoes
    contador = 0 # permite a iteracao da lista cpf_transformado

    # para cada numero na lista, multiplica por laco indo de 10 ate 2
    for laco in range(10, 1, -1):
        total_soma += laco * cpf_transformado[contador]

        # incrementa um no contador para passar por todos elementos da lista
        contador += 1

    # variavel recebe o resto da divisao do total por 11
    modulo = total_soma % 11

    # se o modulo for menor que 2, automaticamente o digito verificador recebe zero
    if modulo == 0 or modulo == 1:
        digito_verificador = 0
    else:
        digito_verificador = 11 - modulo

    return digito_verificador

# Esta funcao faz o calculo para o segundo digito verificador 
def calcula_segundo_digito_verificador():

    total_soma = 0 # soma as multiplicacoes
    contador = 0 # permite a iteracao da lista cpf_transformado

    # para cada numero na lista, multiplica laco por cada numero na lista
    for laco in range(11, 1, -1):
        total_soma += laco * cpf_transformado[contador]

        # incrementa o contador
        contador += 1

    # veriavel recebe o resto da divisao do total divido por 11
    modulo = total_soma % 11

    # se o modulo for menor que 2, automaticamente o digito verificador recebe zero
    if modulo <= 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - modulo

    return digito_verificador

cpf_digitado = solicita_CPF()
cpf_transformado = prepara_cpf(cpf_digitado)

primeiro_digito_verificador = calcula_primeiro_digito_verificador()
segundo_digito_verificardor = calcula_segundo_digito_verificador()

if primeiro_digito_verificador == cpf_transformado[9] and segundo_digito_verificardor == cpf_transformado[10]:
    print('O CPF digitado é válido')
else:
    print('Erro! Verifique os numeros digitados e tente novamente.')
