from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def activate(self):
        pass

class SmartLight(SmartDevice):
    def activate(self):
        return self.name, "is shining at full brightness"

class SmartThermostat(SmartDevice):
    def activate(self):
        return self.name, "is now at 25℃"

devices = [
    SmartLight("Living Room Light"),
    SmartThermostat("Main Thermostat")
]

for device in devices:
    print(device.activate())

        
        