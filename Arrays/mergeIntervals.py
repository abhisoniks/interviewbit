# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        i=0
        while i<len(intervals):
            if intervals[i].end<new_interval.start:
                i+=1
                continue
            break
        if i==len(intervals):
            intervals.append(new_interval)
            return intervals
        if intervals[i].start<=new_interval.start and intervals[i].end>=new_interval.end:
            return intervals
        if intervals[i].start>new_interval.end:
            q=intervals[i:]
            m=intervals[:i]
            m.append(new_interval)
            m.extend(q)
            return m
        start=min(intervals[i].start,new_interval.start)
        s=i
        while s<len(intervals) and intervals[s].end<=new_interval.end:
            s+=1
        end=-1
        flag=False
        result=intervals[:i]
        if s==len(intervals):
            end=new_interval.end
        else:
            if intervals[s].start>new_interval.end:
                flag=True
                end=max(intervals[s-1].end, new_interval.end)
            else:
                end=intervals[s].end
        result.append(Interval(start,end))
        if flag:
            result.extend(intervals[(s):])
        else:
            result.extend(intervals[(s+1):])
        return result
