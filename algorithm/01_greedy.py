#그리디 알고리즘
#지금 당장 좋은 것만 고르는 알고리즘
#최적의 해를 보장할 수 없다


#(예제) 거스름돈 문제--------------------------------
#가장 적은 갯수로 거슬러주는 방법은?(500, 100, 50, 10원)
#가장 큰 화폐부터 거슬러 주면 된다
#> 큰 단위의 동전이 항상 작은 단위의 배수이므로

n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50 ,10]

for coin in array:
  count += n // coin #나뉘어질 때의 몫(정수)
  n %= coin #나뉘어질 때의 나머지(남은 금액)

print('최소 동전 개수는', count, '개')


#(문제) N이 1이 될 때까지 수행해야 하는 최소 횟수---------
#1. N에서 1을 뺍니다
#2. N을 K로 나눕니다
#N(1<=N<=100,000), K(2<=K<=100,000)

#내 풀이
print("n과 k 입력(25 7)")
n, k = map(int, input().split())
result = 0

while n > 1: #연산 종료 조건
  print("n : ", n)
  if n % k != 0: #나누어 떨어지지 않으면
    n -= 1
    result += 1
  else:
    n = n / k #나눈다
    result += 1

print('최소 수행 횟수는 ',result)

#답안 예시
print("n과 k 입력(25 7)")
n, k = map(int, input().split())
result = 0

while True:
  #N이 K로 나누어 떨어지는 수로 만든다
  target = (n//k) * k #(25//7)*7=(3)*7=21
  result += n - target #나누어 떨어지면 변화X
  n = target

  if(n < k):  #나눌 수 없을 때 반복문 탈출
    break

  #나누기
  result += 1
  n //= k

#마지막에 남은 수에 대하여 1씩 뺴기
result += (n - 1)
print('최소 수행 횟수는 ', result)


#(문제) 0~9로 이루어진 문자열 S를 'x'혹은 '+'를 넣어 최댓값을 구하시오
print("0~9로 이루어진 문자열 S")
data = input()
result = int(data[0]) #첫번째 문자로 초기화

for i in range(1, len(data)):
  #두 수 중 하나라도 '0'/'1'이면 덧셈
  num = int(data[i])
  if result <= 1 or num <= 1:
    result += num
  else:
    result *= num

print(result)


#공포도가 X이상인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹에 참여해야 한다(참여 안해도 됨)
#최대 그룹 수는?
print("총 몇명?")
n = int(input())
print("명수대로 공포도 입력")
frig = list(map(int, input().split()))
frig.sort()

result = 0 #총 그룹 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in frig:
  count += 1
  if count >= i:
    result += 1 #총 그룹 수 체크
    count = 0

print(result)