class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n, m =len(mat[0]), len(mat)

        T= r*c
        if n*m != T:
            return mat
        
        output = [[0 for _ in range(c)] for _ in range(r)]
        print(output)
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
        
        k = 0
        for i in range(M):
            for j in range(N):
                output[k//c][k%c] = tmp[k]
                k+=1

        return output