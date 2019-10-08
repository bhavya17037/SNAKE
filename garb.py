'''input
1
2 2 3
1 1
1 2
2 1
'''
from numpy import *
from copy import deepcopy
t = int(input())
for i in range(t):
	s = 0
	n,m,q = map(int,input().split())
	arr1 = matrix(zeros([n,m],int))
	f= []
	j=0
	while j<q:
		x,y = map(int,input().split())
		arr2 = deepcopy(arr1)
		arr2[x-1]=1
		arr3 = deepcopy(arr1)
		arr3[:,y-1] = 1
		arr5 = (add(add(arr1,arr2),arr3))
		f.append(arr5)
		j+=1
	arr6 = matrix(zeros([n,m],int))
	for l in f:
		arr6=add(arr6,l)
	e=(arr6.flatten()).tolist()
	for r in e[0]:
		if int(r)%2!=0:
			s+=1
	print(s)