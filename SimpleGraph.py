import numpy

def Adjacency(n):

  adjMatrix = numpy.zeros((n, n))

  for x in range(n):
      for y in range(numpy.random.randint(0,n)):
          i = numpy.random.randint(0,n)
          if adjMatrix[x][i] != 1 :
              adjMatrix[x][i] += 1

  for i in range(n):
    for x in range(n):
       adjMatrix[x][i] = adjMatrix[i][x]
       adjMatrix[x][x] = 0
       
  return (adjMatrix)



n = int(input("Please insert n: "))
print ("The adjacency matrix of the n-vertex random graph is: ") 
print(Adjacency(n))    