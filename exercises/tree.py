"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""

class Node():
    def __init__(self, key, value=None):
        """Initiera en nod."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def count_children(self):
        count = 0
        if not self.left is None:
            count += 1
        if not self.right is None:
            count += 1

        return count


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self):
        """Initiera det tomma trädet."""
        self.root = None

    def insert(self, key, value=None):
        """Lägg till en nod i trädet. Dubletter tillåts inte."""
        pass

    def lookup(self, key):
        """Sök efter noden med matchande key.

        Returnerar tupeln med matchande noden (objektet) och dess förälder
        (även detta objekt).

        Kasta ett exception om noden med `key` inte finns.
        """
        pass

    def delete(self, key):
        """Radera noden med matchande key.

        Notera att det finns tre fall att hantera, noden som raderas kan ha
        0, 1 eller 2 barn. Dessa hanteras alla på lite olika vis.

        Kasta ett exception om trädet är tomt.
        """
        pass

    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """
        pass

    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        # Använd traverse...
        pass
