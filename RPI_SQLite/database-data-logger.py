from sense_hat import SenseHat
from sqlite3 import Connection, connect, Cursor
from datetime import datetime
from time import sleep

# Initialize DB connection and sensehat
dbconnect: Connection = connect("sensorDB.db")
sense: SenseHat = SenseHat()

# Initailize cursor to execute SQL commands and fetch results
cursor: Cursor = dbconnect.cursor()

# Loop every one second to insert sensor data into database
while True:
	humidity: float = round(sense.get_humidity(), 1)
	pressure: float = round(sense.get_pressure(), 1)
	temperature: float = round(sense.get_temperature(), 1)
	dateTime: str = datetime.now()
	cursor.execute("INSERT INTO sensordata (dateTime, temperature, humidity, pressure) VALUES (?, ?, ?, ?)", (dateTime, temperature, humidity, pressure))
	dbconnect.commit()
	sleep(1)
