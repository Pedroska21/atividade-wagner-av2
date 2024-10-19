def quantidade_palavras(texto):
    palavras = texto.split ()

    return len(palavras)

texto = input("digite uma frase: ")

print ("a quantidade de palavras é: ", quantidade_palavras(texto))