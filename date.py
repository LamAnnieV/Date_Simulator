###############################################################################
#CREATED BY:  ANNIE V LAM
#
#DATE:  2023-09-12
#
#Purpose:  Create a date.py script that is a date simulator
###############################################################################


##################################DEFINE FUNCTION(S)###########################

def second_date(somecost, someamount):
    if somecost < someamount:
        print(f"I had a wonderful time.  I would like to see you again.")

#user input for general information
user_name = input("What is your first name? ")
dates_name = input("What is your date's name? ")
restaurant = input("Name of the restaurant you are taking your date on? ")
budget = float(input("What is your budget for this date? "))

#A welcome statement to the diners
print(f"Welcome {user_name} you are going on a simulated date with {dates_name}.  Let's start your date at {restaurant}")

#Create a List within a Dictionary for Menu Items
menu = {    
    "a": ["water", 0.00],
    "b": ["coke", 2.00],
    "c": ["tea",2.50],
    "d": ["coffee", 3.00],
    "e": ["a glass of wine", 12.00],
    "f": ["a bottle of wine", 40.00],
    "g": ["burger and fries", 15.00],
    "h": ["steak and potatoes", 50.00],
    "i": ["salmon and sauteed garlic green beans", 30.00],
    "j": ["chicken salad", 20.00],
    "k": ["shrimp alfredo", 25.00],
    "l": ["ice cream", 5.00],
    "m": ["cheese cake", 6.00],
    }

#Print Menu in readable form
print("Menu:")
for key, item in menu.items():
    name, price = item
    print(f"{key}: {name} - ${price:.2f}")


print("Welcome I will be your simulated waitress this evening. Here is the menu. Miss, what would you like this evening?")

date_order = []  #set date order to a list
while True:                  #this is a while loop that continues until a "break" statement
    item = input('Enter selection or "done" to stop entering: ')  #This prompts users input and stores it in the local variable 
    if item.lower() == 'done':  #When user enters 'done', the value of the item = "done".  If the value is "done"
        break                    #Then break it to get out of the while loop
    date_order.append(item.lower()) #append the item to the global variable

print(date_order)
print("Welcome I will be your simulated waitress this evening. Here is the menu. Sir, what would you like this evening?")
user_order = []
while True:
    value = input('Enter selection or "done" to stop entering: ')
    if value.lower() == 'done':
        break  
    user_order.append(value.lower())

print(user_order)
combined_order = []
combined_order = user_order + date_order
print(combined_order)
total_bill=0.0

##how to iterate throught the combined_order and get the price from the menu
total_cost = 0.0   #set initial total_cost to zero

for key in combined_order:      #for the key in the combined order_order
    if key in menu:    #if the key is also in the menu
        item_list = menu[key]  #extract the food list from the menu and set it to item_list
        item_price = item_list[1] #set the item_price item price from the item_list using index 
        total_cost += item_price  #add it the item_price to the total_cost
    else:
        print(f"Item with code {key} not found in the menu.")

print(f"Total order cost: ${total_cost:.2f}")

budget -= total_cost

print(f"{user_name}, your remaining budget is ${budget}.")

second_date(total_cost, 80)
