"""Övningar på de enklare ADTerna."""

from .exceptions import EmptyStack, EmptyQueue


class Stack():
    """Implementation av ADTn stack."""

    def __init__(self):
        """Initierar en tom stack."""
        pass

    def push(self, item):
        """Lägg till `item` överst på stacken."""
        pass

    def pop(self):
        """Plockar bort och returnerar översta värdet på stacken."""
        pass

    def peek(self):
        """Returnerar översta värdet på stacken."""
        pass

    def is_empty(self):
        """Returnerar `True` om stacken är tom, annars `False`."""
        pass

    def size(self):
        """Returnerar antalet värden på stacken."""
        pass


class Queue():
    """Implementation av ADTn kö (queue)."""

    def __init__(self):
        """Initierar en tom kö."""
        pass

    def enqueue(self, item):
        """Lägger till `ìtem` i slutuet på kön."""
        pass

    def dequeue(self):
        """Plockar bort det första värdet i kön och returnerar det."""
        pass

    def is_empty(self):
        """Returnerar `True` om kön är tom, annars `False`."""
        pass

    def size(self):
        """Returnerar antalet värden i kön."""
        pass
