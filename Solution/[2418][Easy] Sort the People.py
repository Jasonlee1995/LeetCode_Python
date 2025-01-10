class Solution:
    def sortPeople(self, names, heights):
        name_heights = [(name, height) for name, height in zip(names, heights)]
        name_heights.sort(key=lambda x: -x[1])
        return [name for name, _ in name_heights]