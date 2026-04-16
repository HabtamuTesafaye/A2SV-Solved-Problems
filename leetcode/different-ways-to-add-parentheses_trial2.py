class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            char = expression[i]
            if char in "+-*":
                left_res = self.diffWaysToCompute(expression[:i])
                right_res = self.diffWaysToCompute(expression[i + 1:])
                for l in left_res:
                    for  r in right_res:
                        if char == "+":
                            result.append(l + r)
                        elif char == "-":
                            result.append(l - r)
                        elif char == "*":
                            result.append(l * r)

        if not result:
            result.append(int(expression))

        return result