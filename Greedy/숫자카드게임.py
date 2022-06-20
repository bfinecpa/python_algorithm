#숫자 카드 게임

#문제: 가장 높은 숫자를 뽑는 문제, N X M의 행렬형태를 가진 숫자가 있다. 
#뽑을 숫자의 행의 숫자르 가져온 후 행에서 가장 작은 숫자를 뽑는다.

#입력: 첫째줄, N,M 둘째줄 N개 줄을 거친 숫자 주어진다. 

N,M=map(int,input().split())

lst_n=0

for i in range(N):
    data=list(map(int,input().split()))
    data.sort()
    if data[0]>lst_n:
        lst_n=data[0]

print(lst_n)

#실제 풀이에서는 min(), max()를 쓰자 시간복잡도가 n이다. sort는 nlogn이다. 필요한 것을 정확하게 알 필요가 있다.
