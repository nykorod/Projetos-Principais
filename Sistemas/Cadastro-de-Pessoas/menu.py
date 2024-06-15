from blz import *

a = 'cadastros.txt'

def arqexiste(a):
    try:
        a = open(a, 'rt')
    except: 
        return False
    else:
        return True

def arqcriar(a):
    try:
        a = open(a, 'wt+')
    except:
        print('O arquivo já existe.')
    else:
        print('Arquivo criado com sucesso.')
    finally:
        a.close()

def arqcad(a):
    nome = input('Seu nome:  ')
    idade = leiaint('Sua idade:  ')
    try:
        arq = open(a, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever no arquivo.')
        else:
            print('Cadastro realizado com sucesso!')

def arqler(a):
    try:
        arq = open(a, 'rt')
    except:
        print('Erro ao ler os cadastros.')
    else:
        for pos, linha in enumerate(arq):
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Pessoa {pos+1}: {dado[0]}, {dado[1]} anos')
    finally:
        arq.close()

def menu():
     if not arqexiste(a):
          arqcriar(a)
     while True:
        lin()
        opcoes('Cadastrar nova pessoa', 'Visualizar cadastros', 'Fechar programa')
        lin()
        n = leiaint('Qual é a sua escolha?:  ')
        if n == 1:
            arqcad(a)
        elif n == 2:
            arqler(a)
        elif n == 3:
            lin('Saindo do sistema')
            lin('Finalizando...')
            break
        else:
            print('Número inválido! Tente novamente.')