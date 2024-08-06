# print('Welcome to the band name generator.')
# city = input('Whats the name of the city you grew up in?\n')
# pet = input('What was the name of your first pet?\n')
# print('Your band name is ' + city + ' ' + pet)


print('Welcome to the tip calculator!')
bill_amount = float(input('What was the total bill? €'))
tip = int(input('How much tip would you like to give? 10, 12 or 15? '))
num_people = int(input('How many people to split the bill? '))
tip_calc = tip / 100
final_price = bill_amount * tip_calc + bill_amount / num_people
print(f'Each person should pay €{final_price}')