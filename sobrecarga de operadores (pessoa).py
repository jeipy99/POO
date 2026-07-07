class Pessoa:
    def __init__(self, nome: str, altura: float):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"{self.nome} - {self.altura:.2f}m"

    def __gt__(self, other):
        if isinstance(other, Pessoa):
            return self.altura > other.altura
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Pessoa):
            return self.altura < other.altura
        return NotImplemented

if __name__ == "__main__":
    lst = []
    qtd = int(input("Quantas pessoas serão cadastradas? "))

    for i in range(qtd):
        print(f"\n--- Cadastro da {i+1}ª Pessoa ---")
        nome = input("Nome: ").strip()
        altura = float(input("Altura (em metros, ex: 1.75): "))
        lst.append(Pessoa(nome, altura))

    if lst:
        print("\n--- Resultados ---")
        print("Maior pessoa da lista:", max(lst))
        print("Menor pessoa da lista:", min(lst))

        print("\nPessoas ordenadas por altura:")
        for pessoa in sorted(lst):
            print(pessoa)
