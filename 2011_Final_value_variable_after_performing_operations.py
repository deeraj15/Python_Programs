comie=["++X","--X","X++","X--","X--",]#change the values to check the problem
sum=0
for i in comie:
    if i=="++X" or i=="X++":
        sum+=1
    else:
        sum-=1
print(sum)