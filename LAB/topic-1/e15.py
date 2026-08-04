# Experiment 15: Closest Pair of Points
# Compare Brute Force and Divide & Conquer

import math

# ---------------------------------
# Distance between two points
# ---------------------------------
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# ---------------------------------
# Brute Force Method - O(n²)
# ---------------------------------
def brute_force(points):
    min_dist = float('inf')
    closest_pair = None

    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])

    return closest_pair, min_dist


# ---------------------------------
# Divide & Conquer Method - O(n log n)
# ---------------------------------
def closest_pair(points):
    points = sorted(points)

    def solve(pts):
        if len(pts) <= 3:
            return brute_force(pts)

        mid = len(pts) // 2
        mid_x = pts[mid][0]

        left_pair, left_dist = solve(pts[:mid])
        right_pair, right_dist = solve(pts[mid:])

        if left_dist < right_dist:
            min_dist = left_dist
            best_pair = left_pair
        else:
            min_dist = right_dist
            best_pair = right_pair

        strip = [p for p in pts if abs(p[0] - mid_x) < min_dist]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    best_pair = (strip[i], strip[j])

        return best_pair, min_dist

    return solve(points)


# ---------------------------------
# Main Program
# ---------------------------------
points = [(1, 2), (4, 5), (7, 8), (3, 1)]

pair1, dist1 = brute_force(points)
pair2, dist2 = closest_pair(points)

print("Points:", points)
print("\nBrute Force:")
print("Closest Pair:", pair1)
print("Distance =", dist1)

print("\nDivide & Conquer:")
print("Closest Pair:", pair2)
print("Distance =", dist2)