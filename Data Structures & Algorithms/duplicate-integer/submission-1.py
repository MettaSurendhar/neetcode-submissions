class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # practice:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True

            nums_set.add(num)

        return False

    #     size = len(nums)
    #     al_size = len(set(nums))

    #     if al_size != size:
    #         return True

    #     return False
    # ----------
    #     set_nums = set()

    #     for num in nums:

    #         if num in set_nums:
    #             return True
    #         set_nums.add(num)

    #     return False

    # ---------------------
    # --- Hash set approach --- #
