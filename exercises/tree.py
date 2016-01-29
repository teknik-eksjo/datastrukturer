"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initiera det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägg till en nod i trädet."""
        pass

    def lookup(self, key):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """
        pass

    def delete(self, key):
        """Radera noden med matchande key."""
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
