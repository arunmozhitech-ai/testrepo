#Define The Menu in restaurant
menu={
    'pizza':50,
    'pasta':40,
    'coffee':30,
    'french fries':80,
    'momos':120,
    'burger':150,
}
a=input("")

#greet
print("Welcome to Arun Restaurant")
print("pizza Rs 50\npasta Rs 40\ncoffee Rs 30\nfrench fries Rs 80\nmomos Rs 120\nburger Rs 150")

order_total=0
#80+70=150

item_1=input("Enter the name of the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]  #0+50
    print(f"your item {item_1} has been added to your order")
else:
    print(f"your order {item_1} not available yet")

another_order=input("Do you want to another item (yes/no)")
if another_order=="yes":
    item_2=input("input the name of second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print (f"your item {item_2} has been added to your order")
else:
    print(f"your order {item_2} not available yet")
print(f"total amount of items to pay is {order_total}")