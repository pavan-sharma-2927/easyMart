
from datetime import datetime
vegetable={}
stationary={}
beauty_product={}
foods={}
quantity_foods={}
quantity_vegetable={}
quantity_stationary={}
quantity_beauty_product={}
    
def add_items():
    with open("D:\\desktop\\py_learn\\ZEXERCISE\\shop\\catogary_list.txt", "w+") as catogary_items:
        try:
            print(".............Product Catogary.............")
            print("1: foods\n2: vegetables\n3: stationary products\n4: Beauty & Personal product")
            catogary_items=int(input("Enter catogary: "))
            name=str(input("Enter Name of items: "))
            price=float(input("Enter price of items: \u20B9 "))
            if catogary_items==1:
                quantity=float(input("Enter Quantity(kg): "))
                foods.update({name:price})
                quantity_foods.update({name:quantity})
            elif catogary_items==2:
                quantity=float(input("Enter Quantity(kg): "))
                vegetable.update({"name":price})
                quantity_vegetable.update({name:quantity})
            elif catogary_items==3:
                quantity=int(input("Enter Quantity(piece): "))
                stationary.update({"name":price}) 
                quantity_stationary.update({name:quantity})
            elif catogary_items==4:
                quantity=int(input("Enter Quantity(piece): "))
                beauty_product.update({"name":price}) 
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
                print(name,"\t\t\u20B9",price,"\t\t",quantity)
        elif catogary_items==2:
            print("...............Vegetable...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in vegetable.items():
                quantity=quantity_vegetable[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity)
        elif catogary_items==3:
            print("..................stationary...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in stationary.items():
                quantity=quantity_stationary[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity)
        elif catogary_items==4:
            print("..................beauty_product...................\n")
            print("Item\t\tPrice\t\tQuantity")
            print("-----------------------------------------")
            for name, price in beauty_product.items():
                quantity=quantity_beauty_product[name]
                print(name,"\t\t\u20B9",price,"\t\t",quantity)
    except Exception as e:
        print(e)
        print(type(e))
    else:
        print("items shows successfully.")

while(True):
    print("================ WELCOME TO S.A.P SHOP ===========")
    print("1: Add items\n2: Sell items\n3: Stock items\n4: Cradit sale")
    try:
        choice=int(input("Enter your choice: " ))
    except ValueError:
        print("please enter valid choice.")
    else:
        if choice==1:
            add_items()
        elif choice==2:
            display_items()
    print("Would you like to continue shoping ?\n1: Press 1 to exit.\t\t\t2: Press any key to continue. : ")
    Exitoption=input("Enter your choice: ")
    if Exitoption==1:
        break
    else:
        pass
        