from gpiozero import LED
from time import sleep

class TrafficLight:
	
	def __init__(self):
		self.r: LED = LED(21)
		self.y: LED = LED(20)
		self.g: LED = LED(16)
		
	def red(self):
		self.r.on()
		self.y.off()
		self.g.off()
		sleep(1)
		
	def yellow(self):
		self.r.off()
		self.y.on()
		self.g.off()
		sleep(1)
		
	def green(self):
		self.r.off()
		self.y.off()
		self.g.on()
		sleep(1)
		
if __name__ == "__main__":
	traffic_lights = TrafficLight()
	traffic_lights.yellow()
