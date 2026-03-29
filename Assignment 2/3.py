"""
Project: Sam's Surf Shop
Welcome to Sam’s Surf Shop! This project will exercise your knowledge of errors and unit 
testing practices in Python. It will also give you a small taste of testing a full application.

You’ve been hired to create a handful of tests for the shopping cart software at the surf shop. 
Once that is done, you’ll implement some improvements for these tests using more advanced 
unit testing features (skipping, parameterization, and expected failures). Finally, you’ll 
have the opportunity to fix bugs that were exposed by your tests.

The shopping cart software for Sam’s Surf Shop lives inside of the file called surfshop.py. 
Most of our work will take place in tests.py.
"""

# --- Create your tests ---

# 1. Let’s get some basic setup out of the way. 
# First, import both the surfshop and unittest modules in tests.py.

import unittest
import surfshop
import datetime


# 2. Next, create a class which will contain all of your tests. 
# The class can be named whatever you’d like, but it should inherit from unittest.TestCase.
class Testsurfshop(unittest.TestCase):

# 3. The features you need to test have been implemented in the surfshop.ShoppingCart class. 
# In order to test the inner workings of a class, you will need to create a new instance of the shopping cart. 
# Don’t worry - you will handle that in the next tasks! 
# For now, it’s important that every test has a new ShoppingCart object to work with so that 
# way the test always starts on a clean slate.
# In your class, create a setup fixture that runs before every test. 
# It should instantiate a new ShoppingCart object and assign it to an instance variable called self.cart. 
# Your tests can then use self.cart to reference your instance of the ShoppingCart class.
 def setUp(self):
        self.cart=surfshop.ShoppingCart()

 


# 4. It’s time to create your first test! Let’s test the add_surfboards() method of the cart.
# The ShoppingCart.add_surfboards() method takes an integer as its only argument and updates 
# the number of surfboards in the cart. Define a test method that calls this function with 
# an argument of 1 and checks that 'Successfully added 1 surfboard to cart!' is returned.
 def text_add_surfboards(self):
    message=self.cart.add_surfboards(1)
    self.assertequal(message,"Successfully added 1 surfboards to cart!")


# 5. Let’s test another input for the .add_surfboards() method. 
# Create another test method which calls ShoppingCart.add_surfboards(), but this time, passes 
# an argument of 2. It should test that the return value is 'Successfully added 2 surfboards to cart!'
 def test_add_two_surfboards(self):
    message = self.cart.add_surfboards(2)
    self.assertEqual(message, "Successfully added 2 surfboards to cart!")

# 6. The shopping cart has a limit of 4 surfboards per customer. 
# Create a test to check that a surfshop.TooManyBoardsError (a custom exception) is raised 
# when ShoppingCart.add_surfboards() is called with an argument of 5.
 def test_too_many_surfboards(self):
    with self.assertRaises(surfshop.TooManyBoardsError):
        self.cart.add_surfboards(5)


# 7. The shopping cart has a feature that applies rental discounts for locals called apply_locals_discount(). 
# When this function is called, it sets the self.locals_discount property to True.
# Create a test that calls ShoppingCart.apply_locals_discount() and then checks that 
# ShoppingCart.locals_discount is True.
 def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

# --- Run and maintain your tests ---

# 8. It’s time to start running your tests! At the bottom of tests.py, call unittest.main().
# If you’ve implemented your tests correctly, they should all pass - except for one! 
# It seems that the ShoppingCart.apply_locals_discount() function is not working as expected. 
# While you wait for the development team to fix this bug, you don’t want it to cause our tests to fail. 
# Mark this test as an expected failure.
 #@unittest.expectedFailure
 def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

# 9. Sam, the owner of Sam’s Surf Shop, has just informed us that the shop is heading into 
# the off season and business has slowed down. The store’s shopping cart no longer needs 
# to enforce the 4 surfboards per customer rule - at least until business picks up again.
# Go back and modify the test you wrote in task 6 which checks for a surfshop.TooManyBoardsError 
# so that it is skipped.
 @unittest.skip("Off season - limit disabled")
 def test_too_many_surfboards(self):
    with self.assertRaises(surfshop.TooManyBoardsError):
        self.cart.add_surfboards(5)

# 10. Parameterize the test you wrote in task 4 so that it runs 3 times, passing 2, 3, and 4 
# as the arguments to surfshop.add_surfboards(). This allows us to easily test a single function 
# with a variety of inputs. Remember to modify the expected return value with the correct number of surfboards.
 def test_add_multiple_quantities(self):
    for qty in [2, 3, 4]:
        cart = surfshop.ShoppingCart()
        message = cart.add_surfboards(qty)
        self.assertEqual(
            message,
            f"Successfully added {qty} surfboards to cart!"
        )

# --- Improve the software ---

# 11. Sam has noticed all of your hard work and the fact that your tests found a bug. 
# You can now start working on the actual shopping cart software!
# Take a look in surfshop.py. Recall that the ShoppingCart.apply_locals_discount is not 
# setting the ShoppingCart.locals_discount attribute to True, as it should be. Can you fix it?
# When you do, comment out the expected failure decorator and see if all the tests pass.

#Check Up

# 12. Next, make an improvement to the exception that gets thrown when too many surfboards are added to the cart. 
# Modify TooManyBoardsError so that when raised, it has the message 'Cart cannot have more than 4 surfboards in it!'.


# 13. Congratulations on your first successful software testing project! 
# If you want to challenge yourself even further, take a look at the ShoppingCart.set_checkout_date() function. 
# This function takes a datetime.datetime object as an argument and raises a surfshop.CheckoutDateError 
# if the date is not in the future. Can you write a test that validates this behavior?

 def test_checkout_date_in_past(self):
    
    past_date = datetime.datetime.now() - datetime.timedelta(days=1)

    with self.assertRaises(surfshop.CheckoutDateError):
        self.cart.set_checkout_date(past_date)

if __name__ == "__main__":
    unittest.main()