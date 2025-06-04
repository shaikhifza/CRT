'''
def count_frequencies(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq
arr=list(map(int,input().split()))
frquencies=count_frequencies(arr)
for i,count in frquencies.items():
    print(f"{i}-{count}",end=" ")
'''
#frequency of a given number:
'''
class Solution:
    def findFrequency(self, arr, x):
        # code here
        d={}
        for i in arr:
           if i in d:
               d[i]+=1
           else:
               d[i]=1
        ans=d.get(x)
        if(ans!=None):
            return ans
        elif(ans==None):
            return 0
'''
#find a number that appear more than once
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    ans=d.values()
    if(ans!=1):
        
    else:
        print(0)
