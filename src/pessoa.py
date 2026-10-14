"""classe pessoa"""
class Pessoa:
    """definição da classe"""
    def __init__(self, nome, idade, email):
        """Inicializa a pessoa com nome, idade e e-mail."""
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def getIdade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    def getEmail(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    def setNome(self, nome):
        """Atualiza o nome da pessoa."""
        self.__nome = nome

    def setIdade(self, idade):
        """Atualiza a idade da pessoa."""
        self.__idade = idade

    def setEmail(self, email):
        """Atualiza o e-mail da pessoa."""
        self.__email = email
