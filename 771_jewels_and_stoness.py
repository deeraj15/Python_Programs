stones="Aaaadnff"
jewels="Aa"
ans=""
for i in stones:
    for j in jewels:
        if i==j:
            ans+=i
print(len(ans))