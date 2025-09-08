class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise Exception("Coffee name cannot be changed")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 3:
            raise Exception("Invalid name")
        self._name = value

        
    def orders(self):
        return [orders for orders in Order.all if orders.coffee is self]
    
    def customers(self):
        matches = []
        for order in self.orders():
            c = order.customer
            if c not in matches:
                matches.append(c)
        return matches
    
    def num_orders(self):
        coffee_orders = self.orders()
        return len(coffee_orders)
    
    def average_price(self):
        total = 0
        count = 0
        for order in self.orders():
                total += order.price
                count += 1

        if count == 0:
            return 0
        else:
            avg = total/count
        return avg


class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [orders for orders in Order.all if orders.customer is self]
    
    def coffees(self):
        matches = []
        for order in self.orders():
            co = order.coffee
            if co not in matches:
                matches.append(co)
        return matches
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        best_customer = None
        total_spent = 0

        for customer in cls.all:
            spent = sum( order.price for order in customer.orders() if order.coffee is coffee)
            if  spent > total_spent:
                total_spent = spent
                best_customer = customer
        return best_customer

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise Exception("Not a customer")
        else:
            self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception("Not a coffee")
        else:
            self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if hasattr(self, "_price"):
            raise Exception("Price cannot be changed")
        if not isinstance(value, float):
            raise Exception("Price must be a float")
        if value < 1.0 or value > 10.0:
            raise Exception("Incorrect price")
        self._price = value