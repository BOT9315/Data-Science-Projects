## Aim :
## You are given two strings, A and B. 
## Find if there is a substring that appears in both A and B.

# Input:
# The first line of the input will contain a single integer , tthe number of test cases.
# Then there will be t descriptions of the test cases. Each description contains two lines. 
# The first line contains the string A and the second line contains the string B.

# Output:
# For each test case, display YES (in a newline), if there is a common substring. 
# Otherwise, display NO

n = int(input().strip())
a = []
for a_i in range(2*n):
   a_t = [a_temp for a_temp in input().strip().split(' ')][0]
   a.append(a_t)

for i in range(2*n):
    if (i%2==0):
        s1=set(a[i])
        s2=set(a[i+1])
        S=s1.intersection(s2) #intersection of subset -> return the same characters !!
        if (len(S)==0):
            print("NO")
        else:
            print("YES")

'''
#Corrected version (assuming you want common characters):

n = int(input().strip())
a = []

for _ in range(2 * n):
    a.append(input().strip())  # read the full line as one string

for i in range(0, 2 * n, 2):  # step by 2 to get pairs
    s1 = set(a[i])
    s2 = set(a[i + 1])
    if s1.intersection(s2):
        print("YES")
    else:
        print("NO")
