"""Övningar på ADTn Graph."""


class Vertex():
    """Implementation av nod. Används tillsammans med `Graph`."""
    def __init__(self, key):
        """Initiera noden med `key` och utan grannar."""
        self.key = key
        self._connected_to = {}

    def add_neighbor(self, neighbor, weight=None):
        """Lägg till en granne med den frivilliga vikten `weight`."""
        self._connected_to[neighbor] = weight

    def get_connections(self):
        """Returnera en lista med nodens grannar."""
        return self._connected_to.keys()

    def get_weight(self, neighbor):
        """Returnera vikten hos kanten till grannen `neighbor`."""
        return self._connected_to[neighbor]

    def __repr__(self):
        """Object representation with `self.key` as identifiera and the first
        five neighbors.
        """

        neighbors = sorted(connected_to.keys())
        if len(neighbors) > 5:
            del neighbors[5:]
            neighbors.append('...')
        return '<Vertex {}: {}>'.format(self.key, ', '.join(neighbors))


class Graph():
    """Implementation av ADTn Graph med metoden `Adjacency list`.

    En dictionary, `self._nodes`, används för att lagra alla noder och kanter.
    En node är en nyckel i `self._nodes` och dess kanter representeras av en
    lista med parvisa tupler.

    En graf med noderna `a`, `b` och `c` och kanter mellan alla tre skulle
    representeras som nedan.

    self._nodes = {'a': (('b', 4), ('c', 2)),
                   'b': (('a', 4), ('c', 5)),
                   'c': (('a', 2), ('b', 5))}
    """

    def __init__(self):
        """Initiera `self._vertices`."""
        self._vertices = []

    def add_vertex(self):
        """Lägg till en ny nod."""
        pass

    def get_vertex(self, key):
        """Returnera noden med matchande `key`."""
        pass

    def get_vertices(self):
        """Returnera grafens alla noder."""
        pass

    def __contains__(self, key):
        """Kontrollera om noden med matchande `key` finns."""
        pass

    def __iter__(self):
        """Gör det enkelt att iterera över grafens alla noder."""
        pass
