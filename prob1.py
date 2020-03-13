# Hackerrank 
# https://www.hackerrank.com/challenges/no-idea/problem
import sys
n=[]
A=[]
B=[]

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

#skip the first line quickly
lens=sys.stdin.readline().rstrip() #integer input
lens=lens.split(' ')
lens=[int(x) for x in lens]

n=sys.stdin.readline().rstrip() #integer input
n=n.split(' ')
n=[int(x) for x in n]

A=sys.stdin.readline().rstrip() #integer input
A=A.split(' ')
A=[int(x) for x in A]

B=sys.stdin.readline().rstrip() #integer input
B=B.split(' ')
B=[int(x) for x in B]
A.sort()
B.sort()
happ=0
for i in n:
    if binary_search(A,i):
        happ=happ+1
    elif binary_search(B,i):
        happ=happ-1

sys.stdout.write(str(happ))