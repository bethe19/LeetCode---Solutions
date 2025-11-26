class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        for s in sandwiches:
            if c[s] > 0:
                c[s] -= 1
            else:
                return sum(c.values())
        return 0
        