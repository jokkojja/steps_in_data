my_json = {'amount' : 1000000, 'period' : 120, 'percent' : 15, 'type' : 'annuity'} 
def interest_rate_calculation(json) -> float:
    '''Calculates cumulative interest paid on a loan for the specific period. 
    Function receives json with amount, period, percent rate and type of credit.
    Returns float number, which is cumulative interest paid on a loan'''
    amount = json['amount']
    period = json['period']
    percent = json['percent']
    type_of_loan = json['type']
    if period < 12 or amount < 0 or percent < 0: #check data
        print('Incorrect data')
    else:
        if type_of_loan == 'annuity':
            month_interest_rate = percent / 1200
            anuent_coef = (month_interest_rate * (1 + month_interest_rate) \
                           ** period) / (((1 + month_interest_rate) ** period) - 1)#special annuity coeff
            monthly_payment = amount * anuent_coef 
            total = monthly_payment * period
            cumulative_paid_interest = total - amount
            return round(cumulative_paid_interest, 2)
        if type_of_loan == 'diff':
            month_payment_list = []
            temp_amount = amount
            while temp_amount != 0:
                monthly_payment = (temp_amount / period) + (temp_amount * percent / 1200)
                month_payment_list.append(round(monthly_payment, 2))
                temp_amount = temp_amount - (temp_amount / period)
                period -= 1
            total_pay = round(sum(month_payment_list), 2)
            per = total_pay - amount
            return per
ann_rate = interest_rate_calculation(my_json)
print('My json for annuity loan: ', my_json, '\nCumulative interest paid on a loan: ', ann_rate)


my_json = {'amount' : 1000000, 'period' : 120, 'percent' : 15, 'type' : 'diff'} 
diff_rate = interest_rate_calculation(my_json)
print('My json for diff loan: ', my_json, '\nCumulative interest paid on a loan: ', diff_rate)


