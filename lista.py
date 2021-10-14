pessoas = [{'nome': 'Arthur', 'idade': 19}, {'nome': 'Maria', 'idade': 4}, {'nome': 'José', 'idade': 39},
           {'nome': 'Pedro', 'idade': 35}, {'nome': 'Joana', 'idade': 50}]

#testa se os valores inseridos sao validos
def leiaint(n):
    try:
        return int(n)
    except NameError:
        return n

#adiciona um dicionario na lista
def adicionarpessoas(nome, idade):
    pessoas.append({'nome': nome, 'idade': int(idade)})
    return f'{nome} de {idade} anos adicionado(a) à lista.'

#o menu para despoluir o codigo
def menu():
    print("-=" * 16)
    print("[1]Adicionar pessoas à lista\n"
          "[2]Exibir lista\n"
          "[3]Classificar pessoas da lista\n"
          "[4]Outros...")
    print("-=" * 16)

#outro menu
def menuop2():
    print("-=" * 10)
    print("[1]Ordem de idade\n"
          "[2]Ordem alfabética\n"
          "[3]Ordem de cadastro")
    print("-=" * 10)

#verifica se o nome digitado existe na lista
def achapessoa(nome):
    for pessoa in pessoas:
        if pessoa['nome'] == nome:
            return 1
    return 0

#verifica e retorna a pessoa se achar
def idade(n):
    for pessoa in pessoas:
        if pessoa['nome'] == n:
            return pessoa


while True:
    print("-=" * 16)
    print(f'Lista de cadastros:')
    for i in pessoas:
        print(f'{i}')
    menu()
    while True:
        opcao = leiaint(input("Escolha a opção desejada: "))
        if type(opcao) == int and (opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4):
            break

    if opcao == 1:
        print("Adicionando pessoas na lista...")
        lastaddnome = str(input('Nome da pessoa que deseja adicionar: ')).strip().capitalize()
        while True:
            lastaddidade = leiaint(input(f'Idade de {lastaddnome}: '))
            if type(lastaddidade) == int:
                break
        print(adicionarpessoas(nome=lastaddnome, idade=lastaddidade))
        # lastaddnome e lastaddidade para ter acesso aos ultimos dados adicionados se quiser

    elif opcao == 2:
        print("Exibindo lista em...")
        menuop2()
        while True:
            exibir = leiaint(input("Escolha a opção desejada: "))
            if type(exibir) == int and exibir == 1 or exibir == 2 or exibir == 3:
                break

        if exibir == 1:
            listaordem = sorted(pessoas, key=lambda pessoas: pessoas['idade'])
            for i in range(len(pessoas)):
                print(listaordem[i])

        elif exibir == 2:
            listaordem = (sorted(pessoas, key=lambda pessoas: pessoas['nome']))
            for i in range(len(pessoas)):
                print(listaordem[i])

        else:
            for i in pessoas:
                print(f'{i}')

    elif opcao == 3:
        while True:
            nome = input("Digite um nome presente na lista para saber sua classificação: ")
            result = achapessoa(nome)
            if result == 1:
                break

        pessoa = (idade(nome))

        if 0 <= pessoa['idade'] < 12:
            print(f'{pessoa["nome"]} é Criança.')

        elif 12 <= pessoa['idade'] <= 19:
            print(f'{pessoa["nome"]} é Adolescente.')

        elif 19 < pessoa['idade'] < 65:
            print(f'{pessoa["nome"]} é Adulto(a).')

        elif 65 <= pessoa['idade']:
            print(f'{pessoa["nome"]} é Idoso(a).')

    elif opcao == 4:
        print("[1]Ver ultimo adicionado\n"
              "[2]Sair")
        while True:
            escolha = leiaint(input('Escolha a opção: '))
            if type(escolha) == int and (escolha == 1 or escolha == 2):
                break

        if escolha == 1:
            try:
                lastaddnome
            except NameError:
                print("Ninguém adicionado rescentemente!")
            else:
                print(f'{lastaddnome}, {lastaddidade} anos')

        if escolha == 2:
            break
