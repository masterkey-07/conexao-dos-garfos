from abc import ABC, abstractmethod

class DotBuilder(ABC):
    
    @abstractmethod
    def to_dot() -> None:
        pass