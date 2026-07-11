from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hash_map = defaultdict(list)
        for str in strs: 
            count = [0]*26  # [0,0,0,...0]
            for char in str:
                count[ord(char) - ord('a')] +=1  # find index of that char, i.e a=0, b=1, c=2
            hash_map[tuple(count)].append(str)

        return list(hash_map.values())
            

        ## Hash map 
        ## NOTE: 
        ##      key : value
        ##      (1,1,1,0,0,0,....0) : ['cab']
        ##      -------------------
        ##      count of char in 26 len

        # ana_hash = defaultdict(list)

        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1

        #     ana_hash[tuple(count)].append(s)

        # print(ana_hash)
        
        # ana_list = list(ana_hash.values())


        # return ana_list