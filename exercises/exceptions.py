"""Exceptions för de olika datastrukturerna."""


class EmptyStack(Exception):
    """För operationer som blir omöjliga att utföra för att stacken är tom."""
    pass


class EmptyQueue(Exception):
    """För operationer som blir omöjliga att utföra för att kön är tom."""
    pass


class EmptyList(Exception):
    """För operationer som blir omöjliga att utföra för att listan är tom."""
    pass
