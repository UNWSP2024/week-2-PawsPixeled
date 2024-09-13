#def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
#Price Total Purchase
#Programmer = Caiden Nelson
#Date created 9/13/24

#Gets price of items
print('Please enter the price of your five items when prompted')
item_1 = int(input('Item 1 '))
item_2 = int(input('Item 2 '))
item_3 = int(input('Item 3 '))
item_4 = int(input('Item 4 '))
item_5 = int(input('Item 5 '))

print('thank  you')
#finds total before tax
sub = item_1+item_2+item_3+item_4+item_5
#Finds tax
tax = sub*.07
#finds total after tax
total = sub+tax
#Tells Subtotal, tax, and total
print('Your subtotal is,',sub,'your tax is,',tax,'and your total is',total)
#calculate_total_purchase()

#/Users/caidennelson/PycharmProjects/PythonProgramming/.venv/bin/python /Users/caidennelson/PycharmProjects/PythonProgramming/.venv/week 2/Total Purchase.py 
#Please enter the price of your five items when prompted
#Item 1 5
#Item 2 5
#Item 3 5
#Item 4 5
##Item 5 5
#thank  you
#Your subtotal is, 25 your tax is, 1.7500000000000002 and your total is 26.75

#Process finished with exit code 0
