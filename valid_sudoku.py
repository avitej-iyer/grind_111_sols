class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                curr_ele = board[i][j]
                if curr_ele != ".":
                    res += [(i, curr_ele)]
                    res += [(curr_ele, j)]
                    res += [(i//3, j//3, curr_ele)]

        return len(res) == len(set(res))            