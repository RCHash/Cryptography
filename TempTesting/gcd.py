def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if max(a,b)%min(a,b)==0:
        return min(a,b);
    else:
        return gcd(min(a,b),max(a,b)%min(a,b));