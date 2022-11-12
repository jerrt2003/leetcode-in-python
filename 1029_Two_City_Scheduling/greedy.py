class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        T:O(n+nlog(n)) S:O(1)
        Runtime: 28 ms, faster than 69.83% of Python online submissions for Two City Scheduling.
        Memory Usage: 12.9 MB, less than 9.09% of Python online submissions for Two City Scheduling.
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda cost: cost[0]-cost[1])
        return sum(x[0] for x in costs[:len(costs)/2]) + sum(x[1] for x in costs[len(costs)/2:])

print Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print Solution().twoCitySchedCost([[393,874],[299,93],[947,491],[214,782],[25,158],[666,163],[547,293],[653,291],[922,106],[294,479],[79,559],[579,933],[433,507],[75,686],[420,508],[813,256],[613,936],[192,540],[463,762],[784,881],[440,260],[176,655],[532,263],[890,437],[553,516],[880,668]])