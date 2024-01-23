def adicionarContato(contatos, nome, telefone):
    contato = {"nome": nome, "telefone": telefone, "favorito": False}
    contatos.append(contato)
    print(f"{nome} [{telefone}] foi adicionado(a) a sua lista de contatos!")
    return


def visualizarContato(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "♥" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        print(f"{indice}. [{status}] {nome}: {telefone}")
    return


def editarContato(contatos, indiceContato, novoNumero):
    ajusteIndiceContato = indiceContato - 1
    if ajusteIndiceContato >= 0 and ajusteIndiceContato < len(contatos):
        contatos[ajusteIndiceContato]["telefone"] = novoNumero
        print(f"O telefone foi atualizado para {novoNumero}!")
    else:
        print("Indice de contato inválido!")
    return


def marcarFavorito(contatos, indiceContato):
    ajusteIndiceContato = int(indiceContato) - 1
    if ajusteIndiceContato >= 0 and ajusteIndiceContato < len(contatos):
        contatos[ajusteIndiceContato]["favorito"] = True
        print("O contato foi marcado(a) como favorito!")
    else:
        print("Indice de contato inválido!")
    return


def desmarcarFavorito(contatos, indiceContato):
    ajusteIndiceContato = int(indiceContato) - 1
    if ajusteIndiceContato >= 0 and ajusteIndiceContato < len(contatos):
        contatos[ajusteIndiceContato]["favorito"] = False
        print("O contato não é mais favorito.")
    else:
        print("Indice de contato inválido!")
    return


def contatosFavoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            status = "♥"
            nome = contato["nome"]
            telefone = contato["telefone"]
            print(f"{indice}. [{status}] {nome}: {telefone}")
    return


def apagarContato(contatos, indiceContato):
    ajusteIndiceContato = int(indiceContato) - 1
    if ajusteIndiceContato >= 0 and ajusteIndiceContato < len(contatos):
        contatoApagado = contatos.pop(ajusteIndiceContato)
        print(
            f"O contato de {contatoApagado['nome']} foi apagado com sucesso!")
    else:
        print("Indice de contato inválido!")
    return


contatos = []
while True:
    print("\nMenu da agenda de contatos:")
    print("1. Adicionar contato.")
    print("2. Visualizar lista de contatos.")
    print("3. Editar um contato.")
    print("4. Marcar contato como favorito.")
    print("5. Desmarcar contato como favorito.")
    print("6. Lista de contatos favoritos.")
    print("7. Apagar um contato.")
    print("8. Fechar menu.")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato que quer adicionar: ")
        telefone = input(f"Digite o número de {nome}: ")
        adicionarContato(contatos, nome, telefone)
    if opcao == "2":
        visualizarContato(contatos)
    if opcao == "3":
        visualizarContato(contatos)
        indiceContato = int(
            input("\nQual o índice do contato que deseja alterar? "))
        novoNumero = input("Novo número: ")
        editarContato(contatos, indiceContato, novoNumero)
    if opcao == "4":
        visualizarContato(contatos)
        indiceContato = input(
            "\nQual o índice do contato que deseja marcar como favorito? ")
        marcarFavorito(contatos, indiceContato)
    if opcao == "5":
        visualizarContato(contatos)
        indiceContato = input(
            "\nQual o índice do contato que deseja desmarcar como favorito? ")
        desmarcarFavorito(contatos, indiceContato)
    if opcao == "6":
        contatosFavoritos(contatos)
    if opcao == "7":
        visualizarContato(contatos)
        indiceContato = input("\nQual o índice do contato que deseja apagar? ")
        apagarContato(contatos, indiceContato)
    elif opcao == "8":
        break
