precos_em_moedas = [
    [1, 6, 8, 10],
    [3, 7, 10, 15]
]

taxas_de_conversao = {
    'JPY': 0.67,
    'GBP': 0.51
}

def conversao_para_iene (preco, moeda):
    return preco * taxas_de_conversao[moeda]

preco_em_iene = [
    [conversao_para_iene(preco, 'JPY') for preco in linha] if i == 0
    else [conversao_para_iene( preco, 'GBP')for preco in linha]
    for i , linha in enumerate(precos_em_moedas)
]

print("Preços convertidos em IENE: ")
for linha in preco_em_iene:
    print(linha)