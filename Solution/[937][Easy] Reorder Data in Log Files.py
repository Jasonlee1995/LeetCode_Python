class Solution:
    def reorderLogFiles(self, logs):
        def rule(log):
            identifier, contents = log.split(sep=' ', maxsplit=1)
            if contents[0].isalpha(): return (0, contents, identifier)
            else: return (1, )
        return sorted(logs, key=rule)