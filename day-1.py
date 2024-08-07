# print('Welcome to the band name generator.')
# city = input('Whats the name of the city you grew up in?\n')
# pet = input('What was the name of your first pet?\n')
# print('Your band name is ' + city + ' ' + pet)


# print('Welcome to the tip calculator!')
# bill_amount = float(input('What was the total bill? €'))
# tip = int(input('How much tip would you like to give? 10, 12 or 15? '))
# num_people = int(input('How many people to split the bill? '))
# tip_calc = tip / 100
# final_price = round((bill_amount * tip_calc + bill_amount) / num_people, 2)
# print(f'Each person should pay €{final_price}')

# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M, or L: ')
# pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
# pizza_cost = 0
# pepperoni_cost = 0
# extra_cheese_cost = 0


# if size == "S":
#     if pepperoni == "Y":
#         pepperoni_cost = 2
#     pizza_cost = 15
# elif size == "M":
#     if pepperoni == "Y":
#         pepperoni_cost = 3
#     pizza_cost = 20
# elif size == "L":
#     if pepperoni == "Y":
#         pepperoni_cost = 3
#     pizza_cost = 25

# if extra_cheese == "Y":
#     extra_cheese_cost = 1


# final_bill = pizza_cost + pepperoni_cost + extra_cheese_cost
# print(f'Your final bill is: €{final_bill}')


print("Welcome to Treasure Island. Your mission is to find the treasure")
choice_1 = input("You come to a fork in the road at the stage of your journey. Do you go left at the fork or right? Type 'left' or 'right' to continue: ").lower()

if choice_1 == "left":
    choice_2 = input("After traveling the left path you come to a black lake. Do you swim across the lake or wait? Type 'swim' or 'wait' to continue:  ").lower()
    if choice_2 == "wait":
        choice_3 = input("After a short time waiting you notice 3 doors appear behind you, one blue, one red, and one yellow. Which door do you choose to enter? Type 'blue', 'red' or 'yellow' to continue: ").lower()
        if choice_3 == "blue":
            print("You have been eaten by a wolf! GAME OVER")
        elif choice_3 == "red":
            print("You have been burnt alive! GAME OVER")
        elif choice_3 == "yellow":
            print("You have found the Treasure! YOU WIN")
        else:
            print("Invalid selection! Please enter 'blue', 'red' or 'yellow'")
            choice_3
    else:
        print("You have been attacked by a crocodile! GAME OVER")
else:
    print("You fell into a hole! GAME OVER")
