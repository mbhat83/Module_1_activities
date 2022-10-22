stock_price = 30
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]
total_dividend_income = 0
for dividend in dividend_yields:
    dividend_income = dividend * stock_price
    total_dividend_income = dividend_income + total_dividend_income
    print("Income from the portfolio produce is:", dividend_income)
print("total dividend income will be:", total_dividend_income)



