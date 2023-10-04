class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #solution O(m*n)
        negative_count = 0
        for row in grid:
            for num in row:
                if num < 0:
                    negative_count += 1

        return negative_count

        #-----------------------------------------------
        #solution #2 O(m+n)
        
        count = 0
        n = len(grid[0])
        curr_row_neg_index = n - 1
        for row in grid:
            while curr_row_neg_index >=0 and row[curr_row_neg_index] < 0:
                curr_row_neg_index -= 1
            count += (n - (curr_row_neg_index + 1))
        return count