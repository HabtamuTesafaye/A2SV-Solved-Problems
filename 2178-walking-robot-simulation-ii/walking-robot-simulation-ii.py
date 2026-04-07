class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0

        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir_names = ["East","North","West","South"]
        self.d = 0

        self.perimeter = 2 * (width + height) - 4
        self.started = False

    def step(self, num: int) -> None:
        num %= self.perimeter

        # 🔥 critical logic
        if num == 0:
            if not self.started:
                self.d = 3  # South
                self.started = True
            return

        self.started = True

        while num > 0:
            dx, dy = self.dirs[self.d]
            nx, ny = self.x + dx, self.y + dy

            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.d = (self.d + 1) % 4
                continue

            self.x, self.y = nx, ny
            num -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        
    def getDir(self) -> str:
        return self.dir_names[self.d]