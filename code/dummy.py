""" A dummy example to demonstrate autodocs. """


def add(a: int, b: int) -> int:
    """ A dummy function.

    Note that this will render as any markdown block. That means you can leverage any Mkdocs
    functionality here.

    Example:

    [This is a link embedded inside a docstring](contributing.md#1-writing-docstrings)

    !!! tip

        This is an tip block embedded inside a docstring.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: Result of a + b.
    """
    return a + b
