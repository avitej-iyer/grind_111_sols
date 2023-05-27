class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        for x in range(rows):
            for y in range(cols):
                if mat[x][y]:
                    left_scan = mat[x][y-1] + 1 if y > 0 else 999999
                    top_scan = mat[x-1][y] + 1 if x > 0 else 999999

                    mat[x][y] = min(left_scan,top_scan)

        for x in range(rows-1, -1, -1):
            for y in range(cols-1, -1, -1):
                if mat[x][y]:
                    right_scan = mat[x][y+1] + 1 if y < cols-1 else 999999
                    down_scan = mat[x+1][y] + 1 if x < rows - 1 else 999999   

                    mat[x][y] = min(right_scan, down_scan, mat[x][y])

        return mat      