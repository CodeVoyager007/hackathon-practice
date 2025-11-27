from abc import ABC, abstractmethod

class Skill(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
