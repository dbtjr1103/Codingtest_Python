def solution(n, vertex):
    from collections import deque
    
    # 그래프(인접 리스트) 생성
    graph = [[] for _ in range(n+1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS 초기 설정
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    queue = deque([1])
    visited[1] = True
    
    # BFS로 최단 거리 계산
    while queue:
        current = queue.popleft()
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                distance[nxt] = distance[current] + 1
                queue.append(nxt)
    
    # 가장 멀리 떨어진 거리(max_dist)와 해당 거리 노드 수 반환
    max_dist = max(distance)
    return distance.count(max_dist)
