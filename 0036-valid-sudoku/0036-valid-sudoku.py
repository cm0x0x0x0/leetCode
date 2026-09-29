class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        size = 9

        def validateEachRow():
            for r in range(size):
                dup = set()
                for c in range(size):
                    num = board[r][c]
                    if num == ".":
                        continue

                    if num in dup:
                        return False

                    dup.add(num)

            return True

        def validateEachCol():
            for c in range(size):
                dup = set()
                for r in range(size):
                    num = board[r][c]
                    if num == ".":
                        continue

                    if num in dup:
                        return False

                    dup.add(num)
            
            return True
        
        def validateEachBox():
            # 0-2
            for s in range(0, 7, 3):
                dup = set()
                for r in range(0, 3):
                    for c in range(0, 3):
                        num = board[r][c+s]
                        print(r, c+s, num)
                        if num == ".":
                            continue
                        
                        if num in dup:
                            return False

                        dup.add(num)

            # 3-5
            for s in range(0, 7, 3):
                dup = set()
                for r in range(3, 6):
                    for c in range(0, 3):
                        num = board[r][c+s]
                        if num == ".":
                            continue
                        
                        if num in dup:
                            return False

                        dup.add(num)

            # 6-8
            for s in range(0, 7, 3):
                dup = set()
                for r in range(6, 9):
                    for c in range(0, 3):
                        num = board[r][c+s]
                        if num == ".":
                            continue
                        
                        if num in dup:
                            return False

                        dup.add(num)

            return True

        return validateEachRow() and validateEachCol() and validateEachBox()