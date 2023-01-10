#!/usr/bin/python3
"""defines a pascal triangle"""


def pascal_triangle(n):
    """implements the function"""
    if n <= 0:
        return ([])
    triangles = [[1]]
    for i in range(n - 1):
        temp = [0] + triangles[-1] + [0]
        row = []
        for j in range(len(triangles[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        triangles.append(row)
    return (triangles)
