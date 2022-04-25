finish = 0
identity1 = input("Please enter your name: ")
print("Good day, " + identity1 + ".")
Daily_Expense = float(input("Please enter your daily expense in IDR: "))
Weekly_Expense = 7 * Daily_Expense
Electrical_Expense = 400000
Water_Utility_Expense = 150000
Internet_Connection_Expense = 500000
Drinking_Gallons_Expense = 250000
Monthly_Expense = ((4 * Weekly_Expense) + (2 * Daily_Expense)) + Electrical_Expense + Water_Utility_Expense + Internet_Connection_Expense + Drinking_Gallons_Expense
Annual_Expense = ((12 * Monthly_Expense) + (5 * Daily_Expense))

Additional_Weekly_Expense = 150000
Traveling_Expense = 6000000



while finish < 1:
    weekend_going_out = input("Do you go out on weekend? Yes or no?\n")
    if weekend_going_out == "Yes":
        Weekly_Expense_yes = Weekly_Expense + Additional_Weekly_Expense
        print("\nThat means you have an additional expense of at least IDR " + str(Additional_Weekly_Expense) + ".")
        print("\nYour weekly expense should be at least IDR " + str(Weekly_Expense_yes) + ".")
    elif weekend_going_out == "yes":
        Weekly_Expense_yes = Weekly_Expense + Additional_Weekly_Expense
        print("\nThat means you have an additional expense of at least IDR " + str(Additional_Weekly_Expense) + ".")
        print("\nYour weekly expense should be at least IDR " + str(Weekly_Expense_yes) + ".")
    elif weekend_going_out == "Yes.":
        Weekly_Expense_yes = Weekly_Expense + Additional_Weekly_Expense
        print("\nThat means you have an additional expense of at least IDR " + str(Additional_Weekly_Expense) + ".")
        print("\nYour weekly expense should be at least IDR " + str(Weekly_Expense_yes) + ".")
    elif weekend_going_out == "yes.":
        Weekly_Expense_yes = Weekly_Expense + Additional_Weekly_Expense
        print("\nThat means you have an additional expense of at least IDR " + str(Additional_Weekly_Expense) + ".")
        print("\nYour weekly expense should be at least IDR " + str(Weekly_Expense_yes) + ".")
    else:
        print("\nThat means you don't have any additional weekly expense.")

    total_weekend_going_out = input("\nHow many times from 1-4, do you go out in weekend(s)?\n")
    if total_weekend_going_out == "1":
        Monthly_Expense_w1 = Monthly_Expense + (1 * Additional_Weekly_Expense)
        print("\nAssuming you'll spend IDR 150000 each time you go out on weekend, that means your total weekend expense")
        print("\nis IDR " + str(Additional_Weekly_Expense) + ".")
        print("\nYour monthly expense should be IDR " + str(Monthly_Expense_w1) + ".")
        Annual_Expense_w1 = 12 * Monthly_Expense_w1 + 5 * Daily_Expense

        total_months_going_out = input("\nHow many times do you travel far in 1 year?\nNone\n1 time\n2 times\n3 times\n")
        if total_months_going_out == "1":
            Annual_Expense_w1_t1 = Annual_Expense_w1 + (1 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(1 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w1_t1) + ".")
        elif total_months_going_out == "2":
            Annual_Expense_w1_t2 = Annual_Expense_w1 + (2 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(2 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w1_t2) + ".")
        elif total_months_going_out == "3":
            Annual_Expense_w1_t3 = Annual_Expense_w1 + (3 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(3 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w1_t3) + ".")
        elif total_months_going_out == "None":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        elif total_months_going_out == "none":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        else:
            print("\nYou entered an invalid response.")


    elif total_weekend_going_out == "2":
        Monthly_Expense_w2 = Monthly_Expense + (2 * Additional_Weekly_Expense)
        print("\nAssuming you'll spend IDR 150000 each time you go out on weekend, that means your total weekend expense")
        print("\nis IDR " + str(2 * Additional_Weekly_Expense) + ".")
        print("\nYour monthly expense should be IDR " + str(Monthly_Expense_w2) + ".")
        Annual_Expense_w2 = 12 * Monthly_Expense_w2 + 5 * Daily_Expense

        total_months_going_out = input("\nHow many times do you travel far in 1 year?\nNone\n1 time\n2 times\n3 times\n")
        if total_months_going_out == "1":
            Annual_Expense_w2_t1 = Annual_Expense_w2 + (1 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(1 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w2_t1) + ".")
        elif total_months_going_out == "2":
            Annual_Expense_w2_t2 = Annual_Expense_w2 + (2 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(2 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w2_t2) + ".")
        elif total_months_going_out == "3":
            Annual_Expense_w2_t3 = Annual_Expense_w2 + (3 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(3 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w2_t3) + ".")
        elif total_months_going_out == "None":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        elif total_months_going_out == "none":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        else:
            print("\nYou entered an invalid response.")

    elif total_weekend_going_out == "3":
        Monthly_Expense_w3 = Monthly_Expense + (3 * Additional_Weekly_Expense)
        print("\nAssuming you'll spend IDR 150000 each time you go out on weekend, that means your total weekend expense")
        print("\nis IDR " + str(3 * Additional_Weekly_Expense) + ".")
        print("\nYour monthly expense should be IDR " + str(Monthly_Expense_w3) + ".")
        Annual_Expense_w3 = 12 * Monthly_Expense_w3 + 5 * Daily_Expense

        total_months_going_out = input("\nHow many times do you travel far in 1 year?\nNone\n1 time\n2 times\n3 times\n")
        if total_months_going_out == "1":
            Annual_Expense_w3_t1 = Annual_Expense_w3 + (1 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(1 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w3_t1) + ".")
        elif total_months_going_out == "2":
            Annual_Expense_w3_t2 = Annual_Expense_w3 + (2 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(2 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w3_t2) + ".")
        elif total_months_going_out == "3":
            Annual_Expense_w3_t3 = Annual_Expense_w3 + (3 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(3 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w3_t3) + ".")
        elif total_months_going_out == "None":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        elif total_months_going_out == "none":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        else:
            print("\nYou entered an invalid response.")


    elif total_weekend_going_out == "4":
        Monthly_Expense_w4 = Monthly_Expense + (4 * Additional_Weekly_Expense)
        print("\nAssuming you'll spend IDR 150000 each time you go out on weekend, that means your total weekend expense")
        print("\nis IDR " + str(4 * Additional_Weekly_Expense) + ".")
        print("\nYour monthly expense should be IDR " + str(Monthly_Expense_w4) + ".")
        Annual_Expense_w4 = 12 * Monthly_Expense_w4 + 5 * Daily_Expense

        total_months_going_out = input("\nHow many times do you travel far in 1 year?\nNone\n1 time\n2 times\n3 times\n")
        if total_months_going_out == "1":
            Annual_Expense_w4_t1 = Annual_Expense_w4 + (1 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(1 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w4_t1) + ".")
        elif total_months_going_out == "2":
            Annual_Expense_w4_t2 = Annual_Expense_w4 + (2 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(2 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w4_t2) + ".")
        elif total_months_going_out == "3":
            Annual_Expense_w4_t3 = Annual_Expense + (3 * Traveling_Expense)
            print("\nAssuming you'll spend IDR 6000000 each time you travel far, that means your total annual expense")
            print("\nis IDR " + str(3 * Traveling_Expense) + ".")
            print("\nYour annual expense should be IDR " + str(Annual_Expense_w4_t3) + ".")
        elif total_months_going_out == "None":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        elif total_months_going_out == "none":
            print("\nThat means you don't have any additional annual expense.")
            print("\nYour annual expense should be IDR " + str(Annual_Expense) + ".")
        else:
            print("\nYou entered an invalid response.")


    elif total_weekend_going_out == "0":
        print("\nThat means you don't have any additional monthly expense")
        print("\nYour monthly expense should be IDR " + str(Monthly_Expense) + ".")

    changes = input("\nDo you want to make any changes?\n Yes or no? ")
    if changes == "Yes":
        finish = finish + 0
    elif changes == "yes":
        finish = finish + 0
    elif changes == "no":
        finish = finish + 1
        print("\nThank you for using this counter.")
    elif changes == "No":
        finish = finish + 1
        print("\nThank you for using this counter")
    else:
        repeat = repeat + 0
        print("\nYou have entered an invalid response. Please try to input your response again.")



print("\nHave a great day, and please try to keep being thrifty.")
