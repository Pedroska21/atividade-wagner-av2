def calculadora (numero1,numero2):
        print (numero1 + numero2)
        print (numero1 - numero2)
        print (numero1 * numero2)
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