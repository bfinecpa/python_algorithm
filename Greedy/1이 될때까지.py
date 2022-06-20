#1이 될때까지

#입력 첫째줄: N,K 자연수 이때 N은 항상 K보다 크다.
#출력 : 최소 횟수

N,K= map(int, input().split())
cnt=0


while N!=1:
    if N%K==0:
        N=N//K
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt)

