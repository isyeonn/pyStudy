a = 5
print(a)

b = -.7
print(b)

#지수
c = int(1e7)
print(c) #10의 7제곱

#소수점 계산
a = 0.3 + 0.6
print(a)
print(round(a, 4))

if round(a, 4) == 0.9:
  print(True)
elif round(a, 4) == 1:
  #아무것도 처리하고 싶지 않을 때
  pass
else:
  print(False)


d = 7
f = 3

#나누기
print(d / f)
#나머지 와 몫
print(d % f , "and", d // f)

#크기가 N이고, 모든 값이 0인 1차원 리스트
n = 10
a = [0] * n
print(a)

a = [i for i in range(10)]
print(a)
#뒤에서 세 번째 원소 출력
print(a[-3])
print(a[1 : 4])

#리스트 컴프리헨션
#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array =  [i for i in range(1, 19) if i%2 == 1]
print(array)
#M X N 크기의 2차원 리스트
m = 2
n = 3
#반복을 수행하되 반복을 위한 변수의 값을 무시
array = [[0]*m for _ in range(n)]
print(array)

#리스트 관련 기타 메서드
a = [1, 4, 3]

a.append(2)
print(a)

a.sort()
print(a)

a.sort(reverse = True)
print(a)

a.reverse()
print("원소 뒤집기", a)

a.insert(2, 3)
a.insert(2, 3)
print("인덱스 2에 값 3을 추가", a)
print("값이 3인 데이터 갯수", a.count(3))

a.remove(3)
print("값이 3인 데이터 삭제. 히니민", a)

remove_set = {3, 4}
result = [i for i in a if i not in remove_set]
print("집합 자료형에 없는 데이터 모두 제거", result)

#문자열 연산
st = "String"
print(st * 3)
print(st[2 : 4])

#튜플
print("튜플은 값의 변경 불가능, 공간효율적이다")

a = (1,2,3,4,5,6,7)
print(a)

#사전 자료형
print("사전 자료형은 변경 불가능한 자료형을 키로 사용")
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

data2 = {
  '홍길동' : 97,
  '이순신' : 89
}
print(data2)

key_list = data.keys()
value_list = list(data.values())
print("키만 담은 리스트", key_list)
print("값만 담은 리스트", value_list)

print("중복을 허용하지 않는 집합 자료형")
data = set([1,1,2,3,4,4,4,5])
print("data", data)

data2 = {3,3,3,4,4,5}
print("data2", data2)

print("합집합", data | data2)
print("교집합", data & data2)
print("차집합", data - data2)

data.add(7)
print("원소 추가", data)

data.update([9, 10])
print("여러 개 추가", data)

data.remove(7)
print("원소 삭제", data)