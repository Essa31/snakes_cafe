print(""" $ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
      )
order = input("""
***********************************
** What would you like to order? **
***********************************
> """
    )
while order!="quit":
    n =int(input("How many pieces do you want to eat ? "))
    print(f'** {n} order of {order} have been added to your meal **')
    order = input("""
***********************************
** What would you like to order? **
***********************************
> """)
else:
    print("Exit")
