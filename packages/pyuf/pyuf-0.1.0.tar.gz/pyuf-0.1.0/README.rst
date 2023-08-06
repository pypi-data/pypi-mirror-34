PyUF: Python Union-Find
=======================

Implementation of the ``Union-Find`` data structure in Python.

Data is divided into different groups ("partitions"). Each group has a name,
and a set of objects. Over this setup, we want to support two operations:

    * ``find(x)``: Return the name of the group where x belongs to.
    * ``union(g1, g2)``: Given two groups, merge them into one. The new
      meta-group contains all the elements from ``g1`` and ``g2``.

Example usage:

.. code:: python

    >>> space = UnionFindSpace(
        Partition("letters", "abcdef"),
        Partition("numbers", range(5)),
    )

    >>> space.find("a")
    letters

    >>> space.find(1)
    numbers

    >>> partition = space.union("letters", "numbers")
    >>> partition.name
    letters_numbers


    # It's possible to indicate the name of the  group

    >>> partition = space.union("letters", "numbers", "alpha")
    >>> partition.name
    alpha
