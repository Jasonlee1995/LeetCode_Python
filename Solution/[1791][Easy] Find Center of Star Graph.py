class Solution:
    def findCenter(self, edges):
        return (set(edges[0]) & set(edges[1])).pop()