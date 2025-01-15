from sqlite3 import Connection, connect
import pandas as pd
from pandas import DataFrame
import plotly.graph_objects as go

# Initialize DB connection 
dbconnect: Connection = connect("sensorDB.db")

query: str = "SELECT dateTime, temperature, humidity, pressure FROM sensordata"
# Load sql data based on query into dataframe
df: DataFrame = pd.read_sql_query(query, dbconnect)

# Initialize plot 
fig: go.Figure = go.Figure()

# Add traces for each column that we want to track in the plot
fig.add_trace(
	go.Scatter(x=df["dateTime"], y=df["temperature"], name="temperature", mode="markers", yaxis="y")
)
fig.add_trace(
	go.Scatter(x=df["dateTime"], y=df["humidity"], name="humidity", mode="markers", yaxis="y")
)
fig.add_trace(
	go.Scatter(x=df["dateTime"], y=df["pressure"], name="pressure", mode="markers", yaxis="y2")
)

# Configure plot with 2 y-axes to avoid skewed data, as certain datapoints are in the 1000's while others are in the 10's
fig.update_layout(
	title="Sensor data over time",
	xaxis={ "title": "Date Time" },
	yaxis={ "title": "Temperature (C), Humidity (%)" },
	yaxis2={ "title": "Pressure (millibars)",
			 "overlaying": "y",
			 "side": "right"
	}
)
# Display plot
fig.show()
dbconnect.close()
