# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

import email


def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    print("6 - Analisar pessoa")
    return int(input("Escolha uma opcao: "))
 
def cadastrar_pessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(nomes, idades, emails, pos):
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")
 
def buscar_pessoa(nomes, nome_procurado):
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)

def alterar_pessoa(nomes, idades, emails):
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        nomes[pos] = input("Novo nome: ")
        idades[pos] = int(input("Nova idade: "))
        emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(nomes, idades, emails, pos)

def listar_pessoas(nomes, idades, emails):
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(nomes)))

def classificar_faixa_etaria(idade):
    if idade < 12:
        print("Crianca")
    elif idade < 18:
        print("Adolescente")
    elif idade < 30:
        print("Adulto jovem")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")

def avaliar_email(email):
    if email == "":
        print("ausente")
    if "@" not in email:
        print("invalido")
    print("utilizavel")

def identificar_provedor(email):
    if email.endswith("@gmail.com"):
        print("Gmail")
    elif email.endswith("@outlook.com"):
        print("Outlook")
    elif email.endswith("@hotmail.com"):
        print("Hotmail")
    elif email.endswith("@utfpr.edu.br"):
        print("UTFPR")
    else:
        print("Outro")

def definir_condicao_contato(idade, email):
    if idade >= 18 and email != "":
        print("Cadastro apto para contato")
    elif idade >= 18 and email == "":
        print("Maior de idade sem contato")
    elif idade < 18 and email != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")

def analisar_pessoa(nomes, idades, emails):
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
        return

    idade = idades[pos]
    email_pessoa = emails[pos]

    print("Faixa etaria: " + classificar_faixa_etaria(idade))

    status_email = avaliar_email(email_pessoa)

    if status_email == "ausente":
        print("Cadastro incompleto: sem e-mail")
    elif status_email == "invalido":
        print("E-mail invalido")
    else:
        print("Provedor: " + identificar_provedor(email_pessoa))

    print(definir_condicao_contato(idade, email_pessoa))

nomes = []
idades = []
emails = []
 
qtd = 0
op = 0
 
while op != 5:
    #print("=========================")
    #print(" CADASTRO DE PESSOAS")
    #print("=========================")
    #print("1 - Cadastrar pessoa")
    #print("2 - Consultar pessoa")
    #print("3 - Alterar pessoa")
    #print("4 - Listar pessoas")
    #print("5 - Sair")
    #op = int(input("Escolha uma opcao: "))

    op = exibir_menu()
 
    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)
  
    elif op == 3:
        alterar_pessoa(nomes, idades, emails)            
    elif op == 4:
        listar_pessoas(nomes, idades, emails)
    elif op == 5:
        print("Saindo...") 
    elif op == 6:
        analisar_pessoa(nomes, idades, emails)
    else:
        print("Opcao invalida")
    
print("Fim do programa")
