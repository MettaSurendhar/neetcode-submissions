class Solution:

    def encode(self, strs: List[str]) -> str:

        res=""
        for s in strs:
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:

        res=[]
        i=0

        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            ln = int(s[i:j])
            string = s[j+1:j+ln+1]
            res.append(string)
            i=j+ln+1
        
        return res
