class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []

        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        def dfs(start, hour, minute, cnt):
            if cnt == turnedOn:
                if hour < 12 and minute < 60:
                    result.append(f"{hour}:{minute:02d}")
                return

            for i in range(start, 10):
                if i < 4:
                    dfs(i + 1, hour + hours[i], minute, cnt + 1)
                else:
                    dfs(i + 1, hour, minute + minutes[i - 4], cnt + 1)

        dfs(0, 0, 0, 0)
        return result