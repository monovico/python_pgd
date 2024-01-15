number_of_pizzas = eval(input("how many pizzas do you want?"))
cost_per_pizza = eval(input("how much does each pizza cost?"))

subtotal = number_of_pizzas * cost_per_pizza
tax_rate = (1.25+9.00)/100
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print("The total cost is $",total)
print("This includes $" , subtotal)
print("$" , sales_tax, "in sales tax.")