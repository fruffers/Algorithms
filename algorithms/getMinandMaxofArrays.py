# use linear search

#  initialise min and max as first two eles. start at 3rd ele
# compare each ele with max and min, change the max and min accordingly

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

    def getMinMax(self,arr:list,n:int) -> pair:
        minmax = pair()

        # if one ele then return min and max of both
        if n == 1:
            minmax.max = arr[0]
            minmax.min = arr[0]
            return minmax
        
        

        

