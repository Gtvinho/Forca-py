
    
print("Digite a palavra:")
palavra = input()
palavra = palavra.upper() 

i = len(palavra)
x = len(palavra)

while i != 0:
    chances = len(palavra) 

    print("suas chances sao:")
    print(x)
    
    letra = input("Digite a letra:")
    letra = letra.upper()
    
    
    if x == 0:
        print("voce perdeu!")
        
    elif letra in palavra:
        print('voce acertou!')
        print(letra)
    
    else:
        print ("voce errou")
        i = i - 1
        x = x - 1
