## Given a string of lowercase letters, determine the index of the character 
## whose removal will make the string a palindrome. 
## If the string is already a palindrome, then print -1 . There will always be a valid solution.

## Input:
## The first line contains n (the number of test cases). 
## The n subsequent lines of test cases each contain a single string to be checked.

## Output :
## int the zero-indexed position (integer) of a character whose deletion will result in a palindrome; 
## if there is no such character (i.e.: the string is already a palindrome), print -1.

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [a_temp for a_temp in input().strip().split(' ')][0]
   a.append(a_t)
        
def isPal(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
 
def solve(s):
    for i in range(int((len(s)+1)/2)):
        if s[i] != s[len(s)-i-1]:
            if isPal(s[:i]+s[i+1:]):
                return i
            else:
                return len(s)-i-1
    return -1
for i in range(n):
    x=a[i]
    print(solve(x))



"""
#Cleaned-up version:


def is_palindrome(s):
    return s == s[::-1]  # Pythonic, clean

def solve(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try removing either the left or right character
            if is_palindrome(s[left+1:right+1]):
                return left
            else:
                return right
        left += 1
        right -= 1
    return -1  # already a palindrome

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    print(solve(s))
