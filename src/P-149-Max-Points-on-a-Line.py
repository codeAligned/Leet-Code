# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer

    # May have problem with the floating number rounding
    def line_param(self, p1, p2):
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        if x1 != x2:
            k = float(y1 - y2) / (x1 - x2)
            b = float(x1 * y2 - x2 * y1) / (x1 - x2)
        else:
            k = '*'
            b = x1
        return k, b

    def maxPoints(self, points):
        m = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                k, b = self.line_param(points[i], points[j])
                if (k, b) not in m:
                    m[(k, b)] = set()
                m[(k, b)].add(points[i])
                m[(k, b)].add(points[j])
        return max(len(item) for item in m.values())

s = Solution()
p = [(0,9),(138,429),(115,359),(115,359),(-30,-102),(230,709),(-150,-686),(-135,-613),(-60,-248),(-161,-481),(207,639),(23,79),(-230,-691),(-115,-341),(92,289),(60,336),(-105,-467),(135,701),(-90,-394),(-184,-551),(150,774)]
ps = [Point(item[0], item[1]) for item in p]

print s.maxPoints(ps)