class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## practice:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        if s_count != t_count:
            return False

        return True

        # ## Compare the Frequency: - Hashmap -v2

        # if len(s) != len(t):
        #     return False

        # s_hash = {}
        # t_hash = {}

        # for i in range(len(s)) :
        #     s_hash[s[i]] = s_hash.get(s[i], 0 ) + 1
        #     t_hash[t[i]] = t_hash.get(t[i], 0 ) + 1

        # if s_hash == t_hash:  # check both dicts has same keys with same values
        #     return True

        # return False

        # ## Compare the Frequency: - Hashmap - v1

        # s_hash = {}
        # t_hash = {}

        # for val in s:
        #     if val  in s_hash:
        #         s_hash[val] += 1  ## append
        #     else:
        #         s_hash[val] = 1  ## initialize

        # for val in t:
        #     if val in t_hash:
        #         t_hash[val] += 1  ## append
        #     else:
        #         t_hash[val] = 1  ## initialize

        # for key in s_hash:
        #     if key not in t_hash or s_hash[key] != t_hash[key]:
        #         return False

        # (or simple s_hash == t_hash is enough)
        # return True

        ## Rearranging - sorting - O(nlogn)
        # t = sorted(t)
        # s = sorted(s)

        # if t == s :
        #     return True
        # else:
        #     return False
