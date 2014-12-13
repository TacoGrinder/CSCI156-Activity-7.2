__author__ = 'ortus'


def twosums(n, m=1):
    sums = 0
    for i in range(m, n+1):
        #i += 1
        sums += i
    print(sums)

twosums(10)