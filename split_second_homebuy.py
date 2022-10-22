def price_this_home(home_price,expected_sale_price,hurdle_rate,holding_months):
    present_value = expected_sale_price / (1 + (hurdle_rate/12)) ** holding_months
    net_present_value = present_value - home_price
    return net_present_value
    

expected_profit = price_this_home(home_price = 100000, expected_sale_price = 120000, hurdle_rate = 0.10,
holding_months = 36)
print(f"excepted profit from this home is:", expected_profit)



