#SHIPPING PRICE CALCULATOR
name = input("Enter your name: ")
frequent_customers = ["Juan", "Pedro", "Robert", "Ivan"]
shipping_weight = int(input("Enter the weight of your package in kg:  "))

#Costs
cost_1kg = 5
cost_1_to_5kg = 10
cost_more_5kg = 20

def shipping_calculation(name, weight):
    is_frequent_customer = name in frequent_customers

    if weight <= 1:
        price = cost_1kg
    elif weight <= 5:
        price = cost_1_to_5kg
    else:
        price = cost_more_5kg
    
    if is_frequent_customer:
        print(f"Welcome back {name}")
        discount = price * 0.20
        final_price = price - discount
        print(f"As a frequent customer, you have a 20% discount")
    else:
        final_price = price

    print(f"The total shipping cost is: {final_price} euros")

shipping_calculation(name, shipping_weight)
