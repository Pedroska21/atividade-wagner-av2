def calculadora (numero1,numero2):
    if (operador == 'somar'):
        print (numero1 + numero2)
    elif (operador == 'subtrair'):
        print (numero1 - numero2)
    elif (operador == 'multiplicar'):
        print (numero1 * numero2)
    elif (operador == 'dividir'):
        print (numero1 / numero2)
while (True):
    try:
        numero1 = float (input('digite um numero:'))
        numero2 = float (input('digite outro numero:'))
        operador = input('digite o operador desejado: somar, subtrair, multiplicar ou dividir: ')
        if numero1 <=0 or numero2 <=0:         
            print('digite um valor maior que 0')
            continue
        elif operador != 'somar' and operador != 'subtrair' and operador != 'multiplicar' and operador != 'dividir':
            print('digite um operador valido')
            continue
        else:
            calculadora (numero1, numero2)
            break
    except ValueError:
        print ('digite um numero valido')
