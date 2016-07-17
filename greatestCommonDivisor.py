""" GCD using Euclid algorithm """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
print("The greatest common divisor (GCD) is %d." %gcd(num1, num2))
