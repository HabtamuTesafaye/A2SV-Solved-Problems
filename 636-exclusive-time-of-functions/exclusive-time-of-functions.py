class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        answer = [0] * n
        prev_time = 0

        for log in logs:
            parts = log.split(':')
            func_id = int(parts[0])
            event_type = parts[1]
            time = int(parts[2])


            if stack:
                if event_type == "start":
                    answer[stack[-1]] += time - prev_time
                else:
                    answer[stack[-1]] += time - prev_time + 1
                
            if event_type == "start":
                stack.append(func_id)
                prev_time = time
            else:
                stack.pop()
                prev_time = time + 1
        
        return answer