#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(i, list) for i in m_a) or not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not m_b or not all(m_a) or not all(m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(i, (int, float)) for j in m_a for i in j) or not all(isinstance(i, (int, float)) for j in m_b for i in j):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a) or not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[sum(i * j for i, j in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
