from abc import ABC, abstractmethod


class Sensor(ABC):

    @abstractmethod
    def read_data(self):
        pass


class TemperatureSensor(Sensor):
    def read_data(self):
        return "26°C"


class MotionSensor(Sensor):
    def read_data(self):
        return "Motion detected"
