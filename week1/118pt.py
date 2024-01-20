class Solution:
    # Optimized solution:
    
    
    
    # Initial Solution. Works but conditions could be cleaner
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        # Handles the row in the triangle
        for i in range(2, numRows + 1):
            newRow = []
            lastRow = res[-1]
            # Handles elements in each row for triangle
            for j in range(i):
                if 0 < j < i - 1:
                    newRow.append(lastRow[j-1] + lastRow[j])
                else:
                    newRow.append(1)
            res.append(newRow)
        return res