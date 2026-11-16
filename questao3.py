def menor_numero_moedas(moedas, S):
    dp = [float('inf')] * (S + 1)
    moeda_usada = [-1] * (S + 1)

    dp[0] = 0

    for valor in range(1, S + 1):
        for moeda in moedas:
            if moeda <= valor:
                if dp[valor - moeda] + 1 < dp[valor]:
                    dp[valor] = dp[valor - moeda] + 1
                    moeda_usada[valor] = moeda

    if dp[S] == float('inf'):
        print(-1)
        return

    print("Número mínimo de moedas:", dp[S])

    solucao = []
    valor = S

    while valor > 0:
        moeda = moeda_usada[valor]
        solucao.append(moeda)
        valor -= moeda

    print("Moedas utilizadas:", solucao)

# Teste 1
moedas = [1, 3, 4]
S = 6

menor_numero_moedas(moedas, S)