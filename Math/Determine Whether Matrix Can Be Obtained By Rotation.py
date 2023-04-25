class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for i in range(4):
            self.rotate(mat)
            if mat == target:
                return True
            
        return False