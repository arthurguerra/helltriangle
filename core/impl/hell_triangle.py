class HellTriangle:
    """
    Class that represents a hell triangle. This class is able to find what the maximum sum from triangle is based
    on the following constraint:
        * An element can only be summed with one of the two nearest elements in the next row

    Example:
    Triangle:    6
               3   5
             9   7   1
           4   6   8   4

    In this triangle the maximum total is 6 + 5 + 7 + 8 = 26. The element 3 in row 2 can be summed with 9 and 7,
    but not with 1.
    """
    def __init__(self, triangle):
        #  validating input
        assert triangle is not None
        assert len(triangle) > 0

        self.triangle = triangle

    def find_max_sum(self):
        """
        Find the max sum within a triangle.

        Space Complexity: O(n) -> no additional memory required
        Runtime Complexity: O(n)

        Algorithm:
            * The idea is to pass each element in the triangle only once
            * The hell triangle looks like a binary tree (with some specialties) and we can find the maximum sum
              with an algorithm similar to DFS.
            1) In order to get the max sum of an element in the triangle, we need to know the maximum sum we
              can get from the left child as well as the max sum from the right child. So, the max sum of the
              current element will be whatever the current element value is plus the max sum between my left and
              right children.
            2) Based on (1), instead of going from the top to bottom, we go from bottom to top. By doing that, we
               avoid computing the max sum for the same element twice. So, first we compute the max sum for all "leaves"
               (last row of my triangle), then we compute the max sum for the row above, and so on until we reach the
               top.
               * The operation of finding the max sum is done in-place, so we are using the input array to store
                 the value for the max sum until the current element.
            3) Once the top of the triangle is reached, we will have the max sum for the whole triangle right at
               the top element, so we just return it.

        :return: the maximum sum that can be made from the triangle
        """
        rows = len(self.triangle)
        for row in reversed(range(0, rows-1)):
            left, right = 0, 1
            for col, _ in enumerate(self.triangle[row]):
                self.triangle[row][col] += max(self.triangle[row+1][left], self.triangle[row+1][right])
                left = right
                right += 1

        return self.triangle[0][0]
