class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        ## practice:
        nums_hash = {}

        for i,val in enumerate(nums):

            diff = target - val
            if diff in nums_hash :
                return [nums_hash.get(diff), i]

            nums_hash[val] = i 


        # num_hash = {}

        # for i,val in enumerate(nums):
        #     diff = target - val
        #     print(val, target, diff)

        #     if diff in num_hash:
        #         return [num_hash.get(diff), i]

        #     num_hash[val] = i

            


        # 2 pointer is not suitable for 2sum :(

        #NOTE: 
        # - if has to return True / False or the 2 integers , then can use list instead of hash
        # - if has to return the index of the integers , then use the dict / hash
        # - .index() method is not suitable 

        


        