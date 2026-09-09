class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix: 
        #     left = 0
        #     right = len(i)-1
        #     while left <= right: 
        #         mid = (left+right)//2
        #         if target == i[mid]: 
        #             return True 
        #         elif target > i[mid]: 
        #             left = mid+1 
        #         else: 
        #             right = mid-1
        # return False

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows*cols-1
        while left <= right: 
            mid = left + (right-left)//2
            row = mid // cols 
            col = mid % cols
            if target == matrix[row][col]:
                return True 
            elif target > matrix[row][col]:
                left = mid+1
            else: 
                right = mid-1
        return False 
            