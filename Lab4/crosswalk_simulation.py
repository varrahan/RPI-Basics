from traffic_lights import TrafficLight
from time import sleep
from gpiozero import Button

if __name__ == "__main__":
	lights = TrafficLight()
	button = Button(18)
	
	while(True):
		lights.red()
		sleep(5)
		lights.green()
		button.wait_for_press(5)
		lights.yellow()
		sleep(2)
	
