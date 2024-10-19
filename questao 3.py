def numero_primo (numero):
    if numero == 0 or numero == 1:
     return False
    elif numero > 1:
        for i in range (2, numero):
            if (numero % i) == 0:
                return False
                
                
        else:
            return True

numero = int(input('digite um numero: '))

numero_primo(numero)
print (numero_primo(numero))