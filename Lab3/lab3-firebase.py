# Lab 3 – Pyrebase example code 
import pyrebase 
import random 
import time
from datetime import datetime
from sense_hat import SenseHat
from collections import OrderedDict
# Config will contain the information needed to connect to your firebase 
#   The API KEY and Project ID are found in your project settings 
#   The DB URL can be found under the Realtime Database tab 
config: dict[str,str] = { 
  "apiKey": "AIzaSyCAOhBAwJJvDN_CPTdGOvfkdse0t6vQSvc", 
  "authDomain": "sysc3010-lab3-e9b06.firebaseapp.com", 
  "databaseURL": "https://sysc3010-lab3-e9b06-default-rtdb.firebaseio.com/", 
  "storageBucket": "sysc3010-lab3-e9b06.appspot.com" 
} 

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset: str = "sensor1" 
username: str = "VarrahanU" 

# RPI Sensehat connection initialization
sense: SenseHat = SenseHat()

def writeData():
		# Write 10 data entries to the DB in a loop 
		key: int = 0
		sense_data: dict[str, str or int] = {}
		while(key<10): 
			
			# Sensehat data
			humidity: float = round(sense.get_humidity(), 1)
			pressure: float = round(sense.get_pressure(), 1)
			temperature: float = round(sense.get_temperature(), 1)
			dateTime: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			
			# When writing to your DB each child is a JSON key:value pair
			db.child(username).child(dataset).child(key).child("humidity").set(humidity)
			db.child(username).child(dataset).child(key).child("pressure").set(pressure)  
			db.child(username).child(dataset).child(key).child("temperature").set(temperature)
			db.child(username).child(dataset).child(key).child("date").set(dateTime) 

			key += 1

def getUserNames() -> list[str]:
	database_keys = sorted(db.child("/").get().val().keys())
	return database_keys
		
def readData():
# Returns the entry as an ordered dictionary (parsed from json)
	names = getUserNames()
	for name in names:
		all_data = db.child(name).child(dataset).get()
		# Convert data to a dictionary
		data_dict = all_data.val()
		if not data_dict:
			return []
		recent_entries = []
		if isinstance(data_dict, OrderedDict):
			for key in range(7, 10):
				entry = data_dict[str(key)]
				recent_entries.append(entry)
			data_dict = [item for item in data_dict]
		else:
			# Sort the keys numerically to get the most recent entries
			# Get the 3 most recent entries
			for entry in data_dict[-3:]:
				recent_entries.append(entry)
		print(name)
		print(recent_entries)
		print("\n")

		
if __name__ == "__main__":
	readData()
