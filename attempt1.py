import time
total_stocks = 1 
init_capital = 10000
stock_id_to_stock = {}

class book :
    def __init__(self) :
        self.buy = []
        self.sell = []

    def add_to_book_buy(self , price, quantity , time) : 
        self.buy.append([price,-time,quantity])
        self.buy.sort()

    def add_to_book_sell(self , price, quantity , time):
        self.sell.append([price,time,quantity])
        self.sell.sort(reverse=True)

    def remove_top_buy(self):
        self.buy.pop()

    def remove_top_sell(self):
        self.sell.pop()

    def display_book(self):
        print("Buy side of the book   |||   Sell side of the book")
        print("time | quantity | price |  price | quantity | time" )
        for i in range(1,1+min(len(self.sell),len(self.buy))):
            print(-self.buy[-i][1] , self.buy[-i][2],self.buy[-i][0] , self.sell[-i][0],self.sell[-i][2],self.sell[-i][1])
    
    def give_top_of_the_book(self) : 
        # assuming book is never empty
        return {"top bid"  : self.buy[-1][0] , "bid quantity" : self.buy[-1][1] , "top sell": self.sell[-1][0] , "sell quantity" : self.sell[-1][1]} 

class stock :
    def __init__(self,name,id) :
        self.name = name 
        self.id = id 
        self.book = book() # this is a tuple , a buy side book and a sell side book
        stock_id_to_stock[id]  = self
    def mid_price(self):
        return (self.book.give_top_of_the_book()["top bid"] + self.book.give_top_of_the_book()["top sell"]) / 2
    def swmid_price(self) : 
        return (self.book.give_top_of_the_book()["top bid"]*self.book.give_top_of_the_book()["sell quantity"] + self.book.give_top_of_the_book()["top sell"]*self.book.give_top_of_the_book()["bid quantity"])/(self.book.give_top_of_the_book()["bid quantity"] + self.book.give_top_of_the_book()["sell quantity"])

    def lift_bid(self) : 
        # you sell , you gain money , you lose quantity
        quantity = self.book.give_top_of_the_book()["bid quantity"]
        price = (self.book.give_top_of_the_book()["top bid"]*self.book.give_top_of_the_book()["bid quantity"])
        self.book.remove_top_buy()
        return [quantity, price]

    def lift_sell(self):
        # you buy , you gain money , you lose quantity
        quantity = self.book.give_top_of_the_book()["sell quantity"]
        price = (self.book.give_top_of_the_book()["top sell"]*self.book.give_top_of_the_book()["sell quantity"])
        self.book.remove_top_buy()
        return [quantity, price]

    def place_buy(self,price,quantity) :
        # check that the orders shouldn't clash, book shouldn't cross
        self.book.add_to_book_buy(price,quantity,time.time())
    
    def place_sell(self,price,quantity) : 
        # check that the orders shouldn't clash, book shouldn't cross
        self.book.add_to_book_sell(price,quantity,time.time())



    
class user : 
    def __init__(self, name, id  ):
        self.name = name 
        self.id = id 
        self.portfolio = [0 for _ in range(total_stocks)]
        self.capital = init_capital
    
    def buy_stock_lift_all(self,stock_id , quantity) : 
        # stock_id_to_stock[stock_id].
        self.portfolio[stock_id]+=quantity

    def sell_stock(self,stock_id,quantity) :
        self.portfolio[stock_id]-=quantity
        # note that short selling is allowed
    
    def calculate_pnl() : 
        pass 

aapl = stock("AAPL" , 0)



