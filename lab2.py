print("Pay Check Calculator")

hours = int(input("Hours worked?\n"))
pay_rate = float(input("Hourly pay rate>\n"))
tax_rate = 18
# getting the gross pay, the tax amount and the take home pay
gross_pay = round(hours * pay_rate, 2)
tax_amount = round(gross_pay * (tax_rate / 100), 2)
take_home_pay = round(gross_pay - tax_amount, 2)

print("Hours worked:", hours)
print("Hourly Pay Rate:", pay_rate)
print("Gross Pay:", gross_pay)
print("Tax Rate:", tax_rate)
print("Tax Amount:", tax_amount)
print("Take Home Pay:", take_home_pay)
