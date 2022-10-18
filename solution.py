
R = 3
C = 5

# Check if i, j is under the
# array limits of row and
# column

import numpy as np
from num2words import num2words
def issafe(i, j):

	if (i >= 0 and i < R and
			j >= 0 and j < C):
		return True
	return False


def infect(v):

	changed = False
	no = 2
	while (True):
		for i in range(R):
			for j in range(C):

				# Infect all infected
				# present at (i+1, j),
				# (i, j-1), (i, j+1),
				# (i-1, j)
				if (v[i][j] == no):
					if (issafe(i + 1, j) and
							v[i + 1][j] == 1):
						v[i + 1][j] = v[i][j] + 1
						changed = True

					if (issafe(i, j + 1) and
							v[i][j + 1] == 1):
						v[i][j + 1] = v[i][j] + 1
						changed = True

					if (issafe(i - 1, j) and
							v[i - 1][j] == 1):
						v[i - 1][j] = v[i][j] + 1
						changed = True

					if (issafe(i, j - 1) and
							v[i][j - 1] == 1):
						v[i][j - 1] = v[i][j] + 1
						changed = True

		# if no infected found
		# it means all infected
		# now
		if (not changed):
			break
		changed = False
		no += 1

	for i in range(R):
		for j in range(C):

			# if any uninfected is found
			# to be not infected then
			# ans is not possible
			if (v[i][j] == 1):
				return -1

	for i in range(R):
		for j in range(C):

			# if any uninfected is found
			# to be not infected then
			# ans is not possible
			if (v[i][j] == 0):
				return -1


	
	no=no-2
	print(num2words(no))
	return (no)
   
def checksize(v):
    return(np.shape(v))


def take_input():
	## Python program to take matrix input 

#Take dimension of matrix
	global R
	global C
	R = int(input("Enter the number of rows:"))
	C = int(input("Enter the number of columns:"))

# Initializing empty matrix
	A = []


# Matrix A user input
	print (" \n Enter matrix elements(row wise): \n")
	for i in range(R):		 
		a =[]
		for j in range(C):	
			a.append(int(input()))
		A.append(a)


# Print matrix A
	print (" \nYou have entered the given matrix  \n")
	for i in range(R):
		for j in range(C):
			#print(A[i][j], end = " ")
			v=A
	return(v)
	print(A)

	
	#print (" \nInfected \n")
	
	





# Driver function
if __name__ == "__main__":

	v = [[2, 2, 2, 2, 2],
		[2, 2, 2, 2, 2],
		[2, 2, 2, 2, 2]]
	i=int(input("Do you want to enter manually enter 1 or otherwise default matrice will be used"))

	if(i==1):
		v=take_input()
		print(v)
		print("Max time incurred to infect: ",
		infect(v))

	else:
		print("Max time incurred to infect: ",
		infect(v))
	



