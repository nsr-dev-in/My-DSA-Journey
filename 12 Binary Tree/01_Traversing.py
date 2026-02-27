"""
      drink 
   hot     cold
tea coffe  fanta mango

"""

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

drink=Node("drink")
hot=Node("hot")
cold=Node("cold")
mango=Node("mango")
fanta=Node("fanta")
tea=Node("tea")
coffee=Node("coffee")

drink.left=hot
drink.right=cold

hot.left=tea
hot.right=coffee

cold.left=fanta
cold.right=mango

print(drink) #print address
print(drink.val , drink.left.val , drink.right.val)
print(hot.val , hot.left.val , hot.right.val)
print(cold.val , cold.left.val , cold.right.val)
print(drink.left.right.val)