import numpy

def RandomAdj(n): #generates the adjacency matrix of random n-vert simple graph

  adjMatrix = numpy.zeros((n, n))

  for x in range(n):
      for y in range(numpy.random.randint(0,n+5)):
          i = numpy.random.randint(0,n)
          if adjMatrix[x][i] != 1 :
              adjMatrix[x][i] += 1

  for i in range(n):
    for x in range(n):
       adjMatrix[x][i] = adjMatrix[i][x]
       adjMatrix[x][x] = 0
       
  return (adjMatrix)

n = int(input("Please insert n: "))
a = n
components = n
matrix = RandomAdj(n)
print ("The adjacency matrix of the random n-vertex is: \n", matrix)

for x in range(n):
	for y in range(n):
		if matrix[x][y] == 1 and components > 1:
			matrix[y] = 0
			components += -1
			print(components, "\n", matrix)


print("Number of components:" , components)

