import bisect
import itertools

class Solution:
    def answerQueries(self, nums, queries):
        cum_sum  = list(itertools.accumulate(sorted(nums)))
        return [bisect.bisect_right(cum_sum, q) for q in queries]