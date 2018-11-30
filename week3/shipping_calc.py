import sys

print("===============================================================")
print("                      Shipping Calculator                      ")
print("===============================================================")


shipping_cost = [5.95, 7.95, 9.95]
shipped = 0
total_cost = 0
cost_of_order = 0


def get_input():
    global cost_of_order
    while True:
        cost_of_order = float(input("What is the cost of items: "))
        if cost_of_order <= 0:
            print("You must enter a positive number greater than zero.Please try again")
        elif cost_of_order > 0:
            break
    return


def check_shipping_cost(number):
    global total_cost
    global shipped
    if number < 30.00:
        total_cost = number + shipping_cost[0]
        shipped = shipping_cost[0]
    elif number >= 30.00 and number <= 49.99:
        total_cost = number + shipping_cost[1]
        shipped = shipping_cost[1]
    elif number >= 50.00 and number <= 74.99:
        total_cost = number + shipping_cost[2]
        shipped = shipping_cost[2]
    elif number >= 75.00:
        total_cost = number + 0
        shipped = "Free"
    return round(total_cost, 2)


def result(func):
    print("Cost of items ordered: ", cost_of_order)
    print("Shipping cost: ", shipped)
    print("Total cost: ", func)
    print("===============================================================")


while True:
    get_input()
    result(check_shipping_cost(cost_of_order))
    print(" ")
    cont = input("Continue? (y/n): ")
    if cont.strip().lower() != "y":
        print("Bye!")
        break
sys.exit()
