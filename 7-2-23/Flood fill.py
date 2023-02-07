class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current=image[sr][sc]
        def fill(x,y):
            if x<0 or x>=len(image):
                return
            if y<0 or y>=len(image[0]):
                return
            if image[x][y]==color:
                return
            if image[x][y]!=current:
                return
            image[x][y]=color
            fill(x-1,y)
            fill(x,y-1)
            fill(x+1,y)
            fill(x,y+1)
        
        fill(sr,sc)
        return image

       
