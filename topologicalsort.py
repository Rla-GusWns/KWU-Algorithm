def topologicalSort2(graph):
    visited = {node: False for node in graph}  # Fasle로 만들어
    list = []  # 위상 정렬 결과를 저장할 리스트

    def DFS(node):
        visited[node] = True  # True 처리
        for v in graph[node]:
            if not visited[v]:
                DFS(v)  # 현재 노드의 이웃 노드를 방문
        list.append(node)  # 연결리스트에 넣어
    for node in graph:
        if not visited[node]:
            DFS(node)

    list.reverse()  # 리스트 역순으로 변환하여 위상 정렬 결과 생성

    return list