import csv
import random

# Create a list of 50 random Indian names
names = ["Rahul", "Priya", "Amit", "Anjali", "Rohit", "Suresh", "Geeta", "Vikas", "Neha", "Rakesh", "Sunil", "Anita", "Rajesh", "Kiran", "Sandeep", "Geeta", "Vikram", "Sunita", "Naveen", "Ritu", "Vijay", "Kavita", "Anil", "Smita", "Rajeev", "Rekha", "Deepak", "Manju", "Ajay", "Chitra", "Manoj", "Jyoti", "Ramesh", "Shashi", "Vinod", "Alka", "Suresh", "Kamini", "Rakesh", "Meena", "Sanjay", "Anju", "Pawan", "Neeraj", "Sunil", "Rita", "Ajay"]

# Create a list of lists, where each sublist represents the number of times traveled in each month
travel_data = []
for i in range(50):
    row = []
    for j in range(12):
        row.append(random.randint(0, 3))
    travel_data.append(row)

# Create a CSV writer object
with open("travel_data_50.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Name"] + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    # Write the data rows
    for i in range(len(names)):
        writer.writerow([names[i]] + travel_data[i])

