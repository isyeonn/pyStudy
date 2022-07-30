#조건문 간소화
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

if 10 < score < 90:
  print("합격입니다")

print("1부터 9까지 홀수의 합")
i = 1
sum = 0
while i < 10:
  if i % 2 == 1:
    sum += i
  i += 1
print("sum = ", sum)

scores = [40, 70, 65, 80, 95]
cheating_student = {3, 4}

for i in range(5):
  if i + 1 in cheating_student:
    continue
  elif scores[i] >= 70:
    print(i + 1, "번 학생은 합격입니다.")


#함수
index = 0

def func(a, b):
  global index
  index += 1
  add = a + b
  return index, add

t, y = func(b = 7, a = 1)
print("index : ", t, "add_var : ", y)

#람다 표현식 (함수)(파라미터)
print( (lambda a, b: a + b)(3, 7) )

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
#(1) 일반
def my_key(x):
  return x[1]

#sorted(배열, 정렬기준:배열의 원소 기준)
print(sorted(array, key=my_key))

#(2) 람다
print(sorted(array, key=lambda x:x[1]))

print(array)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

#map : 각각의 원소에 함수를 적용

#map(함수, 배열1, 배열2)
result = map(lambda a, b: a+b, list1, list2)
print(list(result))

#순열과 조합
from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data, 3)) #모든 순열 구하기
print(result)

from itertools import combinations
result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result)


#Counter
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue']) #객체 선언

print("counter['blue']", counter['blue'])
print("counter['red']", counter['red'])
print(dict(counter)) #사전 자료형으로 반환

#최대공약수와 최소공배수
import math

def lcm(a, b):
  return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) #죄대공약수
print(lcm(a, b)) #최소공배수
  