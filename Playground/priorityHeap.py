import heapq

pq = []

queries = [
    [3,1,"task1",],[2,10,"task2",],[1,15,"task3",]
]

def solution(queries):
    for q in queries:
        priority = q[0]
        runAt = q[1]
        taskId = q[2]

        heapq.heappush(pq,(-priority,runAt,taskId))
    pass

solution(queries)

(priority,runAt,taskId) = heapq.heappop(pq)
print(-priority,runAt,taskId)

