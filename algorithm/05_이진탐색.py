#순차 탐색 : 앞에서부터 하나씩 확인
#이진 탐색 : 장렬되어 있는 리스트에서,
#          탐색 범위를 절반씩 좁혀가며 탐색
#          시작점, 끝점, 중간점을 이용
#연산 횟수는 log2N에 비례
#시간복잡도 = O(logN)
print('이진 탐색 소스코드 구현(재귀 함수')
def binary_search(array, target, start, end):
  if start > end: #데이터가 존재하지 않음
    return None #None값을 반환
  
  mid = (start + end) // 2 #중간점 지정

  if array[mid] == target: #탐색 완료
    return mid
  elif array[mid] > target:
    #중간점이 찾으려는 값보다 크면 왼쪽 탐색
    return binary_search(array, target, start, mid - 1)
  else:
    #중간점이 찾으려는 값보다 작으면 오른쪽 탐색
    return binary_search(array, target, mid + 1, end)

print('n(원소의 개수)와 target(찾으려는 값) 입력 (10 7)')
n, target = map(int, input().split())
print('리스트 입력')
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print('원소가 존재하지 않습니다')
else:
  print(result + 1, '번째 원소입니다')

#유용한 파이썬 라이브러리
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print('정렬을 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스')
print(bisect_left(a, x))
print('정렬을 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스')
print(bisect_right(a, x))

#값이 특정 범위에 속하는 데이터 개수 구하기
def count_by_range(arr, left_value, right_value):
  right_index = bisect_right(arr, right_value)
  left_index = bisect_left(arr, left_value)
  return right_index - left_index

arr=[1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print('값이 4인 데이터 개수 : ', count_by_range(arr, 4, 4))
print('값이 [-1, 3] 범위에 있는 데이터 개수 : ', count_by_range(arr, -1, 3))

#파라메트릭 서치
#최적화 문제를 결정 문제(예/아니오)로 바꿔서 해결하는 방법
print('N(떡의 개수), M(떡의 길이) 입력 (4 6)')
n, m = map(int, input().split())
print('떡의 개별 높이')
dduk = list(map(int, input().split()))

#시작점, 끝점, 중간점 지정
start = 0
end = max(dduk)

result = 0
while start <= end:
  total = 0
  mid = (start + end) //2

  for x in array:
    #잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x - mid

    #떡의 양이 부족한 경우 더 많이 자르기
    #왼쪽 부분 탐색
    if total < m:
      end = mid - 1
    #떡의 양이 충분한 경우 덜 자르기
    #오른쪽 부분 탐색
    else:
      result = mid #최대한 덜 잘라야 하므로, 여기에서 result에 기록
      start = mid + 1

print(result)
      
#문제
#N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있을 때, 수열에서 X가 등장하는 횟수를 출력

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
  left_index = bisect_left(arr, left_value)
  right_index = bisect_right(arr, right_value)
  print('>>>>', bisect_left(arr, left_value), '>>>',bisect_right(arr, right_value))
  return right_index - left_index

print('N, X 입력 (7 2)')
n, x = map(int, input().split())
print('배열 입력')
arr = list(map(int, input().split(' ')))

count = count_by_range(arr, x, x)
if count == 0:
  print(-1) #x가 존재하지 않음
else:
  print(count)