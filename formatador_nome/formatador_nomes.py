'''
Lê um arquivo xlsx com uma lista de nomes faz a seguinte formação:

1 - Remove espaços desnecessarios
2 - Remove a pontução
3 - Torna tudo maiusculo
4 - Adicione o sulfixo 'YOUBPOTECH' ao final de todos os nomes

'''

import csv
import string
import os

# 1. Configuração dos caminhos (para garantir que abra na mesma pasta)
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_entrada = os.path.join(pasta_atual, 'dados.csv')
caminho_saida = os.path.join(pasta_atual, 'nomes_formatados.csv')

def limpar_formatar_csv():
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(caminho_entrada):
        print(f"Erro: O arquivo '{caminho_entrada}' não foi encontrado.")
        return

    print("Iniciando processamento...")

    try:
        # Abre o arquivo original (leitura) e o novo (escrita)
        # encoding='utf-8-sig' ajuda a ler arquivos CSV salvos pelo Excel corretamente
        with open(caminho_entrada, 'r', encoding='utf-8-sig') as f_entrada, \
             open(caminho_saida, 'w', encoding='utf-8', newline='') as f_saida:
            
            leitor = csv.reader(f_entrada)
            escritor = csv.writer(f_saida)
            
            # Tabela para remover pontuação (ex: pontos, vírgulas, exclamações)
            tabela_remocao = str.maketrans('', '', string.punctuation)

            contagem = 0
            
            for linha in leitor:
                # Pula linhas vazias
                if not linha:
                    continue
                
                # Pega o primeiro item da linha (Coluna A)
                nome_original = linha[0]
                
                # --- APLICANDO AS REGRAS ---
                
                # 1. Torna tudo maiúsculo
                nome_formatado = nome_original.upper()
                
                # 2. Remove pontuação
                nome_formatado = nome_formatado.translate(tabela_remocao)
                
                # 3. Remove espaços desnecessários (inicio e fim)
                nome_formatado = nome_formatado.strip()
                
                # 4. Adiciona o sufixo 'YOUBPOTECH'
                # Verifica se o nome não ficou vazio após a limpeza
                if nome_formatado:
                    nome_final = f"{nome_formatado} YOUBPOTECH"
                    
                    # 5. Escreve no novo arquivo
                    escritor.writerow([nome_final])
                    contagem += 1

        print(f"Sucesso! {contagem} nomes foram processados.")
        print(f"Arquivo salvo em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função
limpar_formatar_csv()