import numpy

def Adjacency(sequence):
  sequence.sort(reverse=True)
  n=len(sequence)
  adjMatrix = numpy.zeros((n, n))

  for x in range(n):
      for i in range(x+1,n):
        if sequence[i]>0 and adjMatrix[x][i] != 1 and sequence[x]>0:
          adjMatrix[x][i] += 1
          sequence[i] += -1
          sequence[x] += -1

  for i in range(n):
    for x in range(n):
       adjMatrix[x][i] = adjMatrix[i][x]
       
  return (adjMatrix)

print ("Please enter a sequence:")
X = [int(x) for x in input().split()]
n = len(X)
komsumatris = Adjacency(X)
print ("The adjacency matrix of the sequence is: ") 
print(komsumatris)

for x in range(n):
	for y in range(n):
		if komsumatris[x][y] == 1:
			komsumatris[y] = 0
			komsumatris[:y] = 0
a=0
for x in range(n):
	for y in range(n):
		if komsumatris[x][y] == 1:
			a += 1
			print("The center is:", y+1)
			if (a == 2):
				print("The center is edge between them.")

