# Weather Data Analysis

## 📌 Project Overview
This project analyzes weather data across multiple cities using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.  
It combines temperature, humidity, pressure, wind speed, wind direction, and weather description data to extract insights and visualize trends.

---

## 📂 Dataset
The project uses multiple CSV files:
- `temperature.csv`
- `humidity.csv`
- `pressure.csv`
- `wind_speed.csv`
- `wind_direction.csv`
- `weather_description.csv`
- `city_attributes.csv`

**Note:** The `city_attributes.csv` file contains metadata about cities, such as location and geographical attributes.

---

## 🛠 Features
1. **Data Loading & Transformation**
   - Reads multiple CSV files.
   - Uses **Pandas melt** to reshape datasets for merging.
   - Merges all datasets on `datetime` and `city`.

2. **Data Cleaning**
   - Renames columns for consistency.
   - Converts `datetime` column to `datetime` objects.
   - Fills missing values using forward fill (`ffill`).

3. **Data Analysis & Visualization**
   - **Monthly Average Temperature** (Line chart)
   - **Correlation Heatmap** between temperature, humidity, pressure, and wind speed.
   - **Wind Speed Distribution** (Histogram)
   - **Top 10 Weather Descriptions** (Horizontal bar chart)
   - **Hottest & Coldest Cities** ranking

---

## 📊 Visualizations
1. **Monthly Avg Temperature**
   - Shows seasonal temperature trends.

2. **Correlation Heatmap**
   - Displays correlations between numerical weather attributes.

3. **Wind Speed Distribution**
   - Shows the frequency distribution of wind speeds.

4. **Weather Description Frequency**
   - Shows the most common weather descriptions.

---

## 🚀 Installation & Usage
### **1. Install Dependencies**
```bash
pip install pandas numpy matplotlib seaborn
```

### **2. Place CSV files**
Ensure all CSV files are in the same directory as the script.

### **3. Run the Script**
```bash
python analysis.py
```

---

## 📈 Example Output
```
Top 5 Coldest Cities:
 cityA    5.2
 cityB    6.1
 cityC    7.0
 cityD    7.5
 cityE    8.0

Top 5 Hottest Cities:
 cityV    28.1
 cityW    29.0
 cityX    29.8
 cityY    30.5
 cityZ    31.2
```

---

## 🧠 Skills & Tools
- Python (Pandas, NumPy)
- Data Cleaning & Transformation
- Data Visualization (Matplotlib, Seaborn)
- Exploratory Data Analysis (EDA)

---

## 📜 License
This project is open-source and free to use for educational purposes.
