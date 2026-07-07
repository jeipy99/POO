#Q1
def contagem_caracteres(texto):
    contador = {}
    for caractere in texto:
      
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador

resultado = contagem_caracteres("banana")
print(resultado)

#Q2
import string

frequencia_palavras = {}

try:
    with open("estomago.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.lower().strip()
            
            for pontuacao in string.punctuation + "—–" :
                linha = linha.replace(pontuacao, " ")

            palavras = linha.split()

            for palavra in palavras:
                if palavra in frequencia_palavras:
                    frequencia_palavras[palavra] += 1
                else:
                    frequencia_palavras[palavra] = 1

    palavras_ordenadas = dict(sorted(frequencia_palavras.items(), key=lambda item: item[1], reverse=True))

    print(palavras_ordenadas)

#Q3
  def mesclar_dicionarios(dic1, dic2):
    resultado = dic1.copy()
    
    for chave, valor in dic2.items():
        if chave in resultado:
            if valor > resultado[chave]:
                resultado[chave] = valor
        else:
            resultado[chave] = valor
            
    return resultado

d1 = {'a': 10, 'b': 20, 'c': 5}
d2 = {'b': 15, 'c': 30, 'd': 40}
print(mesclar_dicionarios(d1, d2))

except FileNotFoundError:
    print("Erro: O arquivo 'estomago.txt' não foi encontrado no mesmo diretório.")

#Q4
def filtrar_dicionario(dicionario, lista_chaves):
    return {chave: dicionario[chave] for chave in lista_chaves if chave in dicionario}

dados = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo', 'profissao': 'Dev'}
chaves_desejadas = ['nome', 'cidade', 'salario']

resultado = filtrar_dicionario(dados, chaves_desejadas)
print(resultado)

#Q5
def resultado_votacao(lista_votos):
    totais_por_candidato = {}
    votos_totais_geral = 0

    for sessao in lista_votos:
        for candidato, votos in sessao.items():
            totais_por_candidato[candidato] = totais_por_candidato.get(candidato, 0) + votos
            votos_totais_geral += votos

    resultado_final = {}
    for candidato, total_votos in totais_por_candidato.items():
        percentual = (total_votos / votos_totais_geral) * 100 if votos_totais_geral > 0 else 0
        resultado_final[candidato] = (total_votos, round(percentual, 2))
        
    return resultado_final

votos_sessoes = [
    {"Candidato A": 120, "Candidato B": 80},
    {"Candidato A": 150, "Candidato B": 150, "Brancos/Nulos": 20},
    {"Candidato A": 30, "Candidato B": 70}
]

print(resultado_votacao(votos_sessoes))
