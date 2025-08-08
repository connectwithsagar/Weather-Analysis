import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs
temp_df = pd.read_csv("temperature.csv")
humidity_df = pd.read_csv("humidity.csv")
pressure_df = pd.read_csv("pressure.csv")
windSpeed_df = pd.read_csv("wind_speed.csv")
windDirection_df = pd.read_csv("wind_direction.csv")
weatherDescription_df = pd.read_csv("weather_description.csv")
cityAttribute_df = pd.read_csv("city_attributes.csv")


#Melting the dataset
temp_df = temp_df.melt(id_vars=["datetime"], var_name="city", value_name="temperature")
humidity_df = humidity_df.melt(id_vars=["datetime"], var_name="city", value_name="humidity")
pressure_df = pressure_df.melt(id_vars=["datetime"], var_name="city", value_name="pressure")
windSpeed_df = windSpeed_df.melt(id_vars=["datetime"], var_name="city", value_name="wind_speed")
windDirection_df = windDirection_df.melt(id_vars=["datetime"], var_name="city", value_name="wind_direction")
weatherDescription_df = weatherDescription_df.melt(id_vars=["datetime"], var_name="city", value_name="weather_description")


#Viewing the dataset
print("Temp Columns:", temp_df.columns)
print("Humidity Columns:", humidity_df.columns)
print("Pressure Columns:", pressure_df.columns)
print("Wind Speed Columns:", windSpeed_df.columns)
print("Wind Direction Columns:", windDirection_df.columns)
print("Weather Description Columns:", weatherDescription_df.columns)
print("City Attributes Columns:", cityAttribute_df.columns)

#changing CIty to city so that I can merge data
cityAttribute_df.rename(columns={"City": "city"}, inplace=True)


# Merge datasets on datetime and city
df = temp_df.merge(humidity_df, on=["datetime", "city"])
df = df.merge(pressure_df, on=["datetime", "city"])
df = df.merge(windSpeed_df, on=["datetime", "city"])
df = df.merge(windDirection_df, on=["datetime", "city"])
df = df.merge(weatherDescription_df, on=["datetime", "city"])
df = df.merge(cityAttribute_df, on="city")
#
#
#Converting date and time
df["datetime"] = pd.to_datetime(df["datetime"])

df.fillna(method="ffill", inplace=True)  # or df.dropna()


#Monthly Average Temperature
df["month"] = df["datetime"].dt.month
monthlyAvg_temp = df.groupby("month")["temperature"].mean()
monthlyAvg_temp.plot(kind="line", title="Monthly Avg Temperature", marker='o')
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()



#Correlation HeatMap
corr = df[["temperature", "humidity", "pressure", "wind_speed"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()



#Wind Speed Distribution
plt.hist(df["wind_speed"], bins=25, color='skyblue')
plt.title("Wind Speed Distribution")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Frequency")
plt.grid()
plt.show()


#Most Frequent Weather Descriptions
desc_counts = df["weather_description"].value_counts().head(10)
desc_counts.plot(kind="barh", title="Top 10 Weather Descriptions")
plt.xlabel("Frequency")
plt.show()


#Hottest and Coldest Cities
city_avg_temp = df.groupby("city")["temperature"].mean().sort_values()
print("Top 5 Coldest Cities:\n", city_avg_temp.head())
print("Top 5 Hottest Cities:\n", city_avg_temp.tail())
