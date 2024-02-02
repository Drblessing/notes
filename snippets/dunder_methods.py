"""
This module explores the most commond and important dunder methods in Python.
"""


class CoffeeMaker:

    def __init__(self, model, price, coffee_type="Drip"):
        """The __init__ method is called when the object is created.
        It is used to initialize the object's attributes.
        It is also called the constructor method.
        Again, this method is called when an instance of the class is created,
        from the class. It is the first method to be called.
        """

        self.model = model
        self.price = price
        self.coffee_type = coffee_type

    def __repr__(self):
        """Returns an unambiguous string representation of the object.
        repr is displayed when the bare object is typed into the console,
        or the repr() function is called on the object.
        """
        return f"CoffeeMaker(model={self.model!r}, price={self.price!r}, coffee_type={self.coffee_type!r})"

    def __str__(self):
        """Returns a human readable string representation of the object.
        This is displayed then the print() function is called on the object,
        or the str() function is called on the object.

        Example:
        >>> coffe_maker = CoffeeMaker("Breville", 200, "Espresso")
        >>> print(coffe_maker)
        Breville model, priced at $200, Coffee Type: Espresso
        >>> str(coffe_maker)
        Breville model, priced at $200, Coffee Type: Espresso
        >>> coffe_maker
        CoffeeMark(model='Breville', price=200, coffee_type='Espresso')
        >>> repr(coffe_maker)
        CoffeeMark(model='Breville', price=200, coffee_type='Espresso')
        """
        return f"{self.model} model, priced at ${self.price}, Coffee Type: {self.coffee_type}"

    def __del__(self):
        """Called when the object is about to be destroyed.
        It is used to clean up resources or perform other cleanup activities.
        """
        print(f"{self.model} is being destroyed!")

    def __eq__(self, other):
        """Called when the equality operator == is used.
        It is used to compare the equality of two objects.
        """
        return (
            self.price == other.price
            and self.model == other.model
            and self.coffee_type == other.coffee_type
        )

    def __ne__(self, other):
        """Called when the inequality operator != is used.
        It is used to compare the inequality of two objects.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Called when the less than operator < is used.
        It is used to compare if an object is less than another object.
        """
        return self.price < other.price

    def __le__(self, other):
        """Called when the less than or equal to operator <= is used.
        It is used to compare if an object is less than or equal to another object.
        """
        return self.price <= other.price

    def __gt__(self, other):
        """Called when the greater than operator > is used.
        It is used to compare if an object is greater than another object.
        """
        return self.price > other.price

    def __ge__(self, other):
        """Called when the greater than or equal to operator >= is used.
        It is used to compare if an object is greater than or equal to another object.
        """
        return self.price >= other.price

    def __add__(self, other):
        """Called when the addition operator + is used.
        It is used to add two objects together.
        """
        return self.price + other.price

    def __sub__(self, other):
        """Called when the subtraction operator - is used.
        It is used to subtract one object from another.
        """
        return self.price - other.price

    def __mul__(self, other):
        """Called when the multiplication operator * is used.
        It is used to multiply two objects together.
        """
        return self.price * other.price

    def __truediv__(self, other):
        """Called when the division operator / is used.
        It is used to divide one object by another.
        """
        return self.price / other.price

    def __floordiv__(self, other):
        """Called when the floor division operator // is used.
        It is used to perform floor division on two objects.
        """
        return self.price // other.price

    def __iter__(self):
        """Called when an iterator is required.
        It returns an iterator object.
        Can use a generator, so the __next__ method is not required.
        """
        yield self.model
        yield self.price
        yield self.coffee_type

    def __len__(self):
        """Called when the built-in len() function is called on the object.
        It returns the length of the object.
        """
        return len([self.model, self.price, self.coffee_type])

    def __call__(self):
        """Called when the object is called as a function.
        It is used to make the object callable.
        """
        return f"{self.model} made a cup of {self.coffee_type} coffee!"

    def __enter__(self):
        """Called when the object is used in a with statement.
        It is used to return the object for use in the with statement.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when the object is used in a with statement.
        It is used to clean up resources or perform other cleanup activities.
        """
        print("Cleaning up resources...")
        return True
