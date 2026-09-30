"""Sistema de cadastro de pessoas."""


def exibir_menu():
    """Exibe o menu principal e retorna a opcao escolhida."""
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
    """Cadastra uma nova pessoa nas listas."""
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email_pessoa = input("Informe o email: ")
    emails.append(email_pessoa)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def exibir_pessoa(nomes, idades, emails, pos):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])

    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def buscar_pessoa(nomes, nome_procurado):
    """Busca uma pessoa pelo nome e retorna sua posicao."""
    pos = 0

    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1

    return -1


def consultar_pessoa(nomes, idades, emails):
    """Consulta e exibe uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)


def alterar_pessoa(nomes, idades, emails):
    """Altera os dados de uma pessoa existente."""
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
    """Lista todas as pessoas cadastradas."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")

    pos = 0

    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1

    print("Total: " + str(len(nomes)))


def classificar_faixa_etaria(idade):
    """Retorna a faixa etaria correspondente a idade."""
    if idade < 12:
        return "Crianca"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"


def avaliar_email(email_pessoa):
    """Retorna a situacao do e-mail."""
    if email_pessoa == "":
        return "ausente"
    if "@" not in email_pessoa:
        return "invalido"
    return "utilizavel"


def identificar_provedor(email_pessoa):
    """Retorna o provedor do e-mail."""
    if email_pessoa.endswith("@gmail.com"):
        return "Gmail"
    if email_pessoa.endswith("@outlook.com"):
        return "Outlook"
    if email_pessoa.endswith("@hotmail.com"):
        return "Hotmail"
    if email_pessoa.endswith("@utfpr.edu.br"):
        return "UTFPR"
    return "Outro"


def definir_condicao_contato(idade, email_pessoa):
    """Retorna a condicao de contato da pessoa."""
    if idade >= 18 and email_pessoa != "":
        return "Cadastro apto para contato"
    if idade >= 18 and email_pessoa == "":
        return "Maior de idade sem contato"
    if idade < 18 and email_pessoa != "":
        return "Menor de idade com contato"
    return "Menor de idade sem contato"


def analisar_pessoa(nomes, idades, emails):
    """Analisa faixa etaria, e-mail e condicao de contato."""
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


def main():
    """Executa o sistema de cadastro."""
    nomes = []
    idades = []
    emails = []
    op = 0

    while op != 5:
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


if __name__ == "__main__":
    main()
