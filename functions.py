# Function to calculate the discounted price
def calculate_discounted_price(price, discount_percent):
  if discount_percent >= 20:
    discounted_amount = (price * discount_percent) / 100
    discounted_price = price - discounted_amount
    print(f"The discounted price is: {discounted_price}")
  
  else:
      print(f"No discount applied. The price remains: {price}")
    


calculate_discounted_price(2000,25)
# output
# The discounted price is: 1500.0
calculate_discounted_price(2000,15)
# output
# No discount applied. The price remains: 2000



# Question two
# Function to calculate the discounted price
def calculate_discounted_price(price, discount_percent):
  if discount_percent > 100:
    raise ValueError("Discount percentage cannot be greater than 100.")
  else:
    discounted_amount = (price * discount_percent) / 100
    return price - discounted_amount

# Takes original price from user
price = int(input("Enter the price: "))

while True:
  # Takes the discount_percent from the user
  discount_percent = input("Enter the percentage discount: ")

  # Check if discount_percent is a valid integer between 0 and 100
  if discount_percent.isdigit():
    discount_percent = int(discount_percent)
    if 0 <= discount_percent <= 100:
      break
    else:
      print("Please enter a discount percentage between 0 and 100.")
  else:
    print("Invalid input. Please enter a valid integer.")

# Apply the discount if it's greater than 0%
if discount_percent >= 20:
  final_price = calculate_discounted_price(price, discount_percent)
  print(f"The discounted price is: {final_price}")
else:
  print(f"No discount applied. The price remains: {price}")
  
  
# #   output  when price is 2000 and percentage discount is 25
# Enter the price: 2000
# Enter the percentage discount: 25
# The discounted price is: 1500.0

# # output
# Enter the price: 2000
# Enter the percentage discount: 15
# No discount applied. The price remains: 2000