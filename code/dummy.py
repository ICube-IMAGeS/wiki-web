""" A dummy example to demonstrate autodocs. """


def add(a: int, b: int) -> int:
    """ A dummy function.

    !!! warning
        Dummy warning.

    !!! info
        Dummy info.

    !!! tip
        Dummy tip.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        Addition: Result of a + b.
    """
    return a + b
