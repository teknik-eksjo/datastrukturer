"""Övningar på ADTn unordered list."""


class Node():
    """Implementation av nod för `UnorderedList`.
    """

    def __init__(self, data):
        """Initiera noden med attributen `self._data` och `self._next`.
        """
        pass


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):
        """Initiera den tomma listan.
        """
        pass

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`.
        """
        pass

    def add(self, item):
        """Lägg till `item` i början av listan.
        """
        pass

    def size(self):
        """Returnerar antalet värden i listan.
        """
        pass

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`.
        """
        pass

    def remove(self, item):
        """Raderar `item` från listan.
        """
        pass

    def append(self, item):
        """Lägg till `item` i slutet av listan.
        """
        pass

    def insert(self, position, item):
        """Lägg till `item` på index `position`.
        """
        pass

    def index(self, item):
        """Returnerar index i listan för `item`.
        """
        pass

    def pop(self, postition=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """
        pass
