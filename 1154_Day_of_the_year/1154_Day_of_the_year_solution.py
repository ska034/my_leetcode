# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime
        date1 = datetime(day=1, month=1, year=int(date[:4]))
        date2 = datetime.strptime(date, "%Y-%m-%d")
        return (date2-date1).days+1
