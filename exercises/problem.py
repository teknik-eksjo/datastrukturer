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

    # Randomly add a few edges per node to reasonably close nodes.
    # Make sure that we connect each node to at least two other nodes.
    for name, (x, y) in coordinates.items():
        possible_neighbours = list(coordinates.keys())
        possible_neighbours.remove(name)
        nb_names = random.sample(possible_neighbours, random.randint(2, 5))
        for nb_name in nb_names:
            nb_x, nb_y = coordinates[nb_name]
            if not nb_name in g.neighbours(name):
                cost = abs(x - nb_x) + abs(y - nb_y)  # Manhattan distance between nodes
                g.add_edge(name, nb_name, cost)
                g.add_edge(nb_name, name, cost)
                logger.debug('Added edge from {} to {} with cost {}.'.format(name, nb_name, cost))

    # Verify that all nodes are reachable
    logger.debug('Exploring graph to see that all nodes can be reached.')
    all_nodes = list(coordinates.keys())
    reached_nodes = [all_nodes[0]]
    unexplored_nodes = all_nodes[1:]

    queue = [all_nodes[0]]
    while len(queue) > 0:
        node = queue.pop(0)
        logger.debug('Visiting node {}.'.format(node))
        for n in g.neighbours(node):
            if not n in reached_nodes:
                reached_nodes.append(n)
                unexplored_nodes.remove(n)
                queue.append(n)
                logger.debug('First appearance of node {}.'.format(n))

    if len(unexplored_nodes) > 0:
        logger.debug('Connecting unreached nodes...')
        nb_names = random.sample(reached_nodes, 2)
        for nb_name in nb_names:
            nb_x, nb_y = coordinates[nb_name]
            cost = abs(x - nb_x) + abs(y - nb_y)  # Manhattan distance between nodes
            g.add_edge(name, nb_name, cost)
            g.add_edge(nb_name, name, cost)
            logger.debug('Added edge from {} to {} with cost {}.'.format(name, nb_name, cost))

    return g
