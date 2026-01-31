from collections import deque, defaultdict
from typing import List


def solution(queries: List[List[str]]) -> List[str]:
    out = []

    W = None  # windowSeconds

    # Store events in chronological order (time increasing) for O(1) pruning
    # Each event: (time:int, userId:str, eventType:str)
    events = deque()

    # Rolling counts for the active window
    type_count = defaultdict(int)  # eventType -> count in window
    user_count = defaultdict(int)  # userId -> count in window

    # Track last processed time to support pruning correctly
    last_time = None

    def prune(current_time: int) -> None:
        """
        Remove events with time <= (current_time - W),
        because the window is (current_time - W, current_time].
        """
        nonlocal events
        cutoff = current_time - W
        while events and events[0][0] <= cutoff:
            t, u, et = events.popleft()
            type_count[et] -= 1
            if type_count[et] == 0:
                del type_count[et]

            user_count[u] -= 1
            if user_count[u] == 0:
                del user_count[u]

    for q in queries:
        op = q[0]

        if op == "INIT":
            W = int(q[1])
            events.clear()
            type_count.clear()
            user_count.clear()
            last_time = None
            out.append("true")

        elif op == "LOG":
            # LOG time userId eventType
            t = int(q[1])
            userId = q[2]
            eventType = q[3]

            # For typical OA inputs, times are non-decreasing overall.
            # We prune on each time-bearing operation.
            if last_time is None or t >= last_time:
                prune(t)
                last_time = t
            else:
                # If time goes backwards, deque-pruning cannot be correct.
                # For simplicity in OA context, we assume this doesn't happen.
                # You could rebuild from stored history if needed.
                prune(last_time)

            # Append new event (assumes chronological order)
            events.append((t, userId, eventType))
            type_count[eventType] += 1
            user_count[userId] += 1
            out.append("true")

        elif op == "COUNT":
            # COUNT time eventType
            t = int(q[1])
            eventType = q[2]

            if last_time is None or t >= last_time:
                prune(t)
                last_time = t
            else:
                prune(last_time)

            out.append(str(type_count.get(eventType, 0)))

        elif op == "COUNT_USER":
            # COUNT_USER time userId
            t = int(q[1])
            userId = q[2]

            if last_time is None or t >= last_time:
                prune(t)
                last_time = t
            else:
                prune(last_time)

            out.append(str(user_count.get(userId, 0)))

        elif op == "TOP":
            # TOP time k
            t = int(q[1])
            k = int(q[2])

            if last_time is None or t >= last_time:
                prune(t)
                last_time = t
            else:
                prune(last_time)

            if not type_count:
                out.append("")
                continue

            # Sort by: count desc, then eventType asc
            items = sorted(type_count.items(), key=lambda kv: (-kv[1], kv[0]))
            items = items[:k]
            out.append(",".join(f"{etype}({cnt})" for etype, cnt in items))

        else:
            # Unknown op (shouldn't happen in OA)
            out.append("")

    return out


# Quick sanity check (optional)
if __name__ == "__main__":
    queries = [
        ["INIT", "10"],
        ["LOG", "1", "alice", "login"],
        ["LOG", "2", "alice", "view"],
        ["LOG", "3", "bob", "view"],
        ["LOG", "4", "alice", "click"],
        ["LOG", "6", "alice", "click"],
        ["COUNT", "6", "click"],
        ["COUNT_USER", "6", "alice"],
        ["TOP", "6", "3"],
        ["TOP", "20", "3"],  # window (10,20] => empty => ""
    ]
    print(solution(queries))
    # Expected:
    # ["true","true","true","true","true","true","2","4","click(2),view(2),login(1)",""]
