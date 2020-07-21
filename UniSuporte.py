'''
    APLICAÇÃO - UniSuporte (Sistema de gerenciamento na manutenção de computadores)
'''

import _sqlite3

banco = _sqlite3.connect('uniSuporte.db')
sql = banco.cursor()
opcao  = ''

def listaComputador():
    for row in sql.fetchall():
        print('\nCLIENTE:', row[1])
        print('CPF:', row[2])
        print('RELATO:', row[3])
        print('--------------------------------------------')

while opcao != 's':
    print('''
        UniSuporte
            [1] - Cadastrar Computador
            [2] - Atualizar Status
            [3] - Listar Computadores
            [4] - Remover Computador
            [5] - Sair do Programa
        ''')

    opcao = int(input('Digite a opção: '))

    # [1] - Cadastra Computador
    if opcao == 1:
        nomeCliente = input('Informe o nome do Cliente: ')
        cpfCliente = input('Informe o CPF do Cliente: ')
        relato = input('Descreva qual o defeito da máquina: ')

        sql.execute(f"INSERT INTO computador (nomeCliente, cpfCliente, relato, status) VALUES ('{nomeCliente}', '{cpfCliente}', '{relato}', 'na fila')")
        banco.commit()
        print('DADOS INSERIDOS COM SUCESSO!')

    # [2] - Atualizar Status
    elif opcao == 2:
        cpfCliente = input('Informe o CPF do Cliente: ')
        sql.execute(f"SELECT * FROM computador WHERE cpfCliente = '{cpfCliente}'")

        print('\nCONFIRMA DADOS')
        for row in sql.fetchall():
            print('CLIENTE:', row[1])
            print('CPF:', row[2])
            print('RELATO:', row[3])
            print('\n')

        status = input('Informe o status do computador [em manuntenção ou concluído]: ')

        sql.execute(f"UPDATE computador SET status = '{status}' WHERE cpfCliente = '{cpfCliente}'")
        banco.commit()

        print('\nDADOS ALTERADOS COM SUCESSO!')

    elif opcao == 3:
        print('''
                        Opção de Listagem
                            [1] - Na Fila
                            [2] - Em Manutenção
                            [3] - Concluído
                ''')
        listagem = int(input('Informe a opção: '))

        if listagem == 1:
            sql.execute("SELECT * FROM computador WHERE status = 'na fila'")
            listaComputador()
        elif listagem == 2:
            sql.execute("SELECT * FROM computador WHERE status = 'em manutenção'")
            listaComputador()
        elif listagem == 3:
            sql.execute("SELECT * FROM computador WHERE status = 'concluído'")
            listaComputador()

    elif opcao == 4:
        id = int(input('Informe o ID do Computador: '))

        sql.execute(f'DELETE FROM computador WHERE id = {id}')
        banco.commit()

        print('\nDADOS EXCLUÍDOS COM SUCESSO!')

    elif opcao == 5:
        print('SAINDO DO PROGRAMA...')
        break

else:
    print('\n')







