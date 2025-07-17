from abc import ABC, abstractmethod
from scipy import stats


# Define an Interface
class ProbabilityDistribution(object):
    @abstractmethod
    def mean(self):
        pass

    @abstractmethod
    def var(self):
        pass


# Implement the Interface for Descrete and Continuous Distributions
class BinomialDistribution(ProbabilityDistribution):
    def __init__(self, n: int, p: float):
        self.__n = n
        self.__p = p

    def mean(self):
        return stats.binom.mean(n=self.__n, p=self.__p)

    def var(self):
        return stats.binom.var(n=self.__n, p=self.__p)

    def __repr__(self):
        return f"BinomialDistribution(n={self.__n}, p={self.__p})"


class ExponentialDistribution(ProbabilityDistribution):
    def __init__(self, beta: float):
        self.__beta = beta

    def mean(self):
        return stats.expon.mean(scale=self.__beta)

    def var(self):
        return stats.expon.var(scale=self.__beta)

    def __repr__(self):
        return f"ExponentialDistribution(beta={self.__beta})"


if __name__ == "__main__":
    X = BinomialDistribution(n=5, p=0.75)
    print(X)
    print(X.mean())
    print(X.var())
    Y = ExponentialDistribution(beta=2.0)
    print(Y)
    print(Y.mean())
    print(Y.var())
