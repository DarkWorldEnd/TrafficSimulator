from enumerate.Color import Color
from Vehicle import Vehicle
from TrafficLight import TrafficLight
from Agent import Agent

traffic_light_x = TrafficLight("Traffic Light X", Color.GREEN)
traffic_light_y = TrafficLight("Traffic Light Y", Color.RED)

vehicle1_X = Vehicle("Vehicle 1_X")
vehicle2_X = Vehicle("Vehicle 2_X")

vehicle1_Y = Vehicle("Vehicle 1_Y")
vehicle2_Y = Vehicle("Vehicle 2_Y")

traffic_light_x.add_vehicle_observer(vehicle1_X)
traffic_light_x.add_vehicle_observer(vehicle2_X)
traffic_light_y.add_vehicle_observer(vehicle1_Y)
traffic_light_y.add_vehicle_observer(vehicle2_Y)

agent = Agent("Agent 1", [traffic_light_x], [traffic_light_y])

agent.start_clock()