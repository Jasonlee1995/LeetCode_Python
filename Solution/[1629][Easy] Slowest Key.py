class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        k, t = keysPressed[0], releaseTimes[0]
        for i in range(1, len(keysPressed)):
            dk = keysPressed[i]
            dt = releaseTimes[i] - releaseTimes[i-1]

            if (dt > t) or ((dt == t) and (k < dk)):
                k, t = dk, dt
        return k