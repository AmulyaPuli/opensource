s=input()
r=""
count = 1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        r+=s[i-1]+str(count)
        count=1
r+=s[-1]+str(count) 
print(r)