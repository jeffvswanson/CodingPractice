# statsClass.py
"""Class encompassing mean: mean(nums), standard deviation: stdDev(nums), and 
combined return of the mean and standard deviation: meanStdDev(nums)."""

from math import sqrt

class Statistics:

    def __init__(self, nums):
        self.nums = nums

    def mean(self):
        total = 0.0
        for num in self.nums:
            total = total + num
        self.avg = total / len(self.nums)
        return self.avg

    def stdDev(self):
        sumDevSq = 0.0
        self.avg = self.mean()
        for num in self.nums:
            dev = num - self.avg
            sumDevSq = sumDevSq + dev * dev
        self.sigma = sqrt(sumDevSq)/(len(self.nums)-1)
        return self.sigma

    def meanStdDev(self):
        self.avg = self.mean()
        self.sigma = self.stdDev()
        return self.avg, self.sigma