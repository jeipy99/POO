#questao 1
nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()
nome_completo = nome + " " + sobrenome
print(f"Olá, {nome_completo}! Seja bem-vindo.")

#questao 2
frase = input("Digite uma frase: ")
quantidade_espacos = frase.count(" ")
print(f"A frase contém {quantidade_espacos} espaços em branco.")

#questao 3
nome = input("Digite seu nome: ").strip()
for i in range(1, len(nome) + 1):
    print(nome[:i])
#questao 4

num_limpo = input("Digite o número do celular: ").replace("-", "").replace(" ", "")
if len(num_limpo) == 8:
    num_limpo = "9" + num_limpo
    print("Número corrigido para 9 dígitos.")

elif len(num_limpo) == 9:
    if num_limpo[0] != "9":
        print("Aviso: O número tem 9 dígitos mas não começa com 9.")
else:
    print("Aviso: Quantidade de dígitos inválida para um celular.")


if len(num_limpo) == 9:
    num_formatado = f"{num_limpo[:5]}-{num_limpo[5:]}"
    print(f"Número formatado: {num_formatado}")

#questao 5
frase = input("Digite uma frase: ")

indices = []
total_vogais = 0

for indice, letra in enumerate(frase):
    if letra.lower() in "aeiouáéíóúâêîôûãõà":
        indices.append(str(indice))
        total_vogais += 1
print(f"Índices das vogais: {', '.join(indices)}")
print(f"Total: {total_vogais} vogais")

