#Shopping online sim
# Playing with lists
# pascode 4321
import time

#INITIATION/AUTHENTICATION

def login():
    print("Welcome to Bamazon\n")
    username = input("Enter Username: ")

    while True:
        passcode = int(input("Enter passcode: "))
        if passcode == 4321:
            print(f"Hi {username} logging you in...")
            for i in range(3):
                print(".")
            time.sleep(2)
            break
        else:
            print("Invalid passcode")
    return username

def shopping_cart(cart_items, username):
    
    
    while True:
        for i in range(20):
            print(".")

        print("Here are the items of your order-------------")
        print(*cart_items, sep="\n")
        choice = int(input("Press 1 to return to return to shopping center or 2 to clear the cart \n>>  "))
        if choice == 1:
            shopping_center(username)
            break
        elif choice == 2:
            cart_items.clear()
            print("All items have been cleared!")
        else:
            print("Invalid, please enter in a number")

def shopping_center(username):
    cart = []
    items = ["[1]Fish", "[2]Chicken", "[3]Shoes", "[4]Pillow"]
    cart_num = 0

    topuser_info = f"{username}\t\t\t(CART:{cart_num})"
    main_ui = "-------------Todays Items----------------\n"

    while True:
        for i in range(20):
            print(".")

        topuser_info = f"{username}\t\t\t(CART:{cart_num})"

        print(topuser_info)
        print(main_ui)
        print(*items, sep="\t\t")
        print("""\nEnter number associated to the left of the item to add to cart
    or press 0 to access cart""")

        choice = int(input("Enter item number: "))
        if choice == 1:
            cart.append(items[0])
            cart_num += 1
            print(f"Item has been added to cart successfully")
            time.sleep(1)
        elif choice == 2:
            cart.append(items[1])
            cart_num += 1
            print(f"Item has been added to cart successfully")
            time.sleep(1)
        elif choice == 3:
            cart.append(items[2])
            cart_num += 1
            print(f"Item has been added to cart successfully")
            time.sleep(1)
        elif choice == 4:
            cart.append(items[3])
            cart_num += 1
            print(f"Item has been added to cart successfully")
            time.sleep(1)
        elif choice == 0:
            for i in range(10):
                print(".")
            time.sleep(2)
            shopping_cart(cart, username)
            break
        else:
            print("Invalid, please enter in a number")
    return cart


def main():
    username = login()
    shopping_center(username)

main()