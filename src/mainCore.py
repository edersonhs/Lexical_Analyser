from scanner import analisador
from log import nome_arquivo_log, mostraLog
from archives import *
from colors import colors
from time import sleep   # Intervalo
from os import system, name   # Limpar a tela
from subprocess import Popen   # Para abrir o notepad


def menu(*opcoes):
    while True:
        system('cls' if name == 'nt' else 'clear')
        opcao = 0
        print(f'{colors["amarelo"]}Selecione uma opção:')
        for nro, conteudo in enumerate(opcoes):
            print(f'{colors["roxo"]}{nro+1:>2} - {colors["branco"]}{conteudo}.')
        try:
            while True:
                opcao = int(input(f'{colors["amarelo"]}>>> {colors["branco"]}Sua opção: '))
                if opcao > len(list(opcoes)) or opcao <= 0:
                    input(f'\n{colors["vermelho"]}ERRO: Opção invalida. Digite uma opção existente!\n{colors["branco"]}'
                          f'Pressione enter para tentar novamente...')
                    break
                else:
                    break
        except Exception:
            input(f'\n{colors["vermelho"]}ERRO: Opção invalida. Digite um número valido!\n{colors["branco"]}Pressione '
                  f'enter para tentar novamente...')

        if opcao == 1:
            system('cls' if name == 'nt' else 'clear')
            nome_arquivo = './archives/codigo.txt'
            criarArquivo('./archives/log.txt')  # Reescrevendo um arquivo de log vazio para não concatenar com o log da ultima execução

            if arquivoExiste(nome_arquivo) and arquivoExiste(nome_arquivo_log):
                print(f'{colors["verde"]}{nome_arquivo.replace("./archives/", "")} e {nome_arquivo_log.replace("./archives/", "")} encontrados com sucesso!')
                analisador([word for word in lerArquivo(nome_arquivo)])   # Passando cada linha do código.txt para o analisador
                print(f'\n{colors["branco"]}LOG DO ANALISADOR LÉXICO:')
                if len([word for word in lerArquivo(nome_arquivo)]) == 0:
                    print(f'{colors["vermelho"]}>>> O arquivo esta vazio.')
                else:
                    mostraLog()
                input(f'\n{colors["branco"]}Pressione ENTER para continuar...')
            else:
                print(f'{colors["vermelho"]}ERRO: arquivos não encontrados.\n')
                while True:
                    try:
                        opcao_temp = str(input(f'{colors["branco"]}Deseja criar o arquivo? [S/N] ')).upper()[0]
                        system('cls' if name == 'nt' else 'clear')
                        
                        if opcao_temp == 'S':
                            criarArquivo(nome_arquivo)
                            input(f'{colors["branco"]}Pressione enter para continuar...')
                        else:
                            print(f'{colors["verde"]}Beleza! Retornando ao menu principal...')
                            sleep(2)
                    except Exception:
                        print(f'{colors["vermelho"]}ERRO: opção invalida. Digite uma opção valida!')
                    else:
                        break
        elif opcao == 2:
            Popen(["notepad","./archives/codigo.txt"])
        elif opcao == 3:
            system('cls' if name == 'nt' else 'clear')
            exit()


menu('Analisador Léxico', 'Editar o Código', 'Sair do Sistema')
