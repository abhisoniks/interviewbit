# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=self.myFunc)
        startIn=intervals[0].start
        endIn=intervals[0].end
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            inter=intervals[i]
            if inter.start<endIn:
                if inter.end>endIn:
                    endIn=inter.end
                    res[-1].end=endIn
                continue
            else:
                res.append(inter)
                startIn=inter.start
                endIn=inter.end
        return res

    def myFunc(self,val):
        return val.start
