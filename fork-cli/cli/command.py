from abc import ABC, abstractmethod
from cli.context import Context

class Command(ABC):
    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def execute(self, context: Context, args: list[str]):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass