


def karatsubaExemplo(x,y,n):
    if n == 1:
        return x*y
    else:
            # n é o tamanho do número em quantidade de casas exemplo: 1234 = 4
            # a divisão por 2 é para pegar o meio do número
            # exemplo: 1234 = 4/2 = 2, 12
        n = max(len(str(x)), len(str(y)))
        q = n // 2
        # divisão com resto do número a fim
        # de pegar a parte inteira e a parte decimal
        # exemplo: 1234 = 12, 34
        a, b = divmod(x, 10**q)
        print(f"quociente: {a}, resto: {b}")
        c, d = divmod(y, 10**q)
        print(f"quociente: {c}, resto: {d}")
        
        e = karatsubaExemplo(a, c, q) # 12 * 56 parte superior dos dois números
        f = karatsubaExemplo(b, d, q) # 34 * 78  parte inferior dos dois números
        g = karatsubaExemplo(a, d , q) # 12 * 78 parte superior de um número e parte inferior do outro
        h = karatsubaExemplo(b, c, q) # 34 * 56 parte inferior de um número e parte superior do outro
                    # 10**n = 10^4 = 10000(voltar para o tamanho original do número)
        return e * 10**(n) + (g+h) * 10**q + f
                                    #10**q = 10^2 = 100(voltar para o tamanho original do número)
resultadoex = karatsubaExemplo(1234, 5678, 4)
print(f"exemplo do karatsuba com x(primeiro valor) = 1234 e \ny(segundo valor) = 5678 : {resultadoex}")
print("-------------------------------------------------------------------")



def karatsuba(x,y):
    if x < 10 and y < 10:
        return x*y
    else:
            # tamanho do número em quantidade de casas exemplo: 1234 = 4
            # a divisão por 2 é para pegar o meio do número
            # exemplo: 1234 = 4/2 = 2, 12
        n = max(len(str(x)), len(str(y)))
        q = n // 2
        # divisão com resto do número a fim
        # de pegar a parte inteira e a parte decimal
        # exemplo: 1234 = 12, 34
        a, b = divmod(x, 10**q)
        
        c, d = divmod(y, 10**q)
        
        
        e = karatsuba(a, c) # 12 * 56 parte superior dos dois números
        f = karatsuba(b, d) # 34 * 78  parte inferior dos dois números
        g = karatsuba(a, d) # 12 * 78 parte superior de um número e parte inferior do outro
        h = karatsuba(b, c) # 34 * 56 parte inferior de um número e parte superior do outro
                    # 10**n = 10^4 = 10000(voltar para o tamanho original do número)
        return e * 10**(n) + (g+h) * 10**q + f
                                    #10**q = 10^2 = 100(voltar para o tamanho original do número)
xvalue = input("Digite o primeiro valor inteiro: ")
yvalue = input("Digite o segundo valor inteiro: ")

resultado = karatsuba(int(xvalue), int(yvalue))
