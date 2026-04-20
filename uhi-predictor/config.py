#
# This file contains the fixed city-level features and application constants.

CITIES = {
    "Mumbai": { "State": "Maharashtra", "urban": (19.07, 72.87), "rural": (19.25, 72.65), "Elevation": 14, "Population Density": 20667, "Energy Consumption": 3200, "AQI": 147, "Urban Greenness Ratio": 18, "Annual Rainfall": 2167 },
    "Delhi": { "State": "Delhi", "urban": (28.63, 77.21), "rural": (28.90, 76.85), "Elevation": 216, "Population Density": 11320, "Energy Consumption": 3800, "AQI": 168, "Urban Greenness Ratio": 12, "Annual Rainfall": 797 },
    "Pune": { "State": "Maharashtra", "urban": (18.52, 73.85), "rural": (18.70, 73.60), "Elevation": 560, "Population Density": 5600, "Energy Consumption": 2800, "AQI": 98, "Urban Greenness Ratio": 24, "Annual Rainfall": 722 },
    "Chennai": { "State": "Tamil Nadu", "urban": (13.08, 80.27), "rural": (13.30, 79.95), "Elevation": 6, "Population Density": 7088, "Energy Consumption": 2600, "AQI": 112, "Urban Greenness Ratio": 21, "Annual Rainfall": 1400 },
    "Kolkata": { "State": "West Bengal", "urban": (22.57, 88.36), "rural": (22.85, 88.05), "Elevation": 9, "Population Density": 24306, "Energy Consumption": 2400, "AQI": 135, "Urban Greenness Ratio": 19, "Annual Rainfall": 1582 },
    "Hyderabad": { "State": "Telangana", "urban": (17.38, 78.48), "rural": (17.60, 78.20), "Elevation": 542, "Population Density": 6100, "Energy Consumption": 2900, "AQI": 105, "Urban Greenness Ratio": 22, "Annual Rainfall": 812 },
    "Bengaluru": { "State": "Karnataka", "urban": (12.97, 77.59), "rural": (13.20, 77.30), "Elevation": 920, "Population Density": 4381, "Energy Consumption": 3100, "AQI": 88, "Urban Greenness Ratio": 38, "Annual Rainfall": 970 },
    "Ahmedabad": { "State": "Gujarat", "urban": (23.02, 72.57), "rural": (23.25, 72.30), "Elevation": 53, "Population Density": 9000, "Energy Consumption": 3400, "AQI": 152, "Urban Greenness Ratio": 10, "Annual Rainfall": 782 },
    "Jaipur": { "State": "Rajasthan", "urban": (26.91, 75.79), "rural": (27.10, 75.55), "Elevation": 431, "Population Density": 6900, "Energy Consumption": 2700, "AQI": 130, "Urban Greenness Ratio": 9, "Annual Rainfall": 650 },
    "Nagpur": { "State": "Maharashtra", "urban": (21.14, 79.08), "rural": (21.35, 78.85), "Elevation": 310, "Population Density": 4600, "Energy Consumption": 2500, "AQI": 95, "Urban Greenness Ratio": 28, "Annual Rainfall": 1205 },
    "Lucknow": { "State": "Uttar Pradesh", "urban": (26.84, 80.94), "rural": (27.05, 80.70), "Elevation": 123, "Population Density": 6500, "Energy Consumption": 2600, "AQI": 158, "Urban Greenness Ratio": 20, "Annual Rainfall": 910 },
    "Bhopal": { "State": "Madhya Pradesh", "urban": (23.25, 77.41), "rural": (23.45, 77.18), "Elevation": 527, "Population Density": 4700, "Energy Consumption": 2300, "AQI": 92, "Urban Greenness Ratio": 31, "Annual Rainfall": 1146 },
    "Patna": { "State": "Bihar", "urban": (25.59, 85.13), "rural": (25.75, 84.90), "Elevation": 53, "Population Density": 6800, "Energy Consumption": 2100, "AQI": 165, "Urban Greenness Ratio": 14, "Annual Rainfall": 1130 },
    "Thiruvananthapuram": { "State": "Kerala", "urban": (8.52, 76.93), "rural": (8.70, 76.75), "Elevation": 10, "Population Density": 4400, "Energy Consumption": 2200, "AQI": 65, "Urban Greenness Ratio": 45, "Annual Rainfall": 1800 },
    "Bhubaneswar": { "State": "Odisha", "urban": (20.29, 85.82), "rural": (20.45, 85.60), "Elevation": 45, "Population Density": 3100, "Energy Consumption": 1900, "AQI": 98, "Urban Greenness Ratio": 28, "Annual Rainfall": 1540 },
    "Ranchi": { "State": "Jharkhand", "urban": (23.34, 85.30), "rural": (23.55, 85.10), "Elevation": 651, "Population Density": 2900, "Energy Consumption": 1800, "AQI": 115, "Urban Greenness Ratio": 33, "Annual Rainfall": 1380 },
    "Raipur": { "State": "Chhattisgarh", "urban": (21.25, 81.62), "rural": (21.45, 81.40), "Elevation": 298, "Population Density": 4400, "Energy Consumption": 2000, "AQI": 120, "Urban Greenness Ratio": 25, "Annual Rainfall": 1280 },
    "Guwahati": { "State": "Assam", "urban": (26.14, 91.73), "rural": (26.35, 91.50), "Elevation": 55, "Population Density": 4400, "Energy Consumption": 1800, "AQI": 95, "Urban Greenness Ratio": 34, "Annual Rainfall": 1630 },
    "Shimla": { "State": "Himachal Pradesh", "urban": (31.10, 77.17), "rural": (31.30, 77.00), "Elevation": 2276, "Population Density": 800, "Energy Consumption": 1200, "AQI": 45, "Urban Greenness Ratio": 65, "Annual Rainfall": 1450 },
    "Srinagar": { "State": "Jammu & Kashmir", "urban": (34.08, 74.79), "rural": (34.30, 74.60), "Elevation": 1585, "Population Density": 4000, "Energy Consumption": 1600, "AQI": 75, "Urban Greenness Ratio": 42, "Annual Rainfall": 720 },
    "Dehradun": { "State": "Uttarakhand", "urban": (30.31, 78.03), "rural": (30.50, 77.85), "Elevation": 435, "Population Density": 3000, "Energy Consumption": 1500, "AQI": 85, "Urban Greenness Ratio": 50, "Annual Rainfall": 2073 },
    "Visakhapatnam": { "State": "Andhra Pradesh", "urban": (17.68, 83.21), "rural": (17.90, 83.10), "Elevation": 45, "Population Density": 3500, "Energy Consumption": 2100, "AQI": 95, "Urban Greenness Ratio": 25, "Annual Rainfall": 1000 },
    "Itanagar": { "State": "Arunachal Pradesh", "urban": (27.09, 93.62), "rural": (27.20, 93.50), "Elevation": 320, "Population Density": 400, "Energy Consumption": 800, "AQI": 35, "Urban Greenness Ratio": 60, "Annual Rainfall": 2500 },
    "Chandigarh": { "State": "Chandigarh", "urban": (30.73, 76.77), "rural": (30.85, 76.60), "Elevation": 321, "Population Density": 9252, "Energy Consumption": 2200, "AQI": 90, "Urban Greenness Ratio": 38, "Annual Rainfall": 1100 },
    "Panaji": { "State": "Goa", "urban": (15.49, 73.82), "rural": (15.60, 73.70), "Elevation": 7, "Population Density": 1020, "Energy Consumption": 1500, "AQI": 60, "Urban Greenness Ratio": 45, "Annual Rainfall": 2900 },
    "Gurugram": { "State": "Haryana", "urban": (28.45, 77.02), "rural": (28.60, 76.80), "Elevation": 220, "Population Density": 4200, "Energy Consumption": 3200, "AQI": 180, "Urban Greenness Ratio": 8, "Annual Rainfall": 714 },
    "Leh": { "State": "Ladakh", "urban": (34.15, 77.57), "rural": (34.30, 77.40), "Elevation": 3524, "Population Density": 50, "Energy Consumption": 500, "AQI": 30, "Urban Greenness Ratio": 5, "Annual Rainfall": 100 },
    "Imphal": { "State": "Manipur", "urban": (24.81, 93.93), "rural": (24.95, 93.80), "Elevation": 786, "Population Density": 640, "Energy Consumption": 900, "AQI": 45, "Urban Greenness Ratio": 40, "Annual Rainfall": 1400 },
    "Shillong": { "State": "Meghalaya", "urban": (25.57, 91.89), "rural": (25.70, 91.70), "Elevation": 1525, "Population Density": 340, "Energy Consumption": 1000, "AQI": 40, "Urban Greenness Ratio": 50, "Annual Rainfall": 2200 },
    "Aizawl": { "State": "Mizoram", "urban": (23.73, 92.71), "rural": (23.90, 92.60), "Elevation": 1132, "Population Density": 250, "Energy Consumption": 700, "AQI": 35, "Urban Greenness Ratio": 55, "Annual Rainfall": 2500 },
    "Kohima": { "State": "Nagaland", "urban": (25.67, 94.10), "rural": (25.80, 94.00), "Elevation": 1444, "Population Density": 200, "Energy Consumption": 600, "AQI": 30, "Urban Greenness Ratio": 60, "Annual Rainfall": 2000 },
    "Ludhiana": { "State": "Punjab", "urban": (30.90, 75.85), "rural": (31.10, 75.70), "Elevation": 244, "Population Density": 8000, "Energy Consumption": 2800, "AQI": 120, "Urban Greenness Ratio": 12, "Annual Rainfall": 700 },
    "Gangtok": { "State": "Sikkim", "urban": (27.33, 88.61), "rural": (27.50, 88.50), "Elevation": 1650, "Population Density": 250, "Energy Consumption": 600, "AQI": 25, "Urban Greenness Ratio": 65, "Annual Rainfall": 3800 },
    "Agartala": { "State": "Tripura", "urban": (23.83, 91.28), "rural": (24.00, 91.10), "Elevation": 12, "Population Density": 3000, "Energy Consumption": 1100, "AQI": 55, "Urban Greenness Ratio": 40, "Annual Rainfall": 2200 },
    "Port Blair": { "State": "Andaman & Nicobar", "urban": (11.62, 92.72), "rural": (11.80, 92.60), "Elevation": 16, "Population Density": 400, "Energy Consumption": 500, "AQI": 25, "Urban Greenness Ratio": 70, "Annual Rainfall": 3100 },
    "Puducherry": { "State": "Puducherry", "urban": (11.94, 79.80), "rural": (12.10, 79.60), "Elevation": 3, "Population Density": 2500, "Energy Consumption": 1200, "AQI": 60, "Urban Greenness Ratio": 30, "Annual Rainfall": 1300 },
    "Kavaratti": { "State": "Lakshadweep", "urban": (10.56, 72.64), "rural": (10.70, 72.50), "Elevation": 1, "Population Density": 1600, "Energy Consumption": 300, "AQI": 20, "Urban Greenness Ratio": 50, "Annual Rainfall": 1600 },
    "Daman": { "State": "Dadra and Nagar Haveli and Daman and Diu", "urban": (20.39, 72.83), "rural": (20.60, 72.70), "Elevation": 5, "Population Density": 2000, "Energy Consumption": 900, "AQI": 70, "Urban Greenness Ratio": 25, "Annual Rainfall": 2000 }
}

SEVERITY_LABELS = {0: "None", 1: "Mild", 2: "Moderate", 3: "Severe"}
SEVERITY_COLORS = {
    "None":     "#06b6d4",
    "Mild":     "#22c55e",
    "Moderate": "#f59e0b",
    "Severe":   "#dc2626"
}

# Feature order — must match exactly between pipeline.py and Krishna's Colab training
FEATURE_COLUMNS = [
    "Temperature",
    "Elevation",
    "Population Density",
    "Energy Consumption",
    "AQI",
    "Urban Greenness Ratio",
    "Wind Speed",
    "Humidity",
    "Annual Rainfall",
]
