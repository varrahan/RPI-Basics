from datetime import datetime
import json
from sqlite3 import Connection, connect, Cursor, Row
from urllib.request import urlopen
from urllib.parse import urlencode

# Initialize DB connection and sensehat
dbconnect: Connection = connect("sensorDB.db")
dbconnect.row_factory = Row
# Initailize cursor to execute SQL commands and fetch results
cursor: Cursor = dbconnect.cursor()

# api key used to pull data
apiKey: str = "a808bbf30202728efca23e099a4eecc7"

# Input city that data will be pulled for
city: str = "Ottawa"

# Initialize APU components that will be inputted into API
params: dict[str,str] = {
	"q": city,
	"units": "metric",
	"APPID": apiKey
	}
arguments: str = urlencode(params)
address: str = "http://api.openweathermap.org/data/2.5/weather"
url: str = address + "?" + arguments

# Send API request and store values from API response into results dictionary
print(f"Requesting data from url: {url} \n")
webData: object = urlopen(url)
results: dict[str,str] = webData.read().decode('utf-8')
webData.close()

print("The raw JSON string returned by the query is")
print(results + "\n")

# Load json data into a readable format in data dictionary
data: dict[str,str] = json.loads(results)

# Compare previous row inserted from the same city to the row that is about to be inserted
speedCheck: str = f"SELECT * FROM WINDS WHERE City = '{city}' ORDER BY Date DESC LIMIT 1"
cursor.execute(speedCheck)
for row in cursor:
	prevWindSpeed: float = row["WindSpeed"]
	prevDate: str = row["Date"]
	if data["wind"]["speed"] > prevWindSpeed:
		print(f"Previous wind speed recorded at {prevDate} for {city} is less than current windspeed\n")
	elif data["wind"]["speed"] < prevWindSpeed:
		print(f"Previous wind speed recorded at {prevDate} for {city} is greater than current windspeed\n")
	elif data["wind"]["speed"] == prevWindSpeed:
		print(f"Previous wind speed recorded at {prevDate} for {city} is the same as current windspeed\n")

cursor.execute("INSERT INTO WINDS VALUES (?, ?, ?)", (city, datetime.now(), data["wind"]["speed"]))
dbconnect.commit()
print("Temperature: %d%sC" % (data["main"]["temp"], chr(176) ))
print("Humidity: %d%%" % data["main"]["humidity"])
print("Pressure: %d" % data["main"]["pressure"])
print("Wind: %d" % data["wind"]["speed"])

dbconnect.close()
