exitMenu1 = False
exitMenu2 = False
exitMenu3 = False
exitMenu4 = False
exitMenu5 = False
exitMenu6 = False
exitMenu7 = False
exitMenu8 = False
Bill = False
foodinput = []
quantity = []
totalPrice = []
Price: {
    "Fish&Chips": 190000,
    "Pizza": 250000,
    "Burger": 90000,
    "Peking Duck": 350000,
    "Kung pao Chicken": 65000,
    "Chicken Dumplings": 35000,
    "Lemon tea": 15000,
    "Avocado juice": 30000,
    "Orange juice": 25000,
    "Americano": 25000,
    "Hot tea": 8000,
    "Jasmine tea": 35000
    }
for i in range(len(foodinput)):
   if foodinput[i] in Price.keys():
      n = Price[foodInput[i]] * quantity[i]
      totalPrice.append(n)

while exitMenu1 == False:
    print("___________________________________")
    print("|    Welcome to WxA Restaurant    |")
    print("-----------------------------------")
    username = input("Enter your name:")
    if(username == ""):
        print("Please answer seriously")
    else:
        while exitMenu2 == False:
            print("Hi, " + username)
            for i in range(len(foodinput)):
                print(str(quantity[i]) + "x "+ str(foodinput[i]))
            menu = input("Press enter to continue")
            exitMenu3 = False
            exitMenu6 = False
            print("   Menu   ")
            print("__________")
            print("|1.Foods |")
            print("|2.Drinks|")
            print("|3.Back  |")
            print("----------")
            menu2 = input("choose the number 1-3:")
            if(menu2 == "1"):
                while exitMenu3 == False:
                    exitMenu4 = False
                    exitMenu5 = False
                    print("    Menu    ")
                    print("____________")
                    print("|1.Western |")
                    print("|2.Asian   |")
                    print("|3.Back    |")
                    print("------------")
                    menu2a = input("choose the number 1-3:")
                    if(menu2a == "1"):
                        print("     Menu     ")
                        print("______________")
                        print("|1.Fish&Chips|")
                        print("|2.Pizza     |")
                        print("|3.Burger    |")
                        print("|4.Back      |")
                        print("--------------")
                        menu2aa = input("choose the number 1-4:")
                        if(menu2aa == "1"):
                            quantitya1 = input("Quantity:")
                            quantity.append(quantitya1)
                            foodinput.append("Fish&Chips")
                            for x in foodinput:
                                print(x)
                            print("You have added Fish&Chips")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera1 = input("Choose the number 1-2:")
                            if(ordera1 == "1"):
                                Bill = True
                            if(ordera1 == "2"):
                                exitMenu2 = True
                        if(menu2aa == "2"):
                            quantitya2 = input("Quantity:")
                            quantity.append(quantitya2)
                            foodinput.append("Pizza")
                            for x in foodinput:
                                print(x)
                            print("You have added Pizza")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera2 = input("Choose the number 1-2:")
                            if(ordera2 == "1"):
                                Bill = True
                            if(ordera2 == "2"):
                                exitMenu2 = True
                        if(menu2aa == "3"):
                            quantitya3 = input("Quantity:")
                            quantity.append(quantitya3)
                            foodinput.append("Burger")
                            for x in foodinput:
                                print(x)
                            print("You have added Burger")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera3 = input("Choose the number 1-2:")
                            if(ordera3 == "1"):
                                Bill = True
                            if(ordera3 == "2"):
                                exitMenu2 = True
                        if(menu2aa == "4"):
                            exitMenu4 = True
                        
                    if(menu2a == "2"):
                        print("         Menu         ")
                        print("______________________")
                        print("|1.Peking Duck       |")
                        print("|2.Kung pao Chicken  |")
                        print("|3.Chicken Dumplings |")
                        print("|4.Back              |")
                        print("----------------------")
                        menu2ab = input("choose the number 1-4:")
                        if(menu2ab == "1"):
                            quantitya4 = input("Quantity:")
                            quantity.append(quantitya4)
                            foodinput.append("Peking Duck")
                            for x in foodinput:
                                print(x)
                            print("You have added Peking Duck")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera4 = input("Choose the number 1-2:")
                            if(ordera4 == "1"):
                                Bill = True
                            if(ordera4 == "2"):
                                exitMenu2 = True
                        if(menu2ab == "2"):
                            quantitya5 = input("Quantity:")
                            quantity.append(quantitya5)
                            foodinput.append("Kung pao Chicken")
                            for x in foodinput:
                                print(x)
                            print("You have added Kung pao Chicken")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera5 = input("Choose the number 1-2:")
                            if(ordera5 == "1"):
                                Bill = True
                            if(ordera5 == "2"):
                                exitMenu2 = True
                        if(menu2ab == "3"):
                            quantitya6 = input("Quantity:")
                            quantity.append(quantitya6)
                            foodinput.append("Chicken Dumplings")
                            for x in foodinput:
                                print(x)
                            print("You have added Chicken Dumplings")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            ordera6 = input("Choose the number 1-2:")
                            if(ordera6 == "1"):
                                Bill = True
                            if(ordera6 == "2"):
                                exitMenu2 = True
                        if(menu2ab == "4"):
                            exitMenu5 = True
                    if(menu2a == "3"):
                        exitMenu3 = True
            if(menu2 == "2"):
                while exitMenu6 == False:
                    exitMenu7 = False
                    exitMenu8 = False
                    print("   Menu   ")
                    print("__________")
                    print("|1.Cold  |")
                    print("|2.Hot   |")
                    print("|3.Back  |")
                    print("----------")
                    menu2b = input("choose the number 1-3:")
                    if(menu2b == "1"):
                        print("       Menu       ")
                        print("__________________")
                        print("|1.Lemon tea     |")
                        print("|2.Avocado juice |")
                        print("|3.Orange juice  |")
                        print("|4.Back          |")
                        print("------------------")
                        menu2ba = input("choose the number 1-4:")
                        if(menu2ba == "1"):
                            quantityb1 = input("Quantity:")
                            quantity.append(quantityb1)
                            foodinput.append("Lemon tea")
                            for x in foodinput:
                                print(x)
                            print("You have added Lemon tea")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb1 = input("Choose the number 1-2:")
                            if(orderb1 == "1"):
                                Bill = True
                            if(orderb1 == "2"):
                                exitMenu2 = True
                        if(menu2ba == "2"):
                            quantityb2 = input("Quantity:")
                            quantity.append(quantityb2)
                            foodinput.append("Avocado juice")
                            for x in foodinput:
                                print(x)
                            print("You have added Avocado juice")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb2 = input("Choose the number 1-2:")
                            if(orderb2 == "1"):
                                Bill = True
                            if(orderb2 == "2"):
                                exitMenu2 = True
                        if(menu2ba == "3"):
                            quantityb3 = input("Quantity:")
                            quantity.append(quantityb3)
                            foodinput.append("Orange juice")
                            for x in foodinput:
                                print(x)
                            print("You have added Orange juice")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb3 = input("Choose the number 1-2:")
                            if(orderb3 == "1"):
                                Bill = True
                            if(orderb3 == "2"):
                                exitMenu2 = True
                        if(menu2ba == "4"):
                            exitMenu7 = True
                    if(menu2b == "2"):
                        print("      Menu      ")
                        print("________________")
                        print("|1.Americano   |")
                        print("|2.Hot tea     |")
                        print("|3.Jasmine tea |")
                        print("|4.Back        |")
                        print("----------------")
                        menu2bb = input("choose the number 1-4:")
                        if(menu2bb == "1"):
                            quantityb4 = input("Quantity:")
                            quantity.append(quantityb4)
                            foodinput.append("Americano")
                            for x in foodinput:
                                print(x)
                            print("You have added Americano")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb4 = input("Choose the number 1-2:")
                            if(orderb4 == "1"):
                                Bill = True
                            if(orderb4 == "2"):
                                exitMenu2 = True
                        if(menu2bb == "2"):
                            quantityb5 = input("Quantity:")
                            quantity.append(quantityb5)
                            foodinput.append("Hot tea")
                            for x in foodinput:
                                print(x)
                            print("You have added Hot tea")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb5 = input("Choose the number 1-2:")
                            if(orderb5 == "1"):
                                Bill = True
                            if(orderb5 == "2"):
                                exitMenu2 = True
                        if(menu2bb == "3"):
                            quantityb6 = input("Quantity:")
                            quantity.append(quantityb6)
                            foodinput.append("Jasmine tea")
                            for x in foodinput:
                                print(x)
                            print("You have added Jasmine tea")
                            print("What do you want to do next")
                            print("1. Bill")
                            print("2. Main Menu")
                            orderb6 = input("Choose the number 1-2:")
                            if(orderb6 == "1"):
                                Bill = True
                            if(orderb6 == "2"):
                                exitMenu2 = True
                        if(menu2bb == "4"):
                            exitMenu8 = True
                    if(menu2b == "3"):
                        exitMenu6 = True
            if(menu == "3"):
                exitMenu2 = True
while Bill == False:
    print("____________________________________")
    print("|          WxA Restaurant          |")
    print("------------------------------------")
    print("Hi, " + username)
    for i in range(len(foodinput)):
        print(str(quantity[i]) + "x "+ str(foodinput[i]) + str(totalPrice[i]))
        print("______________________________________________________________")
        print("Total:                                          Rp."+totalPrice)
        print("  Order accepted please go to the cashire to pay. Thank you.  ")