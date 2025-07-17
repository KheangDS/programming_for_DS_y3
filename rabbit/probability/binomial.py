from scipy import stats
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

