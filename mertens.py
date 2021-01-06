def prime(n: int) -> bool:
    """
    Checks if n is prime or not

    Parameters
    ----------
    - n
            int: Positive integer to be checked

    Returns
    -------
    - Primeness of n
            bool
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def mobius(n: int) -> int:
    """
    Performs the Mobiüs function on n

    Parameters
    ----------
    - n
            int: Positive integer to be checked

    Returns
    -------
    - 0 if n has a squared prime factor
    - 1 if n is a square-free positive integer with an even number of prime factors
    - −1 if n is a square-free positive integer with an odd number of prime factors
    """
    if n == 1:
        return 1

    pf_count = 0
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            if n % (i * i) == 0:
                return 0
            pf_count += 1

    if pf_count % 2 == 0:
        return 1
    return -1


'''
def mertens(n):
    sum = 0
    for i in range(1, n + 1):
        sum += mobius(i)
    return sum
'''
