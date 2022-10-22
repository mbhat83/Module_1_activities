import csv
from pathlib import Path
from tkinter import W

equity_funding = [
    {"Company": "CryptoVisors", "Amount": 200000, "Series": "A"},
    {"Company": "Flutterwave", "Amount": 65000000, "Series": "D"},
    {"Company": "nCino", "Amount": 80000000, "Series": "D"},
    {"Company": "Privacy.com", "Amount": 10000000, "Series": "B"},
]

big_raisers = []
for equity in equity_funding:
    if equity["Amount"] >= 50000000:
        big_raisers.append(equity)
        print(big_raisers)

header = ["Company", "Amount", "Series"]
csvpath = Path("my_equity_rounds.csv")
print("writing the data to csv file")

with open(csvpath, "w") as csvfile:
    cswriter = csv.writer(csvfile, delimiter=",")
    cswriter.writerow(header)
    for item in big_raisers:
       cswriter.writerow(item.value())

