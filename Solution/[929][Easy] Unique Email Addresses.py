class Solution:
    def numUniqueEmails(self, emails):
        answer = set()
        for email in emails:
            local, domain = email.split('@')
            stack = []
            for letter in local:
                if letter == '.': continue
                elif letter == '+': break
                else: stack.append(letter)
            answer.add('@'.join([''.join(stack), domain]))
        return len(answer)