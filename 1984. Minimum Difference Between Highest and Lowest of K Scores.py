nums = [3,4,8,1,5,9,3,1,2]
nums.sort()
n=len(nums)
k=3
l=0
ans=float("inf")
for r in range(n):
    if(r-l==k):
        l+=1
    if(r-l+1==k):
        ans=min(ans,nums[r]-nums[l])
print(ans)
    