class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        row_count = len(board)
        col_count = len(board[0])
        def word_search(x_coord, y_coord, word_pos):
            char = board[x_coord][y_coord]
            if char != word[word_pos]:
                return False
            elif word_pos == word_len-1:
                return True
            
            board[x_coord][y_coord] = ''

            if x_coord > 0 and word_search(x_coord-1,y_coord, word_pos+1):
                return True
            if y_coord > 0 and word_search(x_coord, y_coord-1, word_pos+1):
                return True
            if x_coord < row_count-1 and word_search(x_coord+1, y_coord, word_pos+1):
                return True
            if y_coord < col_count-1 and word_search(x_coord, y_coord+1, word_pos+1):
                return True
            return False

        for i in range(row_count):
            for j in range(col_count):
                if word_search(i,j,0):
                    return True

        return False                



                
