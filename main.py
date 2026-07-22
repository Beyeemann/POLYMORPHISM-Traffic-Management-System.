class TrafficDevice:
    def activate(self):
        print("Activating")
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic light is activating")
class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed camera is activating")
class PedestrainSignal(TrafficDevice):
    def activate(self):
        print("Pedestrain signal is activating")
class EmergencySiren:
    def activate(self):
        print("Emergency siren is activating")
trafficdevices=[TrafficDevice(),SpeedCamera(),PedestrainSignal(),EmergencySiren()]
for trafficdevice in trafficdevices:
    trafficdevice.activate()