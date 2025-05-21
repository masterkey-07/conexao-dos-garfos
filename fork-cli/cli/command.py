from abc import ABC, abstractmethod
from cli.context import Context

class Command(ABC):
    @abstractmethod
    def execute(self, context: Context):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass