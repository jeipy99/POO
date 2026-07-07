#questao 1
numeros = []

print("Digite os números inteiros. Digite 'sair' para encerrar.")
while True:
    entrada = input("Digite um número: ").strip().lower()
    
    if entrada == 'sair':
        if len(numeros) < 4:
            print(f"Por favor, insira pelo menos 4 números. Você inseriu {len(numeros)}.")
            continue
        break
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'sair'.")

print(f"\nA lista original: {numeros}")
print(f"Os 3 primeiros elementos: {numeros[:3]}")
print(f"Os 2 últimos elementos: {numeros[-2:]}")
print(f"A lista invertida: {numeros[::-1]}")
print(f"Elementos de índice par: {numeros[::2]}")
print(f"Elementos de índice ímpar: {numeros[1::2]}")

#questao 2
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = [url[4:-4] for url in urls]

print(f"URLs: {urls}")
print(f"dominios: {dominios}")

#questao 3
import random

lista_original = [random.randint(-100, 100) for _ in range(10)]

lista_ordenada = sorted(lista_original)
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))
soma_valores = sum(lista_original)
media_valores = soma_valores / len(lista_original)

print(f"A lista ordenada, sem modificar a original: {lista_ordenada}")
print(f"A lista original: {lista_original}")
print(f"O índice do maior valor da lista: {indice_maior} (Valor: {max(lista_original)})")
print(f"O índice do menor valor da lista: {indice_menor} (Valor: {min(lista_original)})")
print(f"A soma dos valores da lista: {soma_valores}")
print(f"A média dos valores da lista: {media_valores:.2f}")

#questao 4
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    lista1.append(int(input()))

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    lista2.append(int(input()))

lista_intercalada = []
i = 0

while i < len(lista1) and i < len(lista2):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
    i += 1

lista_intercalada.extend(lista1[i:])
lista_intercalada.extend(lista2[i:])

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))

#questao 5
import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = []

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
   
interseccao.sort()

print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"Intersecção - {interseccao}")

#questao 6
import random

# Cria uma lista com 20 valores aleatórios entre 0 e 100
lista_original = [random.randint(0, 100) for _ in range(20)]
print(f"Lista original:\n{lista_original}\n")

tamanho_divisao = int(input("Tamanho para divisão: "))

sublistas = []

for i in range(0, len(lista_original), tamanho_divisao):
    sublistas.append(lista_original[i : i + tamanho_divisao])

print(f"Sublistas:\n{sublistas}")

#questao 7
n = int(input("Digite n: "))
matriz = []

for i in range(n):
    linha = [i] * n
    matriz.append(linha)

print("Resultado:")
for linha in matriz:
    print(linha)
