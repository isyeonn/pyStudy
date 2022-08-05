#다이나믹 프로그래밍
#메모리를 적절하게 사용해서 수행 시간 효율성을 비약적으로 향상
#이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장해서 재계산 방지
#일반적으로 탑다운과 보텀업으로 구성된다
#조건
#최적 부분 구조 : 작은 답을 모아서 큰 문제를 해결
#중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결

#메모이제이션 Memoization
#캐싱
#DP 테이블 : 결과 저장용 리스트

#피보나치 수열
#일반
#시간 복잡도 = O(2의 N제곱) : 매우 복잡
def fibo(x):
  if x < 3:
    return 1
  else:
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

#탑다운 - 메모이제이션
dp = [0] * 100
#한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화

def fibo(x):
  if x == 1 or x == 2:
    return 1
  else : 
    if dp[x] != 0:
      return dp[x]
    else:
      dp[x] = fibo(x - 1) + fibo(x - 2)
      return dp[x]

print(fibo(99))

#동작 분석
#시간복잡도 : O(N)
d = [0] * 100

def fibo(x):
  print('f(' + str(x) + ')', end=' ')
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  else:
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)
print()

#보텀업
dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])

for i in range(3):
  print(i) #0/1/2 출력

#다이나믹 프로그래밍은 풀이 과정을 생각하는 데 많은 시간이 걸리므로
#보통 기본문제가 출제된다
  
#개미전사
#식량창고에서 얻을 수 있는 식량의 최대값 출력
#인접한 창고는 털 수 없다
print('식량창고 개수 입력 (4)')
n = int(input())
print('식량의 개수 입력')
k = list(map(int, input().split()))

#왼쪽부터 차례대로 식량창고를 털 때, i번째 식량창고를 털지 말지는
#i-1의 식량 갯수와 i-2에 i번째를 더한 식량 갯수를 비교한다
dp = [0] * 100 #식량창고의 범위

dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, n):
  dp[i] = max(dp[i - 1], dp[i - 2] + k[i])

print(dp[n - 1])

#1로 만들기
#최소 연산 횟수로 1을 만들자
#X가 5로 나누어 떨어지면, 5로 나눈다
#X가 3으로 나누어 떨어지면, 3으로 나눈다
#X가 2로 나누어 떨어지면, 2로 나눈다
#X에서 1을 뺀다
print('연산할 X 입력 (26)')
x = int(input())

arr = [0] * 30001
#5/3/2로 나누었을 때 최소 값 -> 최적의 해

for i in range(2, x + 1):
  #
  d[i] = d[i - 1] + 1
  #
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  #
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  #
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

#효율적인 화폐구성
#N가지 종류의 화폐로 M원을 만들기 위한 최소한의 화폐 개수
#불가능할 때는 -1을 출력
print('화폐종류, 총 금액 입력 (2 15)')
n, m = map(int, input().split())

array = []
for i in range(n):
  array.append(int(input()))

#한 번 계산된 결과를 저장
#INF : 무한대, 만들 수 없음 : 최대값 + 1로 표현 : 로 초기화
dp = [10001] * (m + 1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    #(i - k)원을 만드는 방법이 존재하는 경우
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)

#계산된 결과 출력
if d[m] == 10001:
  print(-1)
else:
  print(d[m])


#금광 문제
#N X M 크기의 금광
#오른쪽/오른쪽 위/오른쪽 아래로 이동 가능
#얻을 수 있는 금의 최대 크기
print('총 실행 수 (2)')
for t in range(int(input())):
  print('n, m 입력 (3 4)')
  n, m = map(int, input().split())
  print('금광 입력 (1 3 3 2 2 1 4 1 0 6 4 7)')
  arr = list(map(int, input().split()))

  #금광의 모든 위치에서 고려할 사항
  #왼쪽 위/왼쪽/왼쪽 아래에서 오는 경우
  #세 가지만 고려한다
  
  #DP테이블 구성
  #첫 열에는 금광의 값
  #두번째 열 부터는 합산을 작성
  #마지막 열 중에 최대값을 출력
  dp = []
  index = 0

  for i in range(n):
    #m단위로 슬라이싱해서 증가시킴
    dp.append(arr[index:index + m])
    index += m

  #다이나믹 프로그램 진행
  #열 단위로 테이블 갱신
  for j in range(1, m):
    for i in range(n):
      #왼쪽 위에서 오는 경우
      if i == 0 : left_up = 0
      else: left_up = dp[i - 1][j - 1]
        
      #왼쪽 아래에서 오는 경우
      if i == n - 1: left_down = 0
      else: left_down = dp[i + 1][j - 1]
        
      #왼쪽에서 오는 경우
      left = dp[i][j - 1]
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)
  result = 0
  for i in range(n):
      result = max(result, dp[i][m - 1])
  print(result)

                 
#병사 배치하기
#N명의 병사 중 전투력이 높은 병사가 앞에 오도록 내림차순
#남아 있는 병사의 수가 최대가 되도록 할 때, 열외시켜야 하는 병사의 수
#가장 긴 증가하는 부분수열(LIS)
#점화식 : 모든 0<=j<i, d[i] = max(d[i],d[j]+1) if array[j]<array[i]
#DP 테이블 구성 : 이전 값보다 큰 값이 나오면 +1을 해당 인덱스에 저장
#마지막에 입력된 값이 가장 긴 증가하는 부분수열의 길이
                 
print('n 입력 (7)')
n = int(input())
print('전투력 입력 (15 11 4 8 5 2 4)')
array = list(map(int, input().split()))
#순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

dp = [1] * n

#가장 긴 증가하는 부분 수열 알고리즘 (LIS)
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

#열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
                 