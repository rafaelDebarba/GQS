"""Contrato para o armazenamento de pessoas."""

from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Define as operações de armazenamento usadas pelo cadastro."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Armazena uma pessoa."""

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca uma pessoa pelo nome."""

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Lista as pessoas armazenadas."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Substitui a pessoa identificada pelo nome."""
