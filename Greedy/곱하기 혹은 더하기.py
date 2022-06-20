S=input()
data=[]
for i in range(len(S)):
    if S[i]!='0': # 0삭제
        data.append(int(S[i]))

if data[0]!=1:
    slt=1
else:           
    slt=0

for i in data:
    if i==1:
        slt+=1
    else:
        slt*=i
print(slt)


