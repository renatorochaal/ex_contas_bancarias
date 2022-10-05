class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # instanciando a classe Endereco (chamando),
        # salvando, faz oq for a especialidade dela

    def lista_endereco(self):
        for endereco in self.enderecos:
            print((endereco.cidade, endereco.estado))

    def __del__(self):
        print(f'{self.nome} FOI APAGADO ')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')