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
    sequence[i] += -1
  return Graphic(sequence)  

  
print ("Please enter a sequence:")
dizi = [int(x) for x in input().split()]
print (dizi)
if Graphic(dizi) is True:
  print("Sequence is graphic.")
else:
  print("Sequence is not graphic.")