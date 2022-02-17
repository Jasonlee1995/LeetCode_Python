class Solution:
    def findRestaurant(self, list1, list2):
        l1_info = {l1 : idx for idx, l1 in enumerate(list1)}
        answer, least = [], None
        for idx, l2 in enumerate(list2):
            if l2 in l1_info:
                if not answer:
                    answer.append(l2)
                    least = l1_info[l2] + idx
                elif l1_info[l2] + idx < least:
                    answer = [l2]
                    least = l1_info[l2] + idx
                elif l1_info[l2] + idx == least:
                    answer.append(l2)
        return answer
