from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ## Practice : 
        
        # freq map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # freq bucket
        freq_bucket = [[] for i in range(len(nums)+1)]

        # freq map to freq bucket 
        for num,freq in freq_map.items():
            freq_bucket[freq].append(num)

        # res of k values
        res = []
        bucket_i = len(freq_bucket) - 1
        while bucket_i > 0 and len(res)<k:
            for item in freq_bucket[bucket_i]:
                res.append(item)
            bucket_i -=1
        
        return res
        

        ## Bucket sort technique: O(t) = n + m
        ## NOTE: 
        ## bucket: [ [ ],[ ],[ ],[ ] ]
        ## freq:      0   1   2   3
        ## eg of nums = [1,2,3,3,7,7,7]
        ##  [ [], [1,2], [3], [7] ]

        # freq_hashmap = defaultdict(int)

        # for num in nums:
        #     freq_hashmap[num] += 1

        # freq_bucket = [[] for i in range(len(nums) + 1)]  # O(t) = n

        # for key,freq in freq_hashmap.items():  # O(t) = n
        #     freq_bucket[freq].append(key)
        
        # res=[]
        # i = len(freq_bucket) - 1
        
        # while i>=0 and len(res) < k:  # O(t) = m
        #     for item in freq_bucket[i]:
        #         res.append(item)
        #     i-=1
            
        # return res

        ## Min-heap technique  O(t) = mlogk + k

        # freq_hashmap = defaultdict(int)

        # for num in nums:
        #     freq_hashmap[num] += 1

        # heap = []

        # for key,freq in freq_hashmap.items():  # O(t) = m
        #     heappush(heap, (freq,key))  # O(t) = logk

        #     if len(heap) > k:  
        #         heappop(heap)  # min freq tuple will be removed

        # res=[]

        # for val in heap:  # O(t) = k
        #     res.append(val[1])

        # return res

        
        
        ## Sorting technique O(t) = n + m + mlogm + k

        # freq_hashmap = defaultdict(int)

        # for num in nums: # O(t) = n
        #     freq_hashmap[num] += 1
            
        # freq_list = []
        # for key,freq in freq_hashmap.items():  # O(t) = m
        #     freq_list.append([freq,key])

        # freq_list.sort()  # O(t) = mlogm

        # res=[]
        # for _ in range(k):  # O(t) = k
        #     _ , val = freq_list.pop()
        #     res.append(val)

        # return res