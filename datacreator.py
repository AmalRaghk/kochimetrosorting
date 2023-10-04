import pandas as pd
import numpy as np

# Create a list of Indian names
indian_names = ["Rahul", "Ajay", "Vijay", "Suresh", "Rakesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh", "Mahesh", "Vikas", "Rajesh", "Ramesh"]

# Create a list of zones
zones = ["North", "South", "East", "West"]

# Create a list of distances for each quarter
q1_distances = np.random.randint(100, 1000, size=50)
q2_distances = np.random.randint(100, 1000, size=50)
q3_distances = np.random.randint(100, 1000, size=50)
q4_distances = np.random.randint(100, 1000, size=50)

# Create a list of quarters
quarters = np.random.randint(1, 5, size=50)

# Create a DataFrame
df = pd.DataFrame({
"id": np.arange(1, 51),
"name": np.random.choice(indian_names, size=50),
"zone": np.random.choice(zones, size=50),
"q1distance": q1_distances,
"q2distance": q2_distances,
"q3distance": q3_distances,
"q4distance": q4_distances,
"quarter": quarters
})

# Calculate the total distance traveled
df["total_distance"] = df["q1distance"] + df["q2distance"] + df["q3distance"] + df["q4distance"]

# Export the DataFrame to a CSV file
df.to_csv("indian_names_with_quarters_different_distances.csv", index=False)
