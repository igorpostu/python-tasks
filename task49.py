from abc import ABC, abstractmethod

class AnimalInterface(ABC):
    @abstractmethod
    def make_a_noise():
        pass

    @abstractmethod
    def move():
        pass

class Dog(AnimalInterface):
    def make_a_noise(self) -> str:
        return 'bark'
    
    def move(self) -> str:
        return 'run'

class Bird(AnimalInterface):
    def make_a_noise() -> str:
        return 'tweet'
    
    def move() -> str:
        return 'fly'