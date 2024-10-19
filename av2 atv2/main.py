from usuarios import *
from produtos import *
def menu_login ():
    while True:
        try:
            print ('bem vindo ao sistema de registro de farmacia\n\n')
            escolha = int(input('1. Entrar\n2. Cadastrar\n3. Sair\n'))
            if escolha == 1:
                conectado = autenticar()
                if conectado == True:
                    menu_produtos ()
            if escolha == 2:
                criar_usuario ()
            if escolha == 3:
                print ('Encerrando')
                break
            if escolha < 1 or escolha >= 4:
                print ('digite um numero valido\n')
        except ValueError:
            print ('digite um numero\n')

def menu_produtos ():
    while True:
        try:
            print ('Escolha o que deseja fazer\n\n')
            escolha_sistema = int(input('1. cadastrar produto\n2. Editar valor do produto\n3. Excluir produto\n4. Exibir lista de produtos\n5. Saindo\n'))
            if escolha_sistema == 1:
                adicionar_produto()
            if escolha_sistema == 2:
                editar_produto()
            if escolha_sistema == 3:
                deletar_produto()
            if escolha_sistema == 4:
                print (produtos)
            if escolha_sistema == 5:
                print ('Saindo\n')
                break
            if escolha_sistema < 1 or escolha_sistema >= 6:
                print ('Digite um numero valido\n')
        except ValueError:
            print ('digite um numero\n')

menu_produtos()