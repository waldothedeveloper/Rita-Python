print("Bookstore Calculator")

book_price = float(input("Price of book(s): "))
tax_percent = float(input("Tax Percent: "))
tax_amount = 0
total_amount = 0

tax_amount += book_price * (tax_percent / 100)
total_amount = book_price + tax_amount

print("------------")
print("Price:", book_price)
print("Tax percent:", tax_percent)
print("Tax amount:", round(tax_amount, 2))
print("Total amount:", round(total_amount, 2))
