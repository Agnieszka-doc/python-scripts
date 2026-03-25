point_list = [(1, 2), (-1, 3), (0, -2), (2, 2), (0.5, 0.5)]
# (a) punkt w kole jednostkowym
in_circle = lambda p: p[0]**2 + p[1]**2 <= 1
print(list(filter(in_circle, point_list)))
# (b) dodatnie współrzędne
positive_coords = lambda p: p[0] > 0 and p[1] > 0
print(list(filter(positive_coords, point_list)))
# (c) sort: y malejąco, x rosnąco
point_list.sort(key=lambda p: (-p[1], p[0]))
print(point_list)
# (d) sort: |x| + |y|
point_list.sort(key=lambda p: abs(p[0]) + abs(p[1]))
print(point_list)