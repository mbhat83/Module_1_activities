accounts = {"Schwab": 2000, "Fidelity": 8000, "Merrill": 3000, "Wells Fargo": 0.01}
print(accounts["Fidelity"])
del accounts["Wells Fargo"]
accounts["sofi"] = 2000
print(accounts)
old_accounts_amounts =[2000, 8000, 3000, 2000]
total_amount = sum(old_accounts_amounts)
new_accounts = {}
new_accounts["Wealthfront"] = total_amount
print(new_accounts)






