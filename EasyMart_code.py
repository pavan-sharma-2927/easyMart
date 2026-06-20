vegetable={}
stationary={}
beauty_product={}
foods={}
quantity_foods={}
quantity_vegetable={}
quantity_stationary={}
quantity_beauty_product={}
item_unit={}
    
def add_items():
    with open("D:\\desktop\\py_learn\\ZEXERCISE\\shop\\catogary_list.txt", "w+") as catogary_items:
        try:
            print(".............Product Catogary.............")
            print("1: foods\n2: vegetables\n3: stationary products\n4: Beauty & Personal product")
            catogary_items=int(input("Enter catogary: "))
            name=str(input("Enter Name of items: "))
            print("Enter the unit of item\n1: Kg\t\t2: ltr\n3: meter\t4: piece")
            unit=int(input("Enter unit: "))
            item_unit.update({name:unit})
            price=float(input("Enter price of items: \u20B9") )
            if catogary_items==1:
                quantity=float(input("Enter Quantity: "))
                foods.update({name:price})
                quantity_foods.update({name:quantity})
            elif catogary_items==2:
                quantity=float(input("Enter Quantity: "))
                vegetable.update({name:price})
                quantity_vegetable.update({name:quantity})
            elif catogary_items==3:
                quantity=int(input("Enter Quantity: "))
                stationary.update({name:price}) 
                quantity_stationary.update({name:quantity})
            elif catogary_items==4:
                quantity=int(input("Enter Quantity: "))
                beauty_product.update({name:price}) 
                quantity_beauty_product.update({name:quantity})
            else:
                print("Invalid input.")

        except ValueError:
            print("Enter valid data.")
        else:
            print("Item added successfully.")

def display_items():
    try:
        print("-------------------------------------------")
        print("1: foods\n2: vegetables\n3: stationary products\n4: Beauty & Personal product")
        catogary_items=int(input("Enter catogary: "))
        
        if catogary_items==1:
            print("..................foods...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in foods.items():
                quantity=quantity_foods[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity,"kg")
        elif catogary_items==2:
            print("...............Vegetable...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in vegetable.items():
                quantity=quantity_vegetable[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity,"kg")
        elif catogary_items==3:
            print("..................stationary...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in stationary.items():
                quantity=quantity_stationary[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity,"piece")
        elif catogary_items==4:
            print("..................beauty_product...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in beauty_product.items():
                quantity=quantity_beauty_product[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity,"piece")
        else:
            print("Invalid input.")
    except Exception as e:
        print(e)
        print(type(e))
    else:
        print("items shows successfully.")

def sell_items():
    sold_items=input("Enter item name: ")
    print("price of item is: \u20B9",foods[sold_items])
    sold_quantity=int(input("Enter quantity: "))
    if sold_items in foods:
        if sold_quantity<quantity_foods[sold_items]:
            quantity_foods[sold_items]-=sold_quantity
            print("Total price is: ",foods[sold_items]*sold_quantity)
        else:
            print("out of stock.")
            print(" Available stock is: ",foods[sold_items])
    elif sold_items in vegetable:
        if sold_quantity<quantity_vegetable[sold_items]:
            quantity_vegetable[sold_items]-=sold_quantity
            print("Total price is: ",vegetable[sold_items]*sold_quantity)
        else:
            print("out of stock.")
            print(" Available stock is: ",vegetable[sold_items])
    elif sold_items in stationary:
        if sold_quantity<quantity_stationary[sold_items]:
            quantity_stationary[sold_items]-=sold_quantity
            print("Total price is: ",stationary[sold_items]*sold_quantity)
        else:
            print("out of stock.")
            print(" Available stock is: ",stationary[sold_items])
    elif sold_items in beauty_product:
        if sold_quantity<beauty_product[sold_items]:
            beauty_product[sold_items]-=sold_quantity
            print("Total price is: ",beauty_product[sold_items]*sold_quantity)
        else:
            print("out of stock.")
            print(" Available stock is: ",beauty_product[sold_items])








while(True):
    print("================ WELCOME TO S.A.P SHOP ===========")
    print("1: Add items\n2: display items\n3: Sell items\n4: Stock items\n5: Cradit sale")
    try:
        choice=int(input("Enter your choice: " ))
    except ValueError:
        print("please enter valid choice.")
    else:
        if choice==1:
            add_items()
        elif choice==2:
            display_items()
        elif choice==3:
            sell_items()

    print("Would you like to continue shoping ?\n1: Press 1 to exit.\t\t\t2: Press any key to continue. : ")
    Exitoption=input("Enter your choice: ")
    if Exitoption==1:
        break
    else:
        pass
        