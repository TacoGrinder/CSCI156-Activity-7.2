__author__ = 'ortus'


def boxes(m, n=None):
    corners = "+"+"-"*(m)+"+"+"\n"
    vertical = "|"+" "*(m)+"|"+"\n"
    if n is None:
        n = m
    a = corners+vertical*n+corners
    print(a)


boxes(5,6)