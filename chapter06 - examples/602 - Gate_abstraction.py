from abc import ABC, abstractmethod


class Gate(ABC):

    @abstractmethod
    def operate(self, a, b):
        pass


class ANDGate(Gate):
    def operate(self, a, b):
        return a & b


class ORGate(Gate):
    def operate(self, a, b):
        return a | b
