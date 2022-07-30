#기본 입출력-------------------------------------
print("입력할 갯수")
n = int(input())
print("입력하세요")
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

print("3개의 정수 입력", end=' :')
a, b, c = map(int, input().split())
print("a = ", a, ", b= ", b, ", c = ", c)

import sys
print("빠르게 입력받기")
data = sys.stdin.readline().rstrip()
print(data)

answer = 7
print(f"정답은 {answer}입니다.")
