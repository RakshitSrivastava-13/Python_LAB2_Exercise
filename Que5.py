# Sample weather data for New York City from August 1, 2024, to July 10, 2024
weather_data = [
    {'Date': '2024-08-01', 'Max Temp (C)': 29, 'Min Temp (C)': 20, 'Humidity (%)': 65},
    {'Date': '2024-08-02', 'Max Temp (C)': 31, 'Min Temp (C)': 22, 'Humidity (%)': 70},
    {'Date': '2024-08-03', 'Max Temp (C)': 28, 'Min Temp (C)': 21, 'Humidity (%)': 60},
    {'Date': '2024-08-04', 'Max Temp (C)': 32, 'Min Temp (C)': 23, 'Humidity (%)': 55},
    {'Date': '2024-08-05', 'Max Temp (C)': 30, 'Min Temp (C)': 22, 'Humidity (%)': 50},
    # ... (more data here)
    {'Date': '2024-07-10', 'Max Temp (C)': 27, 'Min Temp (C)': 19, 'Humidity (%)': 75},
]

def find_high_low_temperatures(data):
    """Find the highest and lowest temperatures recorded."""
    max_temp = max(record['Max Temp (C)'] for record in data)
    min_temp = min(record['Min Temp (C)'] for record in data)
    return max_temp, min_temp

def count_days_above_30(data):
    """Determine the number of days with temperatures above 30°C."""
    count = sum(1 for record in data if record['Max Temp (C)'] > 30)
    return count

def average_humidity(data):
    """Compute the average humidity over the specified period."""
    total_humidity = sum(record['Humidity (%)'] for record in data)
    return total_humidity / len(data) if data else 0

# Demonstrate the functions
if __name__ == "__main__":
    # Find the highest and lowest temperatures
    max_temp, min_temp = find_high_low_temperatures(weather_data)
    print(f"Highest Temperature Recorded: {max_temp}°C")
    print(f"Lowest Temperature Recorded: {min_temp}°C")
    
    # Count the number of days with temperatures above 30°C
    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of Days with Temperatures Above 30°C: {days_above_30}")
    
    # Compute the average humidity
    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity:.2f}%")
