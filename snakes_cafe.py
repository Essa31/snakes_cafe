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
order=order.capitalize()

menu={
"Wings":0,
"Cookies":0,
"Spring Rolls":0,
"Salmon":0,
"Steak":0,
"Meat Tornado":0,
"A Literal Garden":0,
"Ice Cream":0,
"Cake":0,
"Pie":0,
"Coffee":0,
"Tea":0,
"Unicorn Tears":0
}
reslt=[]


while order!="quit":
    if order not in menu:

        print ("is not in the menu ")
        order = input("""
***********************************
** What would you like to order? **
***********************************
> """)
        order = order.capitalize()
    else:

            menu[order]=menu[order]+1

            if order not in reslt:
               reslt.append(order)
            for i in reslt:
                print(f'** {menu[i]} order of {i} have been added to your meal **')
            order = input("""
***********************************
** What would you like to order? **
***********************************
> """)
else:
    print("Exit")
