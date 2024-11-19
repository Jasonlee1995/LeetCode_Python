class Solution:
    def countAsterisks(self, s):
        return sum(sub_str.count("*") for sub_str in s.split("|")[::2])