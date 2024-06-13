# Coffee Machine Project
Day 16 of 100 days of Python coding. Using Object Oriented Programming created a Coffee machine that make 3 drinks, tracks the resource quantity (water, milk, and coffee), takes orders and calculate payment or orders.

Coffee Machine Program Requirements

**1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”**

**2. Turn off the Coffee Machine by entering “off” to the prompt.**

**3. Print Coffee machine status report.**
a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

**4. Check resources sufficient?**
When the user chooses a drink, the program should check if there are enough resources to make that drink.


**5. Process coins.**
If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.

**6. Check transaction successful?**
Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time the “report” is triggered.
If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.

**7. Make Coffee.**
If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources. 

E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0

Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
