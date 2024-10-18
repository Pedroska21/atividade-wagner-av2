usuarios = { 
        "teste" : "admin", "username" : "password",
    }
produtos = [
    {
        "produto" : "dipirona",
        "preço" : "5,00",
        "quantidade" : "10"
    }
]
def autenticar ():
    login = (input('digite o nome de usuario:'))
    senha = (input('digite a senha:'))
    if login in usuarios and usuarios[login] == senha:
        print ('logado com sucesso')
    else:
        print ('senha ou usuarios incorretos')

def criar_usuario ():
    login = input('digite o nome do usuario:')
    if login in usuarios:
        print ('este usuario ja existe')
    else:
        senha = input('digite a senha do usuario:')
        usuarios [login] = senha
        print ('novo usuario criado')


print ('bem vindo ao sistema de registro de farmacia\n\n')


while True:
    escolha = int(input('1. Entrar\n2. Cadastrar\n3. Sair\n'))
    if escolha == 1:
        autenticar ()
        break
    if escolha == 2:
        criar_usuario ()
    if escolha == 3:
        print ('Encerrando')
        break
    if escolha >= 4:
        print ('digite um numero valido')

while True:
    print ('Escolha o que deseja fazer\n\n')
    escolha_sistema = int(input('1. cadastrar produto\n2. Editar produto\n3. Excluir produto\n4. Exibir lista de produtos\n 5. Saindo'))
    if escolha_sistema == 3:
        excluir = input('digite o nome do item a ser excluido')
        del produtos [excluir]
    if escolha_sistema == 4:
        print (produtos)
    if escolha_sistema == 5:
        print ('Saindo')
        break
    if escolha_sistema >= 6:
        print ('Digite um numero valido')