print('Welcome to Python Pizza Deliveries')
#
user_size = input("Size of your pizza???")
add_pepperoni = input("Do you want pepperoni on your pizza???")
extra_cheese = input("Do you want extra cheese???")
price = {'Large': 25, 'Medium': 20, 'Small': 15}
extra_price = {'pepproni for small pizze': 2, 'pepperoni for large pizza': 3}



if user_size == 'L' and price == 25:
  print("Your bill is $25")
elif user_size == 'L' and add_pepperoni == 'Y':
  print("Your bill is $28")
elif user_size == 'M' and price == 20:
  print("Your bill is $20")
elif user_size == 'S' and price == 15:
  print("Your bill is $15")
else:
  print("Thank you for patronizing us")

