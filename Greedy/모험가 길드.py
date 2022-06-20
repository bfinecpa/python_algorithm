N=input()

data = list(map(int,input().split()))

data.sort(reverse=True)
cnt=0

while data:
    cur_slt=[]
    while True:
        cur_slt.append(data.pop())
        if len(cur_slt)==cur_slt[-1]:
            cnt+=1
            break
        if len(data)==0:
            break
print(cnt)
