class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination: return True

        dic = {num : [] for num in range(n)}
        for node1, node2 in edges:
            dic[node1].append(node2)
            dic[node2].append(node1)

        nodes = set()
        stack = [source]
        while stack:
            node = stack.pop()
            for neighbor in dic[node]:
                if neighbor not in nodes:
                    stack.append(neighbor)
            nodes.add(node)
        return destination in nodes