#Shopping Bill Calculator
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} {item}(s)")
print(f"The amount you have to pay: ${total}")
