class Item:
    def calculate_t_p(self,x,y): #in the place of self the item1 or item 2 will be taken  
        return x*y

item1=Item()
item1.name="Phone"
item1.price=100
item1.quantity=5

print(item1.calculate_t_p(item1.price,item1.quantity)) # In the x the 1st element will be passing same as the 2nd to the y

item2=Item()
item2.name="Laptop"
item2.price=1000
item2.quantity=3

print(item2.calculate_t_p(item2.price,item2.quantity))
