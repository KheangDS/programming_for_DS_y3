from scipy import stats
class ExponentialDistribution(ProbabilityDistribution):
    def __init__(self, beta: float):
        self.__beta = beta

    def mean(self):
        return stats.expon.mean(scale=self.__beta)

    def var(self):
        return stats.expon.var(scale=self.__beta)

    def __repr__(self):
        return f"ExponentialDistribution(beta={self.__beta})"
