class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])

        if m*n!=r*c:
            return mat
        
        flat_mat=[]
        for i in range(m):
            for j in range(n):
                flat_mat.append(mat[i][j])
        
        new_mat=[]
        idx=0
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(flat_mat[idx])
                idx+=1
            new_mat.append(row)
        return new_mat
        