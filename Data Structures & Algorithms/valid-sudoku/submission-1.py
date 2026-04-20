class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(n^2) Space: O(n)
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1  # maps to bit position 0 - 8
                if rows[r] & 1 << val:
                    return False
                if cols[c] & 1 << val:
                    return False
                if squares[r // 3 * 3 + c // 3] & 1 << val:
                    return False

                rows[r] |= 1 << val
                cols[c] |= 1 << val
                squares[r // 3 * 3 + c // 3] |= 1 << val

        return True
