#정렬 (Sorting)

#선택정렬
#시간복잡도 = (N2 + N - 2 ) / 2 = O(N2)
#처리되지 않은 데이터 중 가장 작은 데이터를 맨 앞에 있는 데이터와 바꾼다
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i #가장 작은 데이터 temp 초기화
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  #스와프
  array[i], array[min_index] = array[min_index], array[i]

print(array)

#삽입정렬
#시간복잡도 = O(N2) : 중첩 for 문
#처리되지 않은 데이털ㄹ 하나씩 골라 적절한 위치에 삽입
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): #range(start, stop, step)
    if array[j - 1] > array[j]: #이전 것보다 작으면
      array[j - 1], array[j] = array[j], array[j - 1]#바꿔준다
    else: #아니면 멈춘다
      break

print(array)

#퀵정렬
#시간복잡도 = O(NlogN)
#최악의 경우 O(N2)
#피벗 : 기준, 기본적인 퀵정렬은 첫번째 데이터
#기준보다 큰 데이터(왼쪽부터 시작)와 작은 데이터의(오른쪽부터 시작) 위치를 바꿈
#위치가 엇갈리는 경우 피벗과 작은 데이터의 위치를 변경

#병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간(c, java, python)
#표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    #피벗보다 작은 데이터를 칮을때 까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    #피벗보다 작은 데이터를 찾을 때까지 반복
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right): #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#파이썬의 장점을 살린 방식
def py_quick_sort(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) < 2:
    return array
  pivot = array[0]
  tail = array[1:] #1번째 원소부터 생략시 마지막 원소까지

  left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
  return py_quick_sort(left_side) + [pivot] + py_quick_sort(right_side)

print(py_quick_sort(array))

#계수정렬
#데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 떄 사용
#데이터의 개수가 N, 데이터(양수) 중 최대값 K
#최악의 경우에도 수행시간 = O(N + K)
#시간복잡도, 공간복잡도 모두 O(N + K)
#매우 빠름, 공간복잡도는 높음

#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 #값에 해당하는 인덱스에 개수 체크

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

print('\n\n')
print('선택 정렬과 기본 정렬 라이브러리 수행 시간 비교')
from random import randint
import time

#배열에 10,000개의 정수를 삽입
array = []
for _ in range(5000):
  #1부터 100 사이의 랜덤한 정수
  array.append(randint(1, 100))

#선택 정렬 프로그램 성능 측정
start_time = time.time()

#선택 정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_array = j
  array[i], array[min_index] = array[min_index], array[i]

#측정 완료
end_time = time.time()
#수행 시간 출력
print('선택 정렬 성능 측정 : ', end_time - start_time, '초')

#배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(5000):
  array.append(randint(1, 100))

start_time = time.time()

#기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()

print('기본 정렬 라이브러리 성능 측정 : ', end_time - start_time, '초')

#문제
#두 배열 A, B
#N개의 원소, K번의 바꿔치기 후에 배열 A의 합이 최대가 되도록 합을 출력
print('n, k 입력 (5 3)')
n, k = map(int, input().split())
print('배열 A, 배열 B 입력')
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

for i in range(k):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break

print(sum(A))