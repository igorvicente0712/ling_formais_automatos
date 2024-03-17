estados = []
alfabetos = []
primeiro_estado = ""
estados_aceitos = []
transicoes = {}

imputi = ""

estados = input().split()

alfabetos = input().split()
alfabetos.append("vazio")

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
print(caminhos)
for char in imputi:
    print(char)
    if char not in alfabetos:
        print("rejeita")
        break
    n_caminho = 0
    tam_caminhos = len(caminhos)
    while n_caminho < len(caminhos):
        # COLOCAR SITUAÇÃO DE EPSILON VULGO PASSAR PARA OS OUTROS ESTADOS INDEPENDENTE
        # print(n_caminho, caminhos[n_caminho], char)
        proximos = transicoes[caminhos[n_caminho]][char].split(",")
        # proximos_vazio = transicoes[caminhos[n_caminho]]["vazio"].split(",")
        # for estado in proximos_vazio:
        #     if estado == "vazio":
        #         break
        #     else:
        #         proximos.append(transicoes[estado][char])
        # for estado in proximos:
        if proximos[0] == "vazio":
            del caminhos[n_caminho]
        else:
            #proximos = transicoes[caminhos[n_caminho]][char].split(",")
            caminhos[n_caminho] = proximos[0]
            if len(proximos) > 1:
                for i in range(1, len(proximos)):
                    caminhos.insert(n_caminho + 1, proximos[i])
                    n_caminho = n_caminho + 1
            n_caminho = n_caminho + 1
        tam_caminhos = len(caminhos)
        # sleep(1)
    print(caminhos)
else:
    for estado_caminho in caminhos:
        if estado_caminho in estados_aceitos:
            print("aceita")
            break
    else:
        print("rejeita")
