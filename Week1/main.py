# variable - names should be meaningful

# x represents my favorite number
x = 42

my_favorite_number = 42

print(my_favorite_number)

my_favorite_number = 7

print(my_favorite_number)

#wage_per_hour = 20
wage_per_hour = float(input("Please enter your hourly wage"))
hours_worked_per_week = float(input("Please enter how any hours you worked this week"))

weekly_pay = wage_per_hour * hours_worked_per_week

print("Your weekly pay is: $", weekly_pay)

taxes_owed = weekly_pay * .12

print("You will owe: $", taxes_owed, "in taxes")

net_pay = weekly_pay - taxes_owed

print("Your take home pay is: $", net_pay)


taxes_as_percentage_of_income = taxes_owed / weekly_pay * 100

print("You pay about", taxes_as_percentage_of_income, "percent in taxes")

# order of operations still applies in python
# 9 / 3(3) is really 9 / 3 * 3
some_mystery_value = 9 / 3 * 3
