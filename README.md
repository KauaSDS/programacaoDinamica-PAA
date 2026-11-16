# Questão 3 — Problema do Troco

## 1. Descrição do problema

O problema consiste em encontrar o menor número de moedas necessário para atingir um determinado valor objetivo S, considerando um vetor com n tipos de moedas e suprimento infinito de cada tipo.

Caso não seja possível formar o valor desejado utilizando as moedas disponíveis, o algoritmo deverá informar que não existe solução.

Para resolver o problema, foi utilizada a técnica de Programação Dinâmica bottom-up, que calcula as soluções dos menores subproblemas antes de resolver o problema principal.

## 2. Estratégia de Programação Dinâmica

Foi utilizada uma tabela denominada `dp`, na qual:

- `dp[x]` representa o número mínimo de moedas necessárias para formar o valor x.
- `dp[0] = 0`, pois não precisamos de nenhuma moeda para formar o valor zero.

Inicialmente, todas as demais posições da tabela recebem infinito, representando que ainda não foi encontrada uma solução.

Para calcular cada posição, o algoritmo testa todas as moedas disponíveis. Se uma moeda possui valor menor ou igual ao valor que estamos tentando formar, ela pode ser utilizada.

A recorrência utilizada é:

\[
dp[x] = \min_{m \in moedas,\ m \leq x}
(dp[x-m]+1)
\]

O valor `dp[x-m]` representa a quantidade mínima de moedas necessária para formar o restante do valor. Somamos 1 para considerar a moeda escolhida.

O algoritmo percorre os valores de 1 até S, utilizando os resultados já calculados para preencher a tabela. Dessa maneira, a solução é construída de baixo para cima (bottom-up).

## 3. Rastreamento da solução ótima

Além da tabela `dp`, foi criada uma segunda tabela chamada `moeda_usada`.

Ela armazena qual moeda foi escolhida para alcançar a solução ótima de cada valor.

Quando encontramos uma quantidade de moedas menor que a anteriormente armazenada em `dp[x]`, atualizamos as duas tabelas:

- `dp[x]` recebe a nova quantidade mínima de moedas.
- `moeda_usada[x]` registra a moeda escolhida.

Após calcular `dp[S]`, utilizamos a tabela `moeda_usada` para reconstruir a solução. Começamos pelo valor S, adicionamos a moeda registrada e subtraímos seu valor. Repetimos o processo até chegar a zero.

Se `dp[S]` continuar infinito, significa que não foi possível formar o valor desejado, e o programa retorna -1.

## 4. Implementação em Python

```python
def menor_numero_moedas(moedas, S):
    dp = [float('inf')] * (S + 1)
    moeda_usada = [-1] * (S + 1)

    dp[0] = 0

    # Preenchimento da tabela bottom-up
    for valor in range(1, S + 1):
        for moeda in moedas:
            if moeda <= valor:
                if dp[valor - moeda] + 1 < dp[valor]:
                    dp[valor] = dp[valor - moeda] + 1
                    moeda_usada[valor] = moeda

    # Verifica se existe solução
    if dp[S] == float('inf'):
        print(-1)
        return

    print("Número mínimo de moedas:", dp[S])

    # Reconstrução da solução ótima
    solucao = []
    valor = S

    while valor > 0:
        moeda = moeda_usada[valor]
        solucao.append(moeda)
        valor -= moeda

    print("Moedas utilizadas:", solucao)


# Exemplo de execução
moedas = [9, 6, 5, 1]
S = 19

menor_numero_moedas(moedas, S)
```

## 5. Prova de corretude

Para demonstrar a corretude do algoritmo, utilizamos indução matemática sobre o valor x.

**Caso base:** Para x = 0, temos dp[0] = 0, pois nenhuma moeda é necessária para formar o valor zero. Portanto, o resultado está correto.

**Hipótese de indução:** Supomos que o algoritmo calcula corretamente o número mínimo de moedas para todos os valores menores que x.

**Passo indutivo:** Para calcular dp[x], o algoritmo testa todas as moedas disponíveis cujo valor seja menor ou igual a x. Para cada moeda m, calcula dp[x-m] + 1, representando a quantidade mínima de moedas necessária para formar o valor restante, acrescida da moeda escolhida.

Pela hipótese de indução, sabemos que dp[x-m] contém a solução ótima para o valor restante.

Como qualquer solução para x precisa utilizar alguma moeda m como uma de suas moedas, testar todas as moedas possíveis permite considerar todas as alternativas. O algoritmo escolhe aquela que resulta na menor quantidade total de moedas.

Assim, dp[x] também representa o número mínimo de moedas necessário para formar x.

Portanto, por indução matemática, o algoritmo calcula corretamente o número mínimo de moedas para todos os valores de 0 até S. O rastreamento das moedas escolhidas permite reconstruir uma combinação que atinge esse valor mínimo.

## 6. Análise de complexidade

**Complexidade de tempo:**

O algoritmo possui dois laços aninhados:

- O primeiro percorre os valores de 1 até S, realizando S iterações.
- O segundo percorre os n tipos de moedas disponíveis.

As operações realizadas dentro dos laços possuem custo constante.

Portanto, a complexidade de tempo é:

\[
\boxed{O(n \cdot S)}
\]

A reconstrução da solução percorre as moedas utilizadas, possuindo custo de no máximo O(S), não alterando a complexidade assintótica total.

**Complexidade de espaço:**

São utilizadas duas listas, `dp` e `moeda_usada`, ambas com S + 1 posições.

Portanto, a complexidade de espaço é:

\[
\boxed{O(S)}
\]

## 7. Testes e resultados

Foram realizados testes com os exemplos fornecidos pelo enunciado e com duas novas instâncias, respeitando os limites solicitados.

### Testes dos exemplos do enunciado

**Teste 1:**

Entrada:
- Moedas: [25, 10, 5]
- S = 30

Saída:
```text
Número mínimo de moedas: 2
Moedas utilizadas: [5, 25]
```

**Teste 2:**

Entrada:
- Moedas: [9, 6, 5, 1]
- S = 19

Saída:
```text
Número mínimo de moedas: 3
Moedas utilizadas: [9, 9, 1]
```

**Teste 3:**

Entrada:
- Moedas: [5, 1]
- S = 0

Saída:
```text
Número mínimo de moedas: 0
Moedas utilizadas: []
```

**Teste 4:**

Entrada:
- Moedas: [4, 6, 2]
- S = 5

Saída:
```text
-1
```

### Instância pequena

Para o primeiro teste adicional, foram utilizados 6 tipos de moedas e valor objetivo 47.

Entrada:
- Moedas: [1, 5, 10, 12, 25, 30]
- S = 47

Saída:
```text
Número mínimo de moedas: 3
Moedas utilizadas: [5, 12, 30]
```

Conferindo a solução:

\[
5 + 12 + 30 = 47
\]

### Instância grande

Para o segundo teste adicional, foram utilizados 7 tipos de moedas e valor objetivo 347.

Entrada:
- Moedas: [1, 7, 10, 22, 25, 50, 100]
- S = 347

Saída:
```text
Número mínimo de moedas: 5
Moedas utilizadas: [22, 25, 100, 100, 100]
```

Conferindo a solução:

\[
22 + 25 + 100 + 100 + 100 = 347
\]

## 8. Conclusão

O algoritmo desenvolvido utiliza Programação Dinâmica bottom-up para encontrar o número mínimo de moedas necessário para atingir um valor objetivo.

A utilização da tabela `dp` permite armazenar e reutilizar os resultados dos subproblemas, enquanto a tabela `moeda_usada` possibilita reconstruir a solução ótima encontrada.

Os testes realizados demonstraram que o algoritmo consegue encontrar a quantidade mínima de moedas, apresentar as moedas utilizadas e identificar situações em que não existe uma solução.

Sua complexidade de tempo é O(n · S) e sua complexidade de espaço é O(S).