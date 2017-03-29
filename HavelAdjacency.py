import numpy

def Graphic(sequence):

  if sequence.count(0) == len(sequence):
    return True 
  sequence.sort(reverse=True)
  if sequence[len(sequence)-1] < 0: 
    return False
  if sum(sequence)%2 != 0: 
    return False
  if sequence[0] >= len(sequence):
   return False

  count = sequence.pop(0)

  for i in range(count):
    sequence[i] = sequence[i] - 1
  return Graphic(sequence)  
  
def Adjacency(sequence):

  sequence.sort(reverse=True)
  n=len(sequence)
  adjMatrix = numpy.zeros((n, n))

  for x in range(n):
      for i in range(x+1,n):
        if sequence[x] > 0 and sequence[i] > 0 and adjMatrix[x][i] != 1:
          adjMatrix[x][i] += 1
          sequence[i] += -1
          sequence[x] += -1

  for i in range(n):
    for x in range(n):
       adjMatrix[x][i] = adjMatrix[i][x]

  return (adjMatrix)

print ("Please enter a sequence:")
dizi = [int(x) for x in input().split()]
temp = dizi[:]

if Graphic(dizi) is True:
	print("Sequence is graphic.")
	print ("The adjacency matrix of the graphic sequence is: ") 
	print(Adjacency(temp))

else:
  print("Sequence is not graphic.")