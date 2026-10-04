class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for start, end in edges:
            root_start = find(start)
            root_end = find(end)

            # 같은 그룹이면 이미 연결되어 있으므로 사이클 발생
            if root_start == root_end:
                return [start, end]

            # 작은 그룹을 큰 그룹에 합침
            if size[root_start] >= size[root_end]:
                # start 쪽 그룹이 더 크거나 같음
                # → end 쪽 그룹을 start 쪽 그룹에 합침
                parent[root_end] = root_start
                size[root_start] += size[root_end]
            else:
                # end 쪽 그룹이 더 큼
                # → start 쪽 그룹을 end 쪽 그룹에 합침
                parent[root_start] = root_end
                size[root_end] += size[root_start]

        return []