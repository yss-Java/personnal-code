L = [x * 2 for x in range(5)]
# G = (x * 2 for x in range(5))
#
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))

G = (x * 2 for x in range(5))
for x in G:
    print(x)
