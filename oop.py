class SimpleClass:
    ...
class Person:
    pass
class Classey:
    varia=2

    def method(self):
        print(self.varia)

object_one = Classey()
object_two = Classey()

object_one.varia=3
object_two.varia=5

# print(object_one.varia)
# print(object_two.varia)


class Transport:
    def __init__(self,air,water):
        self.air=air
        self.water=water

    #def __str__(self):


obj_transport = Transport("beluga","Hovercraft")
obj_2=Transport("Jet","boat")

# print(obj_transport.air,obj_transport.water)
# print(obj_2.air,obj_2.water)


class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def print_name(self):
        print(self.fname,self.lname)

x=Person("John","Smith")
y=Person("Mary","Samantha")
# x.print_name()
# y.print_name()

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item_name,qty):
        item=(item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break

#This method computes the number of items in our cart
    def calculate_total(self):
        total=0
        for item in self.items:
            total=total+item[1]

        return total

cart=ShoppingCart()

#add items to our cart
#I used a tuple
cart.add_item("Toyota",2)
cart.add_item("RollsRoyce",3)
cart.add_item("G wagon",2)

print("Current Items in Cart:")
for item in cart.items:
    print(item[0],"-",item[1])

total_qty=cart.calculate_total()
print("Total Qty in Cart:",total_qty)




