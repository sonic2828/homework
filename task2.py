#homework
a=str(input())

b=str(input())

list=[a,b]
output=[str for str in list if a.endswith(b)]
def pstr(output,list):
    if output==list:
	    return True
    else:
           return False
pstr(output,list)

'''23. Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).
Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false'''
