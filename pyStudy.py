#최단 경로 문제
#한 지점에서 다른 한 지점까지의 최단 경로
#한 지점에서 다른 모든 지점까지의 최단 경로
#모든 지점에서 다른 모든 지점까지의 최단 경로

#다익스트라 최단 경로 알고리즘
#특정 노드에서 다른 모든 노드로 가는 최단 경로
#그리디 알고리즘/다이나믹 프로그래밍

#동작 과정
#1. 출발 노드를 설정
#2. 최단 거리 테이블을 초기화(자기 자신으로는 0)
#3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택 -> 그리디
#4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 갱신
#5. 3번과 4번을 반복



def solution(servers, sticky, requests):
    index = 0
    l = len(requests)

    answer = [[] * (l // servers) for _ in range(servers)]

    if sticky:
        #값으로 비교
        for r in requests:
            x =  requests[index] % servers
            if x == 0:
              answer[servers - 1].append(requests[index])
            else:
              answer[x - 1].append(requests[index])
            index += 1

    else:
        #인덱스로 비교
      for indx in range(l):
        x = indx % servers
        answer[x].append(requests[indx])
        
    return answer


print(solution(2, True, [1, 1, 2, 2]))
print(solution(2, True, [1, 2, 2, 3, 4, 1]))
print(solution(2, False, [1, 2, 3, 4]))