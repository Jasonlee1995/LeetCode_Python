class Solution:
    def convertTime(self, current, correct):
        def convert(hm):
            h, m = hm.split(':')
            return 60 * int(h) + int(m)
        
        time0, time1 = convert(current), convert(correct)
        dt = abs(time1 - time0)
        answer = 0
        for t in [60, 15, 5, 1]:
            answer += dt // t
            dt = dt%t
        return answer