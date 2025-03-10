nums=[4,5,3,2,2,4,5,6]
dici={}
for i in nums:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
ans=0
for i in dici:
    n=dici[i]
    temp=n*(n-1)/2
    ans+=temp
print(int(ans))