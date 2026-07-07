class Onibus:
    def __init__(self, placa: str, nome_motorista: str, num_assentos: int):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False] * num_assentos

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if not (0 <= indice < len(self.assentos)):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos) - 1}")
        return self.assentos[indice]

    def __setitem__(self, indice, valor):
        if not (0 <= indice < len(self.assentos)):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos) - 1}")
        if not isinstance(valor, bool):
            raise TypeError("Valor deve ser booleano (True/False)")
        self.assentos[indice] = valor

    def __str__(self):
        totais = len(self.assentos)
        ocupados = self.assentos.count(True)
        livres = self.assentos.count(False)
        
        return (f"Ônibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}\n"
                f"Assentos totais: {totais}\n"
                f"Assentos ocupados: {ocupados}\n"
                f"Assentos livres: {livres}")

if __name__ == "__main__":
    onibus = Onibus("ABC-1234", "João Silva", 10)
    print(len(onibus))
    onibus[0] = True
    print(onibus)
