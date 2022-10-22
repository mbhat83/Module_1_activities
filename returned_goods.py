def process_claims(claims):
    total_claims = sum(claims)
    total_payout = total_claims *.30
    return total_payout
    
    
weekly_claims =  [5000,1000,8000,10000,3000,3500]

Total_insurance_payout = process_claims(weekly_claims)
print("The total insurance payout is:",Total_insurance_payout)




    