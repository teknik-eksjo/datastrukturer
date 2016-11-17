"""Implementation av ADTn graph."""


class Graph():
    """Implementation av ADTn Graph med metoden `Adjacency list`.

    En dictionary, `self._nodes`, används för att lagra alla noder och kanter.
    En node är en nyckel i `self._nodes` och dess kanter representeras av en
    lista med parvisa tupler.

    En graf med noderna `a`, `b` och `c` och kanter mellan alla tre skulle
    representeras som nedan.

    self._nodes = {'a': [('b', 4), ('c', 2)],
                   'b': [('a', 4), ('c', 5)],
                   'c': [('a', 2), ('b', 5)]}
    """

    def __init__(self):
        """Initiera `self._nodes`."""
        self._ nodes = {}


    def is_adjacent(self, x, y):
        """Kontrollera om `x` och `y` är grannar."""
        return False

    def neighbours(self, key):
        """Returnera alla grannar till `key`."""
        pass

    def add_vertex(self, key):
        """Lägg till en ny nod."""
        pass

    def get_vertices(self):
        """Returnera grafens alla noder."""
        pass

    def add_edge(self, x, y, value = None):
        """Lägg till en kant från `x` till `y`."""
        pass

    def set_edge_value(self, key, value):
        """Sätt värde för kanten mellan `x` och `y`."""
        pass

    def get_edge_value(self, key):
        """Returnera värde för kanten mellan `x` och `y`."""
        pass

    def __contains__(self, key):
        """Kontrollera om noden med matchande `key` finns."""
        pass

    def __iter__(self):
        """Gör det enkelt att iterera över grafens alla noder."""
        pass
