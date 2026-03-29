"""
Project: Basta Fazoolin'
You’ve started a position as the lead programmer for the family-style Italian restaurant 
Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen 
a lot of growth lately. You’ve been hired to keep things organized.
"""

# --- Making the Menus ---

# 1. Create a Menu class.
class Menu:
    
# 2. Give Menu a constructor with the five parameters: 
# self, name, items, start_time, and end_time.
    def __init__(self,name,items,start_time,end_time):
        self.name=name
        self.items=items
        self.start_time=start_time
        self.end_time=end_time

    def __repr__(self):
        return f"{self.name} menu avilable from {self.start_time} to {self.end_time}"
    
    def calculate_bill(self,purchased_items):
        total=0
        for item in purchased_items:
            if item in self.items:
                total+=self.items[item]
        return total
    
# 3. Create the brunch menu object.
# Name: 'brunch'
# Time: 11am to 4pm
# Items: {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu=Menu('brunch',{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},11,16)

# 4. Create the early_bird menu object.
# Name: 'early_bird'
# Time: 3pm to 6pm
# Items: {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird=Menu('early_bird',{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00},15,18)

# 5. Create the dinner menu object.
# Name: 'dinner'
# Time: 5pm to 11pm
# Items: {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner_menu=Menu('dinner',{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00},17,23)

# 6. Create the kids menu object.
# Name: 'kids'
# Time: 11am to 9pm
# Items: {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu=Menu('kids',{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},11,21)

# 7. Give the Menu class a string representation method that returns the name 
# of the menu and its availability.
name_menu=brunch_menu

# 8. Test the string representation by printing the brunch menu.
print(name_menu)

# 9. Give Menu a method .calculate_bill() that takes self and purchased_items 
# (a list of item names) and returns the total price.

#Check Up

# 10. Test .calculate_bill() on the brunch menu with: 
# ['pancakes', 'home fries', 'coffee']
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

# 11. Test .calculate_bill() on the early_bird menu with: 
# ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# --- Creating the Franchises ---

# 12. Create a Franchise class.
class Franchise:
    
# 13. Give Franchise a constructor that takes an address and a list of menus.
    def __init__(self,address,list_menu):
        self.address=address
        self.list_menu=list_menu
        

    def __repr__(self):
        return f"{self.address}"
    
    def available_menu(self,time):
        avalible=[]
        for menu in self.list_menu:
            if menu.start_time <= time <= menu.end_time:
                avalible.append(menu.name)
        return avalible

# 14. Create the first two franchises:
# flagship_store: "1232 West End Road" (all four menus)
# new_installment: "12 East Mulberry Street" (all four menus)
flagship_store=Franchise("1232 West End Road",[brunch_menu,early_bird,dinner_menu,kids_menu])
new_installment=Franchise("12 East Mulberry Street",[brunch_menu,early_bird,dinner_menu,kids_menu])

# 15. Give Franchise a string representation that returns the address.

#Check Up

# 16. Give Franchise an .available_menus() method that takes a time and 
# returns a list of Menu objects available at that hour.

#Check Up

# 17. Test .available_menus() at 12 noon (12) and print the results.

print(flagship_store.available_menu(12))

# 18. Test .available_menus() at 5pm (17) and print the results.
print(flagship_store.available_menu(17))


# --- Creating Businesses ---

# 19. Define a Business class.
class Business:

# 20. Give Business a constructor that takes a name and a list of franchises.
    def __init__(self,name,franchises):
        self.name=name
        self.franchises=franchises
    def __repr__(self):
        return self.name
        

# 21. Create the first Business:
# Name: "Basta Fazoolin' with my Heart"
# Franchises: [flagship_store, new_installment]
first_Business=Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])
print(first_Business)


# 22. Create the arepas_menu object.
# Name: 'take_a_arepa'
# Time: 10am to 8pm
# Items: {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu=Menu('take_a_arepa',{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},10,20)
print(arepas_menu)


# 23. Create the arepas_place franchise.
# Address: "189 Fitzgerald Avenue"
# Menus: [arepas_menu]
arepas_place=Franchise("189 Fitzgerald Avenue",[arepas_menu])
print(arepas_place)

# 24. Create the new Business object.
# Name: "Take a' Arepa"
# Franchises: [arepas_place]
new_business=Business("Take a' Arepa",[arepas_place])