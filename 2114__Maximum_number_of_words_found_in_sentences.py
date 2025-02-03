li=["comie is a boy","comie plays","he is a"]
ans=0
for i in range(len(li)):
    s=li[i]
    temp=1
    for j in range(len(s)):
        ab=s[j]
        if ab==" ":
            temp+=1
        ans=max(ans,temp)
print(ans)
