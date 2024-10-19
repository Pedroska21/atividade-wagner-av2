def calculadora (numero1,numero2):
    operador = input('digite que calculo deseja fazer: soma, subtração, divisão ou multiplicação: ')
    if (operador == 'soma'):
        print (numero1 + numero2)
    elif (operador == 'subtração'):
        print (numero1 - numero2)
    elif (operador == 'multiplicação'):
        print (numero1 * numero2)
    elif (operador == 'divisão'):
        print (numero1 / numero2)
while (True):
    try:
        numero1 = float (input('digite um numero:'))
        numero2 = float (input('digite outro numero:'))
        if numero1 <=0 or numero2 <=0:         
            print('digite um valor maior que 0')
            continue
        else:
            calculadora (numero1, numero2)
    except ValueError:
        print ('digite um numero valido')