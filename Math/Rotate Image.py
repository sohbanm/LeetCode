class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                #save topleft
                topLeft = matrix[top][l + i]

                #move the bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
