import sys
import numpy as np
import json
import ast

"""
Sample Input:
 
 "{"timeToLive": 1, "name": 'Caleb_Kumar'}
 {"timeToLive": 2, "name": 'Caleb_Kumar'}
 {"timeToLive": 5, "name": 'Caleb_Kumar'}
 {"timeToLive": 1, "name": 'Caleb_Kumar'}
 {"timeToLive": 2, "name": 'Caleb_Kumar'}
 {"timeToLive": 3, "name": 'Caleb_Kumar'}
 {"timeToLive": 4, "name": 'Caleb_Kumar'}
 {"timeToLive": 3, "name": 'Caleb_Kumar'}
 {"timeToLive": 10, "name": 'Caleb_Kumar'}"
 
 Sample Output:
 
 Number of Lines: 9
 Mean: 3.44                                     (8 + 6 + 17) / 9
 Std. Dev: 

"""


def find_summary_statistics():
    """
    Given stdin of lines of {timeToLive: <num>, name: <string>}
    :return: Std. Dev, Mean, Number of Lines
    """

    # Change var name
    vals = []

    for line in sys.stdin:

        # Change var name
        lineDict = ast.literal_eval(line)
        vals.append(float(lineDict['timeToLive']))

    print('Number of Lines: {}').format(len(vals))
    print('Mean: {}').format(round(sum(vals) / len(vals), 2))

    numArray = np.array(vals, dtype=np.float64)
    print('NumPy Std. Dev: {}').format(np.std(numArray, axis=0, ddof=0))

    print('My Std. Dev: {}').format(round(calculate_std_dev(vals), 2))

    print('Random Std. Dev: {}').format(stddev(vals))


def calculate_std_dev(nums):
    mean = sum(nums) / len(nums)
    diffSquareds = []
    for num in nums:
        diff = num - mean
        diffSquareds.append(diff ** 2)

    meanOfDiffSquared = sum(diffSquareds) / (len(diffSquareds))
    return meanOfDiffSquared ** .5


"""
1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!
"""


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data) / n  # in Python 2 use sum(data)/float(n)


def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x - c) ** 2 for x in data)
    return ss


def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss / (n - ddof)
    return pvar ** 0.5


find_summary_statistics()
