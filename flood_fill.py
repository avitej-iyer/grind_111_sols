class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        def flooder(x_coord,y_coord):
            if x_coord < 0 or x_coord >= len(image):
                return
            if y_coord < 0 or y_coord >= len(image[0]):
                return
            if image[x_coord][y_coord] != orig:
                return
            image[x_coord][y_coord] = color
            flooder(x_coord-1,y_coord)      
            flooder(x_coord+1,y_coord)
            flooder(x_coord,y_coord-1)
            flooder(x_coord,y_coord+1)
            return

        if image[sr][sc] == color:
            return image

        flooder(sr, sc)
        return image     


        