estados = []
alfabetos = []
primeiro_estado = ""
estados_aceitos = []
transicoes = {}

imputi = ""

estados = input().split()

alfabetos = input().split()
alfabetos.append("vario")

primeiro_estado = input()

estados_aceitos = input().split()

transicoes = {}

for i in range(len(estados)):
    transicao = input().split()
    transicoes[transicao[0]] = {}
    for j in range(len(alfabetos)):
        transicoes[transicao[0]][alfabetos[j]] = transicao[j+1]
    #transicoes[transicao[0]][alfabetos[j]] = transicao[j+1]

imputi = input()

caminhos = [primeiro_estado]

for char in imputi:
    if char not in alfabetos:
        print("rejeita")
        break
    n_caminho = 0
    while n_caminho < len(caminhos):
        # COLOCAR SITUAÇÃO DE EPSILON VULGO PASSAR PARA OS OUTROS ESTADOS INDEPENDENTE
        if transicoes[f"{caminhos[n_caminho]}"][f"{char}"] == "vazio":
            del caminhos[i]
        else:
            proximos = transicoes[f"{caminhos[i]}"][f"{char}"].split(",")
            if len(proximos) > 1:
                for i in range(1, len(proximos)):
                    caminhos.insert(n_caminho, proximo)
            n_caminho = n_caminho + 1
            proximos_vazio = transicoes[f"{caminhos[i]}"][f"vazio"].split(",")
else:
    for estado_caminho in caminhos:
        if estado_caminho in estados_aceitos:
            print("aceita")
            break
        else:
            print("rejeita")
