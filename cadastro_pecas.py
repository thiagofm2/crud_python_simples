def cadastrapeca(codigopeca):
    print('Código da peça: {}'.format(codigopeca))
    nomepeca = input('Digite o nome da peça que deseja cadastrar: ')
    fabricantepeca = input('Digite o nome do fabricante desta peça: ')
    precopeca = float(input('Digite o preço da peça: '))
    dicionariopeca = {
        'codigo': codigo,
        'nome': nomepeca,
        'fabricante': fabricantepeca,
        'preco': precopeca
    }
    listapecas.append(dicionariopeca.copy())


def consultapeca():
    while True:
        print('1 - Consultar todas as peças')
        print('2 - Consultar peças por código')
        print('3 - Consultar peças por fabricante')
        print('4 - Retornar')
        escolhauser = int(input('Digite o número da opção que deseja consultar: '))

        if escolhauser == 1:
            print('Lista de peças: ')
            for peca in listapecas:
                print('-' * 15)
                for key, value in peca.items():
                    print('{} : {}'.format(key, value))
                print('-' * 15)
        elif escolhauser == 2:
            codigoescolhido = int(input('Digite o código da peça que deseja consultar: '))
            for peca in listapecas:
                if peca['codigo'] == codigoescolhido:
                    for key, value in peca.items():
                        print('{} : {}'.format(key, value))

        elif escolhauser == 3:
            fabricante = input('Digite o nome do fabricante que deseja procurar: ')
            for peca in listapecas:
                if peca['fabricante'] == fabricante:
                    for key, value in peca.items():
                        print('{} : {}'.format(key, value))

        elif escolhauser == 4:
            print('Saindo...')
            return
        else:
            print('Opção não encontrada. Por favor, tente novamente.')
            continue
    return escolhauser


def removerpeca():
    codigolista = int(input('Digite o codigo da lista de peças que deseja deletar: '))
    for peca in listapecas:
        if peca['codigo'] == codigolista:
            listapecas.remove(peca)
            print('Produto removido.')

listapecas = []
codigo = 0
while True:
    print('1- Cadastrar peças')
    print('2- Consultar peças')
    print('3- Remover peças')
    print('4- Sair')
    codigoopcao = int(input('Número da opção que deseja: '))
    if codigoopcao == 1:
        codigo = codigo + 1
        cadastrapeca(codigo)
    elif codigoopcao == 2:
        consultapeca()
    elif codigoopcao == 3:
        removerpeca()
    elif codigoopcao == 4:
        print('Saindo...')
        break
    else:
        print('Opção não encontrada. Por favor, tente novamente.')
        continue
