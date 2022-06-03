
encontrado = False


while not encontrado:
    
    frutas = ['banana', 'maça', 'pera', 'uva', 'melancia', 'amora']

    frutinha = input('Qual fruta você gostaria de comprar?     ')

    frutinha = frutinha.lower()
    frutinha = frutinha.strip()
    
    if (frutinha in frutas):

        print (F'Opa, temos a fruta {frutinha}!')
        print('[1] Sim    [2] Não')
        resposta = int(input('Gostaria de incluir mais um???  '))
                
        if (resposta < 2):
            encontrado = encontrado
        else: 
            print('Tudo bem, muito obrigado!')
            print('Seu carrinho foi finalizado.')  
            break


    
    else:
        print ('Infelizmente, não temos essa fruta, tente outra! :(')

        encontrado = encontrado


