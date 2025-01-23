def calculatesum(n):
    if(n<=0):
        return 0
    fib=[0]*(n+1)
    fib[1]=1
    sum=fib[0]+fib[1]
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
        sum=sum+fib[i]

    return sum
n=4
print("sum of fibonacci is: ",calculatesum(n))