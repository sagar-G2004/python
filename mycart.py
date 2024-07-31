"""1.	Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price"""
class mycart:
    
    def __init__(self):
        self.items=[]
        
    def add_item(self,x,y):
        self.items.append((x,y))
        print(f"{x} and {y} are added")
        print(self.items)
    def delete(self,name):
        for item in self.items:
            if(item[0])==name:
                self.items.remove(item)
            print(f"{item} is removed")
            print(self.items)
            return
        else:
            print("item not found")
            print(self.items)
    def calc_price(self):
        total=sum(item[1] for item in self.items)
        print("total price:",total)
cart=mycart()
cart.add_item("chair", 200)
cart.add_item("table", 800)
cart.add_item("laptop", 62200)
cart.delete("chair")
cart.calc_price()
    
