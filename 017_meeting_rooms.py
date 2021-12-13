# https://www.lintcode.com/problem/920/description


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda interval: interval.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        
        return True


def getIntervals(list_of_tupels):
    result = []
    for elem in list_of_tupels:
        result.append(Interval(*elem))
    return result

def printIntervals(intervals):
    result = []
    for interval in intervals:
        result.append((interval.start, interval.end))
    print(result)

s = Solution()
# intervals = getIntervals([(0,30),(5,10),(15,20)])
# print(s.canAttendMeetings(intervals))
# intervals = getIntervals([(5,8),(9,15)])
# print(s.canAttendMeetings(intervals))
intervals = getIntervals([(465,497),(386,462),(354,380),(134,189),(199,282),(18,104),(499,562),(4,14),(111,129),(292,345)])
print(s.canAttendMeetings(intervals))