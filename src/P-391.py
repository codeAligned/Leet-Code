class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        min_x, min_y, max_x, max_y = 1 << 32, 1 << 32, 0, 0
        square_sum = 0
        
        pts = {}
        
        # The square should be the same
        for x1, y1, x2, y2 in rectangles:
            min_x, min_y, max_x, max_y = min(x1, min_x), min(y1, min_y), max(x2, max_x), max(y2, max_y)
            square_sum += (x2 - x1) * (y2 - y1)

        if square_sum != (max_x - min_x) * (max_y - min_y):
            return False

        # The count of the four corner points should be 1
        for x1, y1, x2, y2 in rectangles:
            for p in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if p not in pts:
                    pts[p] = 1
                else:
                    pts[p] += 1

        for p in ((min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)):
            if p not in pts:
                return False
            elif pts[p] != 1:
                return False
            else:
                pts.pop(p)
        
        # the count of other points should be even
        for count in pts.values():
            if count %2 != 0:
                return False
        
        return True