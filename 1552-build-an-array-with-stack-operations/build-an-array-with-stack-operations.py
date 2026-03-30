class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        answer = []
        ptr = 0
        for i in range(1, n + 1):
            if ptr >= len(target):
                break

            stack.append(i)            
            answer.append("Push")

            if i != target[ptr]:
                stack.pop()
                answer.append("Pop")
            else:
                ptr += 1

        return  answer
