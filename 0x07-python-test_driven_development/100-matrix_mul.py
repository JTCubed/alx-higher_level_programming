#!/usr/bin/python3

"""multiplies 2 matrices"""


def matrix_mul(m_a, m_b):

    """
    multiplies 2 matrices

    args: m_a and m_b
    """

    for name, m in [("m_a", m_a), ("m_b", m_b)]:
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
        if not m or not all(row for row in m):
            raise ValueError("{} can't be empty".format(name))
        row_len = len(m[0])
        for row in m:
            if not all(isinstance(e, (int, float)) for e in row):
                raise TypeError("{} should contain only"
                                " integers or floats".format(name))
            if len(row) != row_len:
                raise TypeError("each row of {} must be of"
                                " the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
