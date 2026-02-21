from sensor import Sensor
import time

class Heater:
    def on(self):
        print("ON")
    def off(self):
        print("OFF")

    def reachRequestedTemp(self, temp):
        measuredTemp = Sensor().measuredTemp()
        print("Initial temp:", measuredTemp)

        while measuredTemp < temp:
            print(f"Temperature: {measuredTemp}")
            measuredTemp += 1
            time.sleep(1)

        print(f"Temperature: {measuredTemp}")
        self.off()




