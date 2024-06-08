class Solution:
    def timeRequiredToBuy(self, tickets, k):
        answer = tickets[k]
        for idx, ticket in enumerate(tickets):
            if idx < k:   answer += min(ticket, tickets[k])
            elif idx > k: answer += min(ticket, tickets[k]-1)
        return answer