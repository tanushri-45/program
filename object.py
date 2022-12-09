class App:
    def __init__(self, name, price, quantity):
        # will apply condition that quantity should be greater than 0
        assert quantity > 0,  f"{quantity} should be greater than or equal to zero"
        self.price = price
        self.name = name
        self.quantity = quantity


item1 = App("Phone", 1000, 20)
#item1.price = 500
#item1.quantity = 5

item2 = App("Laptop", 300, 90)
#item1.price = 50000
#item2.quantity = 6

print(f"The item1 device is :{item1.name}")
print(f"The item2 device is :{item2.name}")
