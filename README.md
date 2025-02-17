# Algoritmo de Multiplicação de Karatsuba

## Sobre o Projeto
Este projeto implementa o **Algoritmo de Multiplicação de Karatsuba** em Python, um método eficiente para multiplicação de números grandes. O algoritmo divide os números em partes menores e aplica recursão para reduzir o número de operações de multiplicação tradicionais.

## Como Rodar o Projeto
### Pré-requisitos
- Python instalado (versão 3.x recomendada)
- Visual Studio Code instalado

### Instalando o Visual Studio Code
1. Acesse [VS Code](https://code.visualstudio.com/)
2. Faça o download e instale a versão adequada para seu sistema operacional
3. Instale as extensões recomendadas:
   - Python
   - Code Runner (opcional, para executar scripts diretamente no VS Code)

### Clonar o Repositório
```bash
$ git clone https://github.com/seu-usuario/karatsuba-python.git
$ cd karatsuba-python
```

### Executar o Código
```bash
$ python main.py
```

## Lógica do Algoritmo
O **Algoritmo de Karatsuba** funciona dividindo os números em duas partes e aplicando multiplicações menores recursivamente. A lógica básica segue os seguintes passos:

1. **Caso Base:** Se ambos os números forem menores que 10, retorna a multiplicação direta.
2. **Divisão:** Separa cada número em duas partes:
   - `x = 1234 → (a = 12, b = 34)`
   - `y = 5678 → (c = 56, d = 78)`
3. **Recursão:** Calcula quatro multiplicações menores:
   - `e = karatsuba(a, c)  # Parte superior dos dois números`
   - `f = karatsuba(b, d)  # Parte inferior dos dois números`
   - `g = karatsuba(a, d)  # Parte superior de x com inferior de y`
   - `h = karatsuba(b, c)  # Parte inferior de x com superior de y`
4. **Cálculo Final:** Recompõe o número original com:
   
   \[ x \times y = e \times 10^{2q} + (g+h) \times 10^q + f \]

## Implementação em Python
```python
def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    else:
    n = max(len(str(x)), len(str(y)))
    q = n // 2
    
    a, b = divmod(x, 10**q)
    c, d = divmod(y, 10**q)
    
    e = karatsuba(a, c)
    f = karatsuba(b, d)
    g = karatsuba(a, d)
    h = karatsuba(b, c)  
    
    return e * 10**(2*q) + (g + h) * 10**q + f

# Exemplo de uso:
x = 1234
y = 5678
print(f"Resultado da multiplicação: {karatsuba(x, y)}")
```

## Complexidade Assintótica
- **Pior Caso e Caso Médio:** Ambos os casos seguem a complexidade geral \(O(n^2)\), pois, mesmo que os números tenham diferentes tamanhos, o algoritmo ainda realiza 4 chamadas recursivas e soma os resultados.
- **Melhor Caso:**\(O(1)\)  Ocorre quando os números são pequenos (apenas 1 dígito), pois a multiplicação é feita diretamente.


## Complexidade Ciclomática
A complexidade ciclomática é calculada pela fórmula:

\[ M = E - N + 2P \]

Onde:
- \(E\) = 7 (Número de arestas no grafo)
- \(N\) = 7 (Número de nós no grafo) 
- \(P\) = 1 Número de componentes conexos 

O fluxo de controle do algoritmo possui condições e chamadas recursivas, aumentando sua complexidade. Para o código acima, o cálculo aproximado da complexidade ciclomática resulta em **M = 2**, indicando um fluxo de controle simples

## Contribuições
Sinta-se à vontade para contribuir com melhorias! Para isso, abra um Pull Request com sugestões .

---
**Autor:** Gabriel Ferreira Amaral



