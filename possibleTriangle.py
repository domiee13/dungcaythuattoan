# Python3 code to count the number of 
# possible triangles using brute 
# force approach 

# Function to count all possible 
# triangles with arr[] elements 
def findNumberOfTriangles(arr, n): 
	
	# Count of triangles 
	count = 0
	
	# The three loops select three 
	# different values from array 
	for i in range(n): 
		for j in range(i + 1, n): 
			
			# The innermost loop checks for 
			# the triangle property 
			for k in range(j + 1, n): 
				
				# Sum of two sides is greater 
				# than the third 
				if (arr[i] + arr[j] > arr[k] and
					arr[i] + arr[k] > arr[j] and
					arr[k] + arr[j] > arr[i]): 
					count += 1
	return count 

# Driver code 
def solve(n):
    size = n
    arr = [i for i in range(1,n+1)] 

    print("Total number of triangles possible is", 
                findNumberOfTriangles(arr, size)) 
    return findNumberOfTriangles(arr,size)
res = []
f = open('output_triangle.txt',"r+")
for i in range(1,1000000):
    print("{}\t\t".format(i),end="\t")
    f.writelines("{} is {}\n".format(i,solve(i)))
# This code is contributed by shubhamsingh10 
