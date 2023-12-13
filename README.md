THE PLAN : 
I want to make a trading site ? 
so each user will have a portfolio, which will contain stock (for now just stocks)
Each stock will have a book, that is all you get.
You will have a PnL that is marked to market.
At the end you need to close your positions... so you have to trade back all the stocks ?
otherwise stock have 0 value or something..

well start out with the absolutely basic... 
one user, one stock

user is an object that has a name, an ID and cash amount and a portfolio (dictionary of stock : amount).
stock is an object that has a name, an ID, a book -> (tuple of list ?)

functions supported :
calculate the PnL 
then add new order to the book
lift existing order from the book
query the book etc.

leaderboard is a list of users 

