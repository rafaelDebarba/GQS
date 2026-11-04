"""Gerenciamento do cadastro de pessoas."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria

class CadastroPessoas:
    """Mantém e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self, repositorio: Optional[RepositorioPessoas] = None):
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()
        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        """Adiciona uma pessoa ao cadastro e a retorna."""
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Busca uma pessoa pelo nome ou retorna None se não encontrar."""
        return self.__repositorio.buscar(nome)

    def listar(self) -> List[Pessoa]:
        """Retorna a lista de pessoas cadastradas."""
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Atualiza os dados da pessoa identificada pelo nome."""
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa
