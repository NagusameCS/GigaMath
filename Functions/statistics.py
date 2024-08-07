import statistics as stats

class Statistics:
    @staticmethod
    def mean(data):
        result = stats.mean(data)
        explanation = f"The mean of the data {data} is {result}."
        return result, explanation

    @staticmethod
    def median(data):
        result = stats.median(data)
        explanation = f"The median of the data {data} is {result}."
        return result, explanation

    @staticmethod
    def std_dev(data):
        result = stats.stdev(data)
        explanation = f"The standard deviation of the data {data} is {result}."
        return result, explanation

    @staticmethod
    def variance(data):
        result = stats.variance(data)
        explanation = f"The variance of the data {data} is {result}."
        return result, explanation
