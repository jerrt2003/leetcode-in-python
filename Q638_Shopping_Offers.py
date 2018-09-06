class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        list_satisfied = True
        for idx in range(len(needs)):
            if needs[idx] != 0:
                list_satisfied = False
                break
        if list_satisfied:
            return 0
        # total price to pay by w/o using offer
        res = 0
        res_need_list = [0]*len(needs)
        for idx in range(len(needs)):
            res += price[idx]*needs[idx]
        # now go through the special offer list
        cost_list = list()
        for offer in special:
            # to find if current offer match the requirement
            _needs = needs[:]
            offer_fit = True
            for idx in range(len(_needs)):
                if offer[idx] > _needs[idx]:
                    offer_fit = False
                    break
            if offer_fit:
                cost = offer[-1]
                for idx in range(len(_needs)):
                    _needs[idx] -= offer[idx]
                if cost < res:
                    cost = offer[-1]
                    res_need_list = _needs
                    _tmp = self.shoppingOffers(price, special, res_need_list)
                    cost_list.append(_tmp+cost)
        for _cost in cost_list:
            if _cost < res:
                res = _cost
        return res






'''
price = [2, 5]
special = [[3,0,5],[1,2,10]]
needs = [3, 2]
'''

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]

sol = Solution()
print sol.shoppingOffers(price, special, needs)



