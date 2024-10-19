def quantidade_vogal (texto):
    lista_vogais = ["a","e","i","o","u","A","E","I","O","U"]
    vogal = 0
    quantidade = 0
    for vogal in range(len(texto)):
        if texto[vogal] in lista_vogais:
            quantidade +=1
    print (quantidade)

texto = input('digite uma palavra: ')

quantidade_vogal(texto)