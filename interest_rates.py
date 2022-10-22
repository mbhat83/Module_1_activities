prinicple = 103208.56
interest_rates = [.103, .607, .099, .10]
total_interest = 0.0


for rate in interest_rates:
    interest = rate * prinicple
    total_interest = total_interest + interest
    print("Your interest will be: ", interest)
print("The total interest is: ", total_interest)