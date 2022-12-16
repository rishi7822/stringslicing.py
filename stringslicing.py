#python slicing is about obtaining a sub string from the given string by slicing it respectively
#from start to end
#two methods

#using a slice() method
#using array slicing[::]method

#slice() method  slice(start,stop,step)

string = "BRUCEWAYNE"

#USING slice() constrctor
s1 = slice(5)
s2 = slice(1,6,2)
s3 = slice(-2,-4,-3)


print(string[s1])
print(string[s2])
print(string[s3])


# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Using indexing sequence
print(String[:3])
