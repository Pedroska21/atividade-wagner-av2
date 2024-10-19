def adicionar_lista (numero):
    print (sum(lista_numero))
lista_numero = []
numero = int(input("adicione um numero a lista: "))
lista_numero.append (numero)
adicionar_numero = input('deseja adicionar outro numero?[s ou n]')[:1]
while adicionar_numero == 's':
    numero = int(input("digite outro numero a lista:"))
    lista_numero.append (numero)
    adicionar_numero = input ("deseja adicionar outro numero?[s ou n]")[:1]

adicionar_lista(numero)