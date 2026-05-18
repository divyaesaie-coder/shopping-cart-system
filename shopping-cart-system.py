#Develop a Python shopping cart system to add items, manage cart items, and calculate total amount.
items = {}      
cart = {}       
while True:
    print("\n1) Add items")
    print("2) Add to cart")
    print("3) Display cart")
    print("4) Total amount")
    print("5) Exit")
    ch = input("Choose: ")
    if ch == "1":
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        if item in items:
            print("Item already exists!")
        else:
            items[item] = price
            print("Item added successfully!")
    if ch=="2":
    	print(items)
    	item=input("Enter the item:")
    	if item in items:
    		qty=int(input("Enter the quantity:"))
    		if item in cart:
    			cart[item]+=qty
    		else:
    			cart[item]=qty
    			print("Added to cart!")
    	else:
    		print("Item not found!!")
    if ch=="3":
    	print(cart)
    if ch=="4":
    	total=0
    	for item,qty in cart.items():
    		total+=items[item]*qty
    		print("Your total amount is:",total)
    if ch=="5":
    	print("Thank you,Bye!!")
    	break
