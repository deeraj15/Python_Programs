s=set()
nums=[2,4,5,2,7,5]
missing=10000
duplicate=10000
for i in range(len(nums)):
    if nums[i] not in s:
        s.add(nums[i])
    else:
        duplicate=nums[i]
for i in range(1,len(nums)+1):
    if i not in s:
        missing=i
print(duplicate,missing)
