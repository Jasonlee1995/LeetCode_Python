import collections

class Solution:
    def countStudents(self, students, sandwiches):
        preference = collections.Counter(students)
        
        for sandwich in sandwiches:
            preference[sandwich] -= 1

            if (preference[0] == -1) or (preference[1] == -1):
                preference[sandwich] += 1
                break

        return preference[0] + preference[1]