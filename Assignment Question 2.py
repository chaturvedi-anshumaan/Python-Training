import numpy as np
import time
from numpy import random
np.random.seed(27)
A = np.random.randint(1,9,size = (20,20))
B = np.random.randint(1,9,size = (20,20))
print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")
print(f"Matrix A X Matrix B multiplication \n")
start_timer1 = time.perf_counter();
if A.shape[1] == B.shape[0]:
    res = np.dot(A, B)
    print(res)
else:
    print("Matrix multiplication not possible");
end_timer1 = time.perf_counter();
total_time_taken_by_numpy = (end_timer1-start_timer1)*10**6

print('\n================Matrix multiplication using List================================ \n')
print('=============================================')
print('First Matrix construction using list')
print('=============================================')
firstListOfRandomNumber = []
numberOfElementInListA = 400
for i in range(numberOfElementInListA):
    firstListOfRandomNumber.append(random.randint(1,9))
print('Constructed list: ', firstListOfRandomNumber)
n, m = 20, 20
 
k = 0
resultForMatrixA = []
 
# n*m == 20 > length, hence result not possible.
if n*m != len(firstListOfRandomNumber):
 
    # checking if Matrix Possible
    resultForMatrixA = "Matrix Not Possible"
else:
 
    # Constructing Matrix A
    for idx in range(0, n):
        sub = []
        for jdx in range(0, m):
            sub.append(firstListOfRandomNumber[k])
            k += 1
        resultForMatrixA.append(sub)
 
# printing result
resultForMatrixA = np.asarray(resultForMatrixA);
print("Constructed Matrix B: \n ",resultForMatrixA)

print('=============================================')
print('Second Matrix construction using list')
print('=============================================')
secondListOfRandomNumber = []
numberOfElementInListB = 400
for i in range(numberOfElementInListB):
    secondListOfRandomNumber.append(random.randint(1,9))
print('Constructed list: ', secondListOfRandomNumber)
a, b = 20, 20
 
j = 0
resultForMatrixB = []
 
# n*m == 20 > length, hence result not possible.
if a*b != len(secondListOfRandomNumber):
 
    # checking if Matrix Possible
    resultForMatrixB = "Matrix Not Possible"
else:
 
    # Constructing Matrix A
    for idx in range(0, a):
        sub = []
        for jdx in range(0, b):
            sub.append(secondListOfRandomNumber[j])
            j += 1
        resultForMatrixB.append(sub)
 
# printing result
resultForMatrixB = np.asarray(resultForMatrixB);
print("Constructed Matrix B : \n ",resultForMatrixB)

print("\n ===================================================")
print("=========Matrix multiplication of lists===============")
print("=================================================== \n")
start_timer2 = time.perf_counter();
matrixC = [[0]* n for length in range(m)]
for i in range(len(resultForMatrixA)):
   # iterate through columns of Y
   for j in range(len(resultForMatrixB[0])):
       # iterate through rows of Y
       for k in range(len(resultForMatrixB)):
           matrixC[i][j] += resultForMatrixA[i][k] * resultForMatrixB[k][j]

for r in matrixC:
   print(r)
end_timer2 = time.perf_counter();
time_taken_by_non_numpy = (end_timer2-start_timer2)*10**6;

print(f"\n Time taken by numpy arrays: {total_time_taken_by_numpy:.03f} micro seconds")
print(f"\n Time taken by List matrices: {time_taken_by_non_numpy:.03f} micro seconds ")

if(time_taken_by_non_numpy > total_time_taken_by_numpy):
    print("\n Numpy arrays are faster in matrix multiplication")
else:
    print("\n List matrix multiplication is faster")
