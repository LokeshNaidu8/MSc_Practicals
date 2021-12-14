
V = 4

INF = 99999


def floydWarshall(graph): 
    
    """ dist[][] will be the output matrix that will finally 
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph)) 
    
    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
 
                dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                ) 
    printSolution(dist)
    
def printSolution(dist): 
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print("%7s" %("INF"), end = " ") 
            else: 
                print("%7d" %(dist[i][j]), end = " ") 
            if j == V-1: 
                print(end = "\n") 


print("Given graph is:")
print(""" 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           
""")

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
] 
floydWarshall(graph)
