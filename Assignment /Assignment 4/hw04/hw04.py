HW_SOURCE_FILE = 'hw04.py'
from math import *

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a)- avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    ans = []
    for number in s:
        if (round(sqrt(number))**2 == number):
            ans.append(round(sqrt(number)))
    return ans

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if (n <= 3):
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if (n <= 3):
        return n
    else:
        f = (n + 1) * [0]
        for i in range(n + 1):
            if (i <= 3):
                f[i] = i
            else:
                f[i] = f[i - 1] + 2 * f[i - 2] + 3 * f[i - 3]
        return f[n]

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def check_divided(k):
        return k % 7 == 0
    
    def check_contain(k):
        if (k == 0):
            return False
        elif (k % 10 == 7):
            return True
        else:
            return check_contain(k // 10)


    def checkSwitch(k):
        if (check_divided(k) or check_contain(k)):
            return True
        else:
            return False


    def count(curr, k, flag = True):
        if (k == n):
            return curr
        else:
            if (checkSwitch(k + 1) and flag):
                return count(curr + 1, k + 1, not flag)
            elif (checkSwitch(k + 1) and not flag):
                return count(curr - 1, k + 1, not flag)
            elif (flag):
                return count(curr + 1, k + 1, flag)
            else:
                return count(curr - 1, k + 1, flag)
    
    return count(0, 0, True)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    k = 0
    while (True):
        if (2 ** (k + 1) > amount):
            break
        else:
            k += 1

    def _count(n):
        f = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if (i == 0):
                    f[i][j] = 1
                elif (j == 0):
                    f[i][j] = 1
                else:
                    f[i][j] = f[i][j - 1]

                    if (i >= 2**j):
                        f[i][j] += f[i - 2**j][j]
        return f[n][k]

    return _count(amount)

print(count_change(7))

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    
    return (lambda b: (lambda a, b: a(a, b))(lambda a, b: b * a(a, b - 1) if b > 0 else 1, b))
