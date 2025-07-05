from sense_hat import SenseHat

sense: SenseHat = SenseHat()

humidity: float = round(sense.get_humidity(), 1)
pressure: float = round(sense.get_pressure(), 1)
temperature: float = round(sense.get_temperature(), 1)

sensor_data: str = f"Temperature: {temperature}. Pressure: {pressure}. Humidity: {humidity}."

sense.show_message(sensor_data, 0.05)

sense.clear()
