lista_nome = list()
lista_nome = ["Arthur" ,"Antonio","Alexandre" , " Augusto","Alice","Aurora" ,"Alana"	,"Alícia"]
def adiciona_elemento_na_lista_nome(nome_pessoa):
    """ Realiza a insersão do elemento na lista"""
    lista_nome.append(nome_pessoa)
def remove_elemento_da_lista_nome(nome_pessoa):

    posicao = lista_nome.index(nome_pessoa)
    remove_elemento_da_lista_data_pelo_indice(posicao)
    lista_nome.remove(nome_pessoa)
def remove_elemento_da_lista_nome_de_um_data(posicao):
    lista_nome.pop(posicao)
def altera_elemento_da_lista_nome(novo_nome_pessoa, posicao):
 
    lista_nome[posicao] = novo_nome_pessoa

    if nome in lista_nome: return True
    return False
def mostra_elementos_individualmente_da_lista_nome():
    print("----------Nomes inseridas na lista :\n Nomes que já constam na lista não podem ser alterados!")
    print(" Obs.: Nomes que já constam na lista não podem ser alterados!")
    for nome_pessoa in lista_nome:
        print("   -",nome_pessoa)
def get_nome(posicao):
    return lista_nome[posicao]
def get_tam_nome():
    return len(lista_nome)
""" lista de datas """
lista_data = list()
lista_data = ["2/3/23","11/11/20","30/7/13","5/1/19","8/12/24","20/3/21","2/2/20","12/4/20",]
def adiciona_elemento_na_lista_data(nome_data):
    """ Realiza a insersão do elemento na lista"""
    lista_data.append(nome_data)
def remove_elemento_da_lista_data_pelo_indice(indice):
    lista_data.pop(indice)
def remove_elemento_da_lista_data(nome_data):
    """ Retira um elemento da lista. """
    lista_de_indices = []
    for posicao, data in enumerate(lista_data):
        if nome_data == data:
            lista_de_indices.append(posicao)
    lista_de_indices.reverse()
    for posicao in lista_de_indices:
        remove_elemento_da_lista_nome_de_um_data(posicao)
        remove_elemento_da_lista_data_pelo_indice(posicao)
def altera_elemento_da_lista_data(data_velha, novo_nome):
    """ Modifica um elemento na posição correta da lista. """
    for posicao,data in enumerate(lista_data):
        if data == data_velha:
            lista_data[posicao] = novo_nome
def elemento_esta_na_lista_data(data):
    if data in lista_data: return True
    return False
def mostra_elementos_individualmente_da_lista_data():
    print("-----Data inserida na lista: \n   Obs.: Datas que já constam na lista não podem ser alteradas!")
    for nome_data in list(set(lista_data)):
        print("   -",nome_data)
def get_data(posicao):
    return lista_data[posicao]
""" Menu """
def menu_principal():
    return input(("\n"*0) + """
            Menu
    0-	Finalizar o Programa
    1-	Adicionar Nome  e Data            
    2-	Listar os nomes e suas  respectivos datas
    3-	Alterar o nome de uma nome
    4-	Alterar o nome de um data
    5-	Listar todos os nomes de uma determinada data
    6-	Retirar da lista um nome ou data
    Escolha: """)
def menu_retirar_lista():
    return input("""
            Menu
    1-	Retirar nome da lista
    2-	Retirar data da lista
    Escolha:""")
def adicionar_nome():
    mostra_elementos_individualmente_da_lista_nome()
    while True:
        nome_pessoa = input(".........Adicione um novo Nome à lista:\n...Nome: ").upper()
        if not elemento_esta_na_lista_nome(nome_pessoa):
            adiciona_elemento_na_lista_nome(nome_pessoa)
            break
        else: input("-----Nome já consta na lista. [Enter]")
def adicionar_data():
    mostra_elementos_individualmente_da_lista_data()
    while True:
        nome_data = input(".......Escolha um data ou Digite nova Data.\n...Nome do data: ")
        if not elemento_esta_na_lista_data(nome_data):
            resposta = input("......... Data não consta na lista. Inserir? s/n: ").lower()
            if resposta == "n":
                continue
        adiciona_elemento_na_lista_data(nome_data)       
        break
def listar_nomes():
    """ Esta função tem a finalidade de mostrar todas as
        nomes da lista_nome e seu data.    """
    print("\n"*5)
    print("..... Nomes  e datas existentes na lista:")
    for x in range(get_tam_nome()):
        print(f"nome {get_nome(x).ljust(40,'.')}  data: {get_data(x)}")
    input("[Enter]")
def mostra_nome_data(data_escolhido):
    print("-------- Nomes do data",data_escolhido)
    for posicao,nome in enumerate(lista_nome):
        if get_data(posicao) == data_escolhido:
            print("   -nome:",nome)
def mostrar_nomes_por_data():
    print("-------- Datas Existentes:")
    mostra_elementos_individualmente_da_lista_data()
    data_escolhido = input("Escolha um data da Lista: ").upper()
    if elemento_esta_na_lista_data(data_escolhido):
        mostra_nome_data(data_escolhido)
    else: print("-------Elemento não encontrado na lista. ")
    input("[Enter]")
def alterar_nome():
    """ Esta função tem a finalidade de alterar o nome de
        alguma nome.    """
    while True:
        nome_pessoa = input("..........Nome para ser  alterado: ").upper()
        if elemento_esta_na_lista_nome(nome_pessoa):
            novo_nome_pessoa = input("..........Novo nome da nome: ").upper()
            if not elemento_esta_na_lista_nome(novo_nome_pessoa):
                posicao_na_lista = lista_nome.index(nome_pessoa)
                altera_elemento_da_lista_nome(novo_nome_pessoa,posicao_na_lista)
                break
            else: 
                input("-----Nome já consta na lista. [Enter]")
        else:
            input("-----Nome não consta na lista. [Enter]")
def alterar_data():
    """ Esta função tem a finalidade de alterar o nome de
        algum data.    """
    while True:
        nome_data_atual = input("........Nome do data para alterar: ").upper()
        if elemento_esta_na_lista_data(nome_data_atual):
            novo_nome = input("...........Novo nome do data: ").upper()
            altera_elemento_da_lista_data(nome_data_atual,novo_nome)
            return
        else:
            input("-----Data digitado não consta na lista. [Enter]")
        alterar_data()
def excluir_nomes():
    """ Esta função tem a finalidade de retirar o nome de uma nome da lista
        de nomes.    """
    mostra_elementos_individualmente_da_lista_nome()
    while True:
        nome_pessoa = input(".........Nome da nome para retirar da lista: ").upper()
        if elemento_esta_na_lista_nome(nome_pessoa):
            remove_elemento_da_lista_nome(nome_pessoa)
            break
        else:
            input("-----Nome não consta na lista. [Enter]")
def excluir_data():
    """ Esta função tem a finalidade de retirar o nome de um data da lista
        de datas, retirando também as nomes vinculadas a este data.    """
    mostra_elementos_individualmente_da_lista_data()
    while True:
        nome_data = input("...Nome do data para retirar da lista: ").upper()
        if elemento_esta_na_lista_data(nome_data):
            remove_elemento_da_lista_data(nome_data)
            break
        else:
            input("-----Data não consta na lista. [Enter]")
def retirar_nome_ou_data():
    resposta = menu_retirar_lista()
    if resposta == '1':
        excluir_nomes()
    if resposta == '2':
        excluir_data()
def adicionar_nome_data():
    adicionar_nome()
    adicionar_data()
# Programa - Início
while True:
    resposta = menu_principal()
    if resposta == '0':break
    elif resposta == '1': adicionar_nome_data()
    elif resposta == '2': listar_nomes()
    elif resposta == '3': alterar_nome()
    elif resposta == '4': alterar_data()
    elif resposta == '5': mostrar_nomes_por_data()
    elif resposta == '6': retirar_nome_ou_data()
