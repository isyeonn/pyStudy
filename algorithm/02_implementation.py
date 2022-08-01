#구현

#행렬 : 주로 2차원 공간을 나타낼 때 사용
matx = ''
for i in range(5):
  for j in range(5):
    matx += str('(' + str(i) + ',' + str(j) + ')')
  matx  += '\n'
print(matx)

#(문제) 여행가 A가 최종적으로 도착할 지점의 좌표 (x, y)
#NXN을 벗어나면 무시
#움직임 : U / D / R / L
#(1, 1)에서 시작

# x, y 좌표의 변화
# U : -1, 0 (**생각과 다름, 행렬 값 보고 할 것)
# D : +1, 0
# R : +0, +1
# L : +0, -1

#배열에 담으면
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_type = ['U', 'D', 'R', 'L']

print('크기 입력 (5)')
n = int(input()) #크기

print('이동계획 입력 (R R R U D D)')
x, y = 1, 1 #출발점 셋팅
plans = input().split() #이동계획

for plan in plans:
  for i in range(len(move_type)):
    if(plan == move_type[i]):
      nx = x + dx[i]
      ny = y + dy[i]
      #공간을 벗어나면 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny
  print(x,'>>>>',y)

print(x, y)


#문제
#00시 00분 00초부터 N시 59분 59초 까지 중
#3이 하나라도 포함되는 모든 경우의 수 출력
print('N을 입력 (5)')
t = int(input())
result = 0

for h in range(t + 1): #시
  for m in range(60): #분
    for s in range(60):#초
      if '3' in str(h) + str(m) + str(s):
        result += 1

print(result)


#문제
#8X8좌표(a1 ~ h8) 안에서 나이트가 갈 수 있는 경우의 수
#수평 두 칸 + 수직 한 칸 가능
#수직 두 칸 + 수평 한 칸 가능
print('시작 좌표 (a1)')
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
#ord() : 문자를 유니코드로 변환

#나이트가 이동할 수 있는 모든 뱡향 정의 (8가지)
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0

for step in steps:
  #이동하게 될 위치
  next_row = row + step[0]
  next_column = column + step[1]
  #이동이 가능한지 확인
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1


print(result)


#문제
print('알파벳 대문자와 숫자(0~9)로 이루어진 문자열 입력 (K1KA5CBC7)')
#문자열을 정렬해서, 숫자는 모두 더해서 출력
data = input()
result = []
value = 0

for x in data:
  if x.isalpha(): #알파벳 체크
    result.append(x)
  else:
    value += int(x)

result.sort() #오름차순으로 정렬

if value != 0:
  result.append(str(value))

#리스트를 문자열로 변환하여 출력 ****
print(''.join(result))