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
        self._attributes = {"model": model, "price": price, "coffee_type": coffee_type}

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

    def __getitem__(self, key):
        """Allows dict-like access to the object's attributes"""
        return self._attributes.get(key, None)

    def __setitem__(self, key, value):
        """Enables setting attributes like a dictionary."""
        if key in self._attributes:
            setattr(
                self, key, value
            )  # Update the attribute using the built-in setattr function
            self._attributes[key] = value  # Keep the _attributes dictionary in sync

    def __delitem__(self, key):
        """Allows deletion of attributes like a dictionary, with some restrictions for essential attributes."""
        if key in [
            "model",
            "price",
            "coffee_type",
        ]:  # Prevent deleting essential attributes
            raise KeyError("Cannot delete essential attribute.")
        del self._attributes[key]

    def __contains__(self, key):
        """Check if a certain attribute exists within the object."""
        return key in self._attributes

    def __hash__(self):
        """Make object hashable, based on immutable attributes."""
        # Assuming model, price, and coffee_type together define the uniqueness of the object
        return hash((self.model, self.price, self.coffee_type))

    def __del__(self):
        """Called when the object is about to be destroyed.
        It is used to clean up resources or perform other cleanup activities.
        This is not really recommended to use, as it is not guaranteed to be called.
        Instead, we use context managers or explicitly call a cleanup method.
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


if __name__ == "__main__":
    coffe_maker = CoffeeMaker("Breville", 200, "Espresso")
    print(coffe_maker)
    print(repr(coffe_maker))
    print(len(coffe_maker))
    print(coffe_maker())
    with coffe_maker:
        print("Making coffee...")
    print("Done!")
    coffee_maker2 = CoffeeMaker("Breville", 200, "Espresso")
    coffee_maker3 = CoffeeMaker("Keurig", 150, "Drip")
    for i in coffe_maker:
        print(i)
    print(coffee_maker2 == coffee_maker3)
    print(coffee_maker2 != coffee_maker3)
    print(coffee_maker2 < coffee_maker3)
    print(coffe_maker + coffee_maker2)
    # Dictionary-like access
    print(coffe_maker["model"])
    coffe_maker["model"] = "Keurig"
    print(coffe_maker["model"])
    if "model" in coffe_maker:
        print("Yes")
    print(hash(coffe_maker))
    d = {}
    d[coffe_maker] = "Breville"
    print(coffe_maker.model)
