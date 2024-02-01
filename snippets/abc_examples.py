""" 
Gives an example of using abstract base classes to create a custom tea party 
observer and subject class.
"""

from abc import ABC, abstractmethod


class TeaPartyMember(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

    @abstractmethod
    def member_catchphrase(self):
        pass


class Guest(TeaPartyMember):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received message: {message}")


class MadHatter(Guest):
    def member_catchphrase(self):
        return "Why is a raven like a writing desk?"


class Alice(Guest):
    def member_catchphrase(self):
        return "Curiouser and curiouser!"


class CheshireCat(Guest):
    def member_catchphrase(self):
        return "We're all mad here."


class Host:
    def __init__(self):
        self.guests = []

    def invite(self, guest: Guest):
        self.guests.append(guest)

    def tea_ready(self):
        print("Tea is ready!")
        for guest in self.guests:
            guest.update("Tea is ready!")
            print(f"{guest.name}: {guest.member_catchphrase()}")


if __name__ == "__main__":
    # Create instances of the guests
    mad_hatter = MadHatter("Mad Hatter")
    alice = Alice("Alice")
    cheshire_cat = CheshireCat("Cheshire Cat")

    # Create a Host
    host = Host()

    # Invite the guests
    host.invite(mad_hatter)
    host.invite(alice)
    host.invite(cheshire_cat)

    # Notify the guests that the tea is ready
    host.tea_ready()  # Mad Hatter, Alice, and Cheshire Cat receive the message that tea is ready
