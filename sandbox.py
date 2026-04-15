#!/usr/local/bin/python3

inf = int(1e8)
dist = [[ 0, inf,  1, inf, inf, inf],
 [inf,  0, inf, inf,  2,  7],
 [ 9, inf,  0,  7, inf,  6],
 [inf, inf, inf,  0,  2,  7],
 [ 4,  2,  9, inf,  0,  3],
 [ 4,  3, inf, inf, inf,  0]]
V = len(dist)


# for each intermediate vertex
for k in range(V):

  # Pick all vertices as source one by one
  for i in range(V):

    # Pick all vertices as destination
    # for the above picked source
    for j in range(V):

      # shortest path from i to j 
      if dist[i][k] != inf and dist[k][j] != inf:
        dist[i][j] = min(dist[i][j],
                         dist[i][k] + dist[k][j])

for row in dist:
    print(row)