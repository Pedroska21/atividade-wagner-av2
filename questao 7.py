def conversor (grau_temperatura, temperatura, resultado):
    if grau_temperatura == 'c':
        resultado = temperatura * 1,8 + 32
        print(f'{temperatura} graus celsius são {resultado} em fahrenheit')




grau_temperatura = input('escolha entre celsius ou fahrenheit. [c ou f]: ')[:1]
temperatura = float(input('insira a temperatura desejada'))
resultado = 0
conversor(grau_temperatura, temperatura, resultado)
print (resultado)