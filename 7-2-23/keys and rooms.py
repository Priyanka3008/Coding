class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit=set()
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for i in rooms[node]:
                dfs(i)
        dfs(0)
        return len(visit)==len(rooms)
