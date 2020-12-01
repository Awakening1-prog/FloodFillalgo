class Solution:
    def fun(self,arr,i,j,r,c,target,color):
        if i<0 or j<0 or i>=r or j>=c or color!=arr[i][j]:
            return
        if arr[i][j]==target:
            return
        arr[i][j]=target
        self.fun(arr,i+1,j,r,c,target,color)
        self.fun(arr,i-1,j,r,c,target,color)
        self.fun(arr,i,j-1,r,c,target,color)
        self.fun(arr,i,j+1,r,c,target,color)
    def solve(self, matrix, r, c, target):
        self.fun(matrix,r,c,len(matrix),len(matrix[0]),target,matrix[r][c])
        return matrix
