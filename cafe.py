# menu={
#     'Pizza':79,
#     'Pasta':60,    
#     'Burger':99,
#     'Salad':70,
#     'Coffee':80,
# }

# print("Welcome To Phool Restaurant")
# print("Pizza:Rs79\nPasta:Rs60\nBurger:Rs99\nSalad:Rs70\nCoffee:Rs80"
#       )

# order_total=0

# item_1=input("Enter the name of item you want to oreder= ")
# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"Your item{item_1} has been added to your order")

# else:
#     print(f"Ordered item{item_1}is not avaialable yet!")

# another_order=input("Do you want to add another item ?(Yes/No) ")

# if another_order=="Yes":
#     item_2=input("Enter the name of second item= ")
#     if item_2 in menu:
#         order_total +=menu[item_2]
#         print(f"Ordered item {item_2} is not avaialable yet!")


# print(f"The total amount of items of to pay is {order_total}")


menu = {
    'Pizza': 79,
    'Pasta': 60,    
    'Burger': 99,
    'Salad': 70,
    'Coffee': 80,
}

print("Welcome To Phool Restaurant")
print("Pizza:Rs79\nPasta:Rs60\nBurger:Rs99\nSalad:Rs70\nCoffee:Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order= ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item ? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is Rs{order_total}")
