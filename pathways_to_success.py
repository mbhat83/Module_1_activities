import csv
from pathlib import Path

data = [
    {
        "first_name": "Jericho",
        "last_name": "Smith",
        "pin": 123
    },
    {
        "first_name": "Samantha",
        "last_name": "Jones",
        "pin": 456
    }
]

header = ["first_name", "last_name", "pin"]

csvpath = Path("my_employees.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write our header row first!
    csvwriter.writerow(header)

    # Then we can write the data rows
    for row in data:
        csvwriter.writerow(row.values())


first_name = "Michelle"
last_name = "Jones"

full_name = first_name + last_name
print(full_name)
print("My name is " + first_name + " " + last_name + ".")