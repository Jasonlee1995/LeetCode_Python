class Solution:
    def defangIPaddr(self, address):
        return ''.join(l if l != '.' else '[.]' for l in address)