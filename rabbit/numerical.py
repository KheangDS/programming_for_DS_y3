def EvaluatePolynomial2(a: list, x: complex) -> tuple[complex, complex, complex]:
    """
    TODO
    ----------
    Evaluate a polynomial and its first and second derivatives at a given value of `x`.

    Parameters
    ----------
    `a` : `list[complex]`
        list of coefficients `[a_0,...,a_n]` of the polynomial `p(x)=a_0+a_1 x+...+a_n x^n`
    `x` : `complex`
        complex value at which the polynomial to be evaluated

    Return
    ----------
    `p` : `complex`
        complex value of the polynomial evaluated at `x`
    `dp` : `complex`
        complex value of the first derivative of polynomial evaluated at `x`
    `ddp` : `complex`
        complex value of the second derivative of polynomial evaluated at `x`

    Example
    ----------
    >>> import NumericalAnalysis as na
    >>> p, dp, ddp = na.EvaluatePolynomial2(a=[1, 1, 1], x=1)
    >>> print(p)
    >>> print(dp)
    >>> print(ddp)
    """
    N = len(a)
    n = N - 1
    p = a[n]
    dp = 0
    ddp = 0
    for i in range(1, N, 1):
        ddp = 2 * dp + x * ddp
        dp = p + x * dp
        p = a[n - i] + x * p
    return (p, dp, ddp)

if __name__=="__main__":
    p, dp, ddp = EvaluatePolynomial2(a=[3, 2, 1], x=1)
    print(f"p(2)={p}")
    print(f"dp(2)={dp}")
    print(f"ddp(2)={ddp}")