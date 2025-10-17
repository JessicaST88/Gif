# Lista vazia de alunos
alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ").strip()
    
    if nome.lower() == "sair":
        break
    
    if nome in alunos:
        print("Este aluno já está na lista! Digite outro nome.")
    else:
        alunos.append(nome)
        print(f"{nome} adicionado à lista!")

# Mostrando a lista final de alunos
print("\nLista de alunos cadastrados:")
for i, aluno in enumerate(alunos):
    print(f"{i}: {aluno}")
