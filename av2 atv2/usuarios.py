usuarios = { 
        "teste" : "admin", "username" : "password",
    }
def autenticar ():
    login = (input('digite o nome de usuario:'))
    senha = (input('digite a senha:'))
    if login in usuarios and usuarios[login] == senha:
        print ('logado com sucesso')
        return True
    else:
        print ('senha ou usuarios incorretos')
def criar_usuario ():
    while True:
        login = input('digite o nome do usuario:')
        if login in usuarios:
            print ('este usuario ja existe')
        else:
            senha = input('digite a senha do usuario:')
            usuarios [login] = senha
            print ('novo usuario criado\n')
            break
