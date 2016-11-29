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

    # Randomly add a few edges per node to reasonably close nodes.
    for name, (x, y) in coordinates.items():
        for i in range(random.randint(1, 3)):
            nb_name = random.choice(list(coordinates.keys()))
            nb_x, nb_y = coordinates[nb_name]
            if not nb_name == name and not nb_name in g.neighbours(name):
                cost = abs(x - nb_x) + abs(y - nb_y)  # Manhattan distance between nodes
                g.add_edge(name, nb_name, cost)
                g.add_edge(nb_name, name, cost)
                logger.debug('Added edge from {} to {} with cost {}.'.format(name, nb_name, cost))

    # Verify that all nodes are reachable
    all_nodes = list(coordinates.keys())
    reached_nodes = [all_nodes[0]]
    unexplored_nodes = all_nodes[1:]

    queue = g.neighbours(all_nodes[0])
    for node in queue:
        for n in g.neighbours(node):
            if not n in reached_nodes:
                reached_nodes.append(n)
                unexplored_nodes.remove(n)
                queue.append(n)

    if len(unexplored_nodes) > 0:
        logger.debug('Connecting unreached nodes...')
        nb_name = random.choice(reached_nodes)
        nb_x, nb_y = coordinates[nb_name]
        cost = abs(x - nb_x) + abs(y - nb_y)  # Manhattan distance between nodes
        g.add_edge(name, nb_name, cost)
        g.add_edge(nb_name, name, cost)
        logger.debug('Added edge from {} to {} with cost {}.'.format(name, nb_name, cost))

    return g
