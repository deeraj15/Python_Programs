prices=[7,1,5,3,6,4]
minnval=prices[0]
anss=0
for i in range(1,len(prices)):
        anss=max(anss,(prices[i]-minnval))
        minnval=min(minnval,prices[i])
print(anss)