"""Code for generating graphs that can be used to solve TSPs."""
import math
import random
import logging
from exercises.graph import Graph


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def names(size, alphabet = ''):
    """Generate reasonable names for nodes."""

    alphabet = alphabet if len(alphabet) > 1 else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name_length = math.ceil(math.log(size, len(alphabet)))

    for i in range(size):
        name = ''
        while i >= len(alphabet):
            name += alphabet[i % len(alphabet)]
            i = i // len(alphabet)
        name = alphabet[i % len(alphabet)] + name

        yield '{0:{fill}>{width}}'.format(name, fill=alphabet[0], width=name_length)


def generate(x_size, y_size):
    coordinates = {name: ((i % x_size) * 10 + 5 + random.randint(-5, 5), (i // y_size) * 10 + 5 + random.randint(-5, 5)) for i, name in zip(range(x_size * y_size), names(x_size * y_size))}
    logger.debug('Coordinates: {}'.format(coordinates))

    g = Graph()

    # Add all nodes to graph.
    for name in coordinates.keys():
        g.add_vertex(name)
        logger.debug('Adding node {}'.format(name))

    # Add edges to all other nodes.
    for name, (x, y) in coordinates.items():
        nodes = list(coordinates.items())
        for nb_name, (nb_x, nb_y) in nodes:
            if not name == nb_name and not nb_name in g.neighbours(name):
                cost = abs(x - nb_x) + abs(y - nb_y)  # Manhattan distance between nodes
                g.add_edge(name, nb_name, cost)
                g.add_edge(nb_name, name, cost)
                logger.debug('Added edge from {} to {} with cost {}.'.format(name, nb_name, cost))
    return g
