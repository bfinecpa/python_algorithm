#큰 수의 법칙
#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 문제

#입력 조건 첫째줄에 N,M,K 주어진다. 둘째 줄에 N개의 자연수가 주어진다.
#ex) 5 8 3 // 2 4 5 4 6  => 46


#입력
N,M,K = map(int,input().split())
N_list = list(map(int,input().split()))

N_list.sort()
cnt=0
val=0
for i in range(M):
    if cnt<K:
        val+=N_list[-1]
        cnt+=1
    else:
        val+=N_list[-2]
        cnt=0
print(val)
#위 방식은 단순하게 푸는 방식 -> N이 100억 이상이면 시간초과 -> 수학적으로 풀면 100억도 가능
