class Solution:
    def maximumPopulation(self, logs):
        y_min, y_max = 1950, 2050
        years = [0] * (y_max+1)
        for s, e in logs:
            years[s] += 1
            years[e] -= 1
        for y in range(y_min, len(years)):
            years[y] += years[y-1]
        return years.index(max(years[y_min:]))