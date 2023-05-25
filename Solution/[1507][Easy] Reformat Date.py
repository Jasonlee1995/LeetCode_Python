class Solution:
    def reformatDate(self, date):
        d, m, y = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return '{}-{:02}-{:02}'.format(y, months.index(m)+1, int(d[:-2]))