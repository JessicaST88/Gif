# Criando uma lista vazia de frutas
frutas = []

# Adicionando frutas à lista
frutas.append("Maçã")
frutas.append("Banana")
frutas.append("Morango")

# Mostrando a lista completa
print("Lista de frutas:", frutas)

# Mostrando o tamanho da lista com len()
print("Quantidade de frutas:", len(frutas))

# Visualizando uma fruta pelo índice
indice = int(input("Digite o índice da fruta que deseja ver: "))
if 0 <= indice < len(frutas):
    print("A fruta escolhida é:", frutas[indice])
else:
    print("Índice inválido!")

# Alterando uma fruta pelo índice
indice = int(input("Digite o índice da fruta que deseja alterar: "))
if 0 <= indice < len(frutas):
    nova_fruta = input("Digite o novo nome da fruta: ")
    frutas[indice] = nova_fruta
    print("Lista atualizada:", frutas)
else:
    print("Índice inválido!")
