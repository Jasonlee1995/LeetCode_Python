class Solution:
    def isPathCrossing(self, path):
        direction = {'N' : 1j, 'S' : -1j, 'E' : 1, 'W' : -1}
        node = 0
        history = {node}
        for d in path:
            node += direction[d]
            prev = len(history)
            history.add(node)
            if len(history) == prev:
                return True
        return False