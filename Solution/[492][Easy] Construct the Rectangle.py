class Solution:
    def constructRectangle(self, area):
        for num in range(int(area ** 0.5), 0, -1):
            if area % num == 0:
                return [area//num, num]
