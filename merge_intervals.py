class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=sorted(intervals,key=lambda x:x[0])
        s=l[0][0]
        e=l[0][1]
        res=[]
        for i in range(1,len(l)):
            if l[i][0]<=e:
                e=max(l[i][1],e)
            else:
                res.append([s,e])
                s=l[i][0]
                e=l[i][1]
        res.append([s,e])
        return res

