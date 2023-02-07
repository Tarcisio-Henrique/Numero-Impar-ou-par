def impar():
    num1 = int(input('Digite um numero: '))
    resto = num1 % 2

    if resto == 0:
        print(f'O numero {num1} é Par!')
    elif resto != 0:
        print(f'O número {num1} é Impar!')
impar()