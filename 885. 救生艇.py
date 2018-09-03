class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        b = [limit]*len(people)
        c = [2]*len(people)
        p = len(people) - 1
        max_ = 0
        while p >= 0:
            for i in range(len(b)):
                if b[i]-people[p] >= 0 and c[i] > 0:
                    b[i] -= people[p]
                    c[i] -= 1
                    if i > max_:
                        max_ = i
                    break
            p -= 1
        return max_ + 1

    def __init__(self, people, limit):
        self.people = people
        self.limit = limit

    def getAns(self, people, limit):
        print(Solution.numRescueBoats(self, people, limit))
def main():
    people = [3,2,2,1]
    limit = 3
    S = Solution(people,limit)
    S.getAns(people,limit)
if __name__ == '__main__':
    main()