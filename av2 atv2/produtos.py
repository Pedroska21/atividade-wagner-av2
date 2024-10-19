produtos = {
        "dipirona" : "5,00"
    }

def adicionar_produto(): 
    while True:
        produto = input('digite o nome do produto: ')
        if not produto in produtos:
            preco = float (input('digite o preço do produto: '))
            produtos[produto] = preco
            print (f'{produto} foi adicionado')
            break
        elif produto in produtos:
            print ('Produto já existe na lista')

def editar_produto():
    lista_atualizar = {}
    while True:
        produto_editado = input ('digite o nome do produto que deseja editar: ')
        if produto_editado in produtos:
            novo_valor = float(input('digite o novo valor do produto: '))
            lista_atualizar[produto_editado] = novo_valor
            produtos.update(lista_atualizar)
            print ('preço do produto alterado com sucesso')
            break
        else:
            print ('o produto escolhido não existe na lista')
def deletar_produto():
    while True:
        produto_apagar = input('digite o nome do produto que deseja apagar: ')
        if produto_apagar in produtos:
            produtos.pop(produto_apagar)
            break
        else:
            print ('digite o nome de um produto valido')