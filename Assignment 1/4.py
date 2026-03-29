"""
Project: Len's Slice
Organizing pizza sales data using Python lists.
"""

# --- Make Some Pizzas ---

# 1. Create a list called 'toppings' with the following:
# "pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"
toppings=["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]


# 2. Create a list called 'prices' with the following integer values:
# 2, 6, 1, 3, 2, 7, 2
prices=[2, 6, 1, 3, 2, 7, 2]


# 3. Count the number of occurrences of 2 in the 'prices' list.
# Store the result in a variable called num_two_dollar_slices and print it.
num_two_dollar_slices=prices.count(2)

print(num_two_dollar_slices)


# 4. Find the length of the 'toppings' list and store it in num_pizzas.
num_pizzas=len(toppings)


# 5. Print the string: "We sell [num_pizzas] different kinds of pizza!"
#  where [num_pizzas] represents the value of our variable num_pizzas.
print(f"We sell {num_pizzas} different kinds of pizza!")


# 6. Create a 2D list called 'pizza_and_prices' where each sublist is [price, topping].
# Use this data:
#
# Price | Topping
# ------------------
# 2     | "pepperoni"
# 6     | "pineapple"
# 1     | "cheese"
# 3     | "sausage"
# 2     | "olives"
# 7     | "anchovies"
# 2     | "mushrooms"
#
# For this new list make sure the prices come before the topping name like so: [price, topping_name]
pizza_and_prices=[]
for i in range(len(prices)):
   pizza_and_prices.append([prices[i],toppings[i]])

# 7. Print pizza_and_prices.
print(pizza_and_prices)


# --- Sorting and Slicing Pizzas ---

# 8. Sort pizza_and_prices in ascending order by price.
pizza_and_prices.sort()



# 9. Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza=pizza_and_prices[0]


# 10. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
# Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza=pizza_and_prices[-1]


# 11. It looks like the most expensive pizza from the previous step was our very last 
# "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last 
# slice.
pizza_and_prices.pop(-1)



# 12. Since there is no longer an "anchovies" pizza, you want to add a new topping called 
# "peppers" to keep your customers excited about new toppings. Here is what your new topping 
# looks like:
# [2.5, "peppers"]

# Add the new peppers pizza topping to our list pizza_and_prices.

# Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()


# 13. Three mice walk into the store. They don’t have much money (they’re mice), 
# but they do each want different pizzas.
# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called 
# three_cheapest.
three_cheapest=pizza_and_prices[0:3]


# 14. Print the three_cheapest list.
print(three_cheapest)