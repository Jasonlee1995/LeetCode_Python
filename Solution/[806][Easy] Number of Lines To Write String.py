class Solution:
    def numberOfLines(self, widths, s):
        line, width = 1, 0
        for letter in s:
            w = widths[ord(letter)-ord('a')]
            if width + w > 100: line, width = line+1, 0
            width += w
        return [line, width]