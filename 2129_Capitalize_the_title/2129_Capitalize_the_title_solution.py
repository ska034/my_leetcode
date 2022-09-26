# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        new_title = title.split(" ")
        for i in range(len(new_title)):
            if len(new_title[i]) > 2:
                new_title[i] = new_title[i].capitalize()
            else:
                new_title[i] = new_title[i].lower()
        return " ".join(new_title)
