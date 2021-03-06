# Libraries
import csv
import random as rd
import math
#_______________________________________________________________

# CSV File Reading
with open('iris dataset.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#_______________________________________________________________

# General Variables
match=0
mismatch=0
Acurracy=0

print("Enter Number of Percetrons in Hidden Layer:")
N=int(input())
#________________________________________________________________

# Initializing Random Weights for Hidden Layer
rows=5
cols=N
HLWs = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
 for j in range(cols):
  HLWs[i][j] = rd.randint(-10,10)

print("Random Generated Weights for Hidden Layer are:")
for row in HLWs:
    print(row)
#_________________________________________________________________

# Initializing Random Weights for Output Layer
rows1=1
cols1=N+1
OLWs = [[0 for i in range(cols1)] for j in range(rows1)]
for i in range(rows1):
 for j in range(cols1):
  OLWs[i][j] = rd.randint(-10,10)

print("Random Generated Weights for Output Layer are:")
for row in OLWs:
    print(row)
#__________________________________________________________________

# Sigmoid Function
def sigmoid(z1):
  zs=1/(1+(pow(2.718,-(z1))))
  return zs
#__________________________________________________________________

# Hidden Layer Perceptron Function
def HLPerceptron(I,W,i,j):
  z=W[0][j]
  z= z + float(I[i][0])*W[1][j] + float(I[i][1])*W[2][j] + float(I[i][2])*W[3][j] + float(I[i][3])*W[4][j]
  s=sigmoid(z)
  return s  
#_____________________________________________________________________

# Output Layer Perceptron Function
def OLPercetron(L1,OL):
  z1=OL[0][0]
  for i in range(1,N+1):
    z1=z1+(L1[i]*OL[0][i])
  s1=sigmoid(z1)
  return s1
#_____________________________________________________________________

# Main
for i in range (1,151):
  L=list()
  L.append(0)
  for j in range (N):
    x=HLPerceptron(data,HLWs,i,j)
    L.append(x)

  yhat=OLPercetron(L,OLWs)
  #print(yhat)
  specie=0
  if yhat>=0.63 and yhat<1:
    specie=3
  elif yhat>=0.33 and yhat<0.63:
    specie=2
  elif yhat>=0 and yhat<0.33:
    specie=1
  #print("Specie is:",specie)
  if specie==float(data[i][4]):
    match=match+1
  else:
    mismatch=mismatch+1

Accuracy=(match/150)*100
print("Match Count is: ",match)
print("Mismatch Count is: ",mismatch)
print("Accuracy is:",Accuracy,"%")
