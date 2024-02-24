estados = []
alfabetos = []
primeiro_estado = ""
estados_aceitos = []
transicoes = {}

imputi = ""
estados = input().split()
estados_aceitos = input().split()
primeiro_estado = input()
alfabetos = input().split()

transicoes = {
    "q1,0":"q1",
    "q1,1":"q2",
    "q2,0":"q3",
    "q2,1":"q2",
    "q3,0":"q2",
    "q3,1":"q2",
}

imputi = input()

estado_atual = primeiro_estado

for char in imputi:
    if char not in alfabetos:
        print("rejeita")
        break
    else:
        estado_atual = transicoes[f"{estado_atual},{char}"]
else:
    if estado_atual in estados_aceitos:
        print("aceita")
    else:
        print("rejeita")
