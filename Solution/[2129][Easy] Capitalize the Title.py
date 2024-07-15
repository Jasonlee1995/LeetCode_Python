class Solution:
    def capitalizeTitle(self, title):
        stack = []
        for word in title.split():
            if len(word) < 3: stack.append(word.lower())
            else:             stack.append(word.capitalize())
        return ' '.join(stack)