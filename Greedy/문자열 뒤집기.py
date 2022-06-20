S=input()

num_0=0
num_1=0
idx=0

while idx<len(S):
    if S[idx]=='0':
        num_0+=1
        while idx<len(S) and S[idx]=='0':
            idx+=1
    else:
        num_1+=1
        while idx<len(S) and S[idx]=='1' :
            idx+=1

print(min(num_0,num_1))