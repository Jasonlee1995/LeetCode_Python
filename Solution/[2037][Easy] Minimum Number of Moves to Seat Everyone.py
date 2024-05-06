class Solution:
    def minMovesToSeat(self, seats, students):
        return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))