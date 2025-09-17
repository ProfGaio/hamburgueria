class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
    # fim do construtor __init__()

    def exibirLanche(self):
        """
        Exibe os dados do lanche cadastrado (nome, preco e ingredintes[])
        """
        print(f"Sanduíche:{self.nome}; Preço:{self.preco};Ingredientes:{self.ingredientes}")
# Fim da classe















""" sanduiches = [] # Criada a lista vazia de sanduiches

for i in range(4): # laço para cadastrar 4 sanduiches
   sanduiche = input("Nome do novo sanduiche:")
   # Adiciona o sanduiche à lista sanduiches
   sanduiches.append(sanduiche)  

# Laço para exibir os sanduiches cadastrados
for sanduiche in sanduiches:
    print(f"Lanche: {sanduiche}")


 """