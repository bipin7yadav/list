# j=[7,8]
# for i in j:
# 	print(j)
# 	j.append(j)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor

# a= ['abc', 'xyz', 'aba', '1221']
# count=0
# for i in a:
# 	if len(i)>1 and i[0]==i[-1]:
# 		count+=1
# print(count)

# 7. Write a Python program to remove duplicates from a list. Go to the editor
# a=[1,2,3,7,3,2,4,4,6,4,3]
# dup=[]
# n=[]
# for i in a:
# 	if i not in dup:
# 		dup.append(i)
# 	else:
# 		n.append(i)
# print(dup)
# print(n)

# 8. Write a Python program to check a list is empty or not. Go to the editor
# a=[]
# if len(a)==0:
# 	print("list is empty")
# else:
# 	print("list is not emptys")

# 9. Write a Python program to clone or copy a list. Go to the editor
# a=[1,2,3,4,5,6,7,8]
# print(a.copy())

# 10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor
# n=2
# a=['we','are','united','no','matter','what']
# m=[]
# for i in a:
# 	if len(i)>n:
# 		m.append(i)
# print(m)

# # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# x= 


# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). Go to the editor
# a=[]
# for i in range(1,30):
# 		a.append(i**2)
# print(a[0:5])
# print(a[-5:])

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). Go to the editor
# a=[]
# for i in range(1,31):
# 	a.append(i**2)
# print(a[5:])

# 18. Write a Python program to generate all permutations of a list in Python.
# a=[1,2,3]
# m=[]
# for i in a:
# 	for j in a:
# 		for k in a:
# 			if i!=j!=k!=i:
# 				m.append([i,j,k])
# print(m)

# 19. Write a Python program to get the difference between the two lists. Go to the editor
# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# m=[]
# n=[]
# for i in list1:
# 	if i not in list2:
# 			m.append(i)
# for j in list2:
# 	if  j not in list1:
# 		n.append(j)
# m.extend(n)
# print(m)
# print(n)




# 20. Write a Python program access the index of a list. 
# a=[9,8,7,6,5,4,3,2,1]
# for i in a:
# 	print(a.index(i),i)

# 21. Write a Python program to convert a list of characters into a string. 
# a=['p','y','t','h','o','n']
# print(''.join(a))

# 23. Write a Python program to flatten a shallow list. Go to the editor

# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# m=[]
# for i in original_list[0] :
# 	m.append(i)
# for j in original_list[1] :
# 	m.append(j)
# for k in original_list[2] :
# 	m.append(k)
# for l in original_list[3] :
# 	m.append(l)
# print(m)

# 272. Write a Python program to generate a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.
# n=int(input("Enter starting point:"))
# v=int(input("Enternter end point:"))
# j=int(input("Enter diffence:"))
# m=[]
# for i in range(n,v,j):
# 	m.append(i)
# print(m)


# 271. Write a Python program to check if there are duplicate values in a given flat 

# a=[1,2,3,4,5,7,8]
# b=set(a)
# if len(a)==len(b):
# 	print("duplicates are not present")
# else:
# 	print("duplicates are present")


# 270. Write a Python program to check if the elements of the first list are contained in the second one regardless of order. Go to the editor
# a=[1,2,3,4,5,6]
# b=[7,9,2,5,3]
# for i in a:
# 	for j in b:
# 		if i == j:
# 			print("true")
# 			break
		
# if len(set(a).intersection(set(b)))>0:
# 	print("true")
# else:
# 	print("false")

# 269. Write a Python program to get the every nth element in a given list. Go to the editor
# a=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
# n=int(input("Enter nth element: "))
# print(a[::n])

# 268. Write a Python program to get a list with n elements removed from the left, right. Go to the editor
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[:4])
# b=[1,2,3,4,5,6,7,8,9,10]#doubt
# print(b[-3:])	

# 267. Write a Python program to get the cumulative sum of the elements of a given list. Go to the editor
# a=[1, 2, 3, 4]
# sum=0
# for i in a:
# 	sum+=i
# a.append(sum)
# print(a)

# 265. Write a Python program to generate a list, containing the Fibonacci sequence, up until the nth term. Go to the editor

# first=0
# second=1
# m=[]
# n=int(input("Enter length of fibonacci series: "))
# for i in range(n):
# 	last=first+second
# 	first=second
# 	second=last
# 	m.append(first)
# print(m)

# 264. Write a Python program to create a two-dimensional list from given list of lists.
# a=[(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
# m=[]
# for i in range(len(a)):
# 	m.append(a[i][0:2])
# print(m)

# 263. Write a Python program to move the specified number of elements to the start of the given list. 
# a=[1, 2, 3, 4, 5, 6, 7, 8]
# print(a[-1:]+ a[:-1])

# 262. Write a Python program to move the specified number of elements to the end of the given list. 
# a=[1, 2, 3, 4, 5, 6, 7, 8]
# print(a[2:]+ a[:2])

# 261. Write a Python program to get the most frequent element in a given list of numbers. 
# a=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# # m=[]
# maxc=a.count(a[0])
# for i in a:
# 	# m.append([i,a.count(a[i])])#doubt
# 	if maxc > a.count(a[i]):
# 		print(i, maxc)
# 		break

# 260.Write a Python program to check if all the elements of a list are included in another given list.
# a=[1,2,3,4,5]
# b=[6,7,1,2,3,4]
# for i in a:
# 	if i not in b:
# 		print("false")
# 		break
# 	else:
# 		print("true")
# 		continue

# 257. Write a Python program to check if two given lists contain the same elements regardless of order. 
# a=[1,2,3]
# b=[3,1,2]
# m=[]
# for i in a:
# 	if a[i] :
# 		m.append(i)#doubt
# print(m)

# 254. Write a Python program to get the weighted average of two or more numbers. Go to the editor
# a=[10, 50, 40]
# b=[2, 5, 3]
# print((a[0]*b[0]+a[1]*b[1]+a[2]*b[2])/(b[0]+b[1]+b[2]))

# 253. Write a Python program to get the n minimum elements from a given list of numbers. Go to the editor
# a=[-2, -3, -1, -2, -4, 0, -5]
# a.sort()
# print(a[:2])

# 251. Write a Python program to initialize and fills a list with the specified value. 
# m=[]
# n=int(input("enter no: "))
# o=int(input("Enter length: "))
# for i in range(o):
# 	m.append(n)
# print(m)

# a=['bipin','yadav']
# m=[]
# one=""
# two=""
# for i in a[0]:
# 	one=i+one
# m.append(one)
# for j in a[1]:
# 	two=j+two
# m.append(two)
# print(m) 




# a=[1,2,3]
# b=[1,2,3]
# a=b
# a.pop(0)
# print(a)
# print(b)









# list1=[1,2,3,4,6,7,8,9]
# output= 1 2 3 4  6 7 8 9
# for i in list1:
# 	print(i,end=" ")
# print(*slist1)
# for i in list1:
#  print(i)


# a=[34,25,6,19,93,90,54,38]

# for i in range(len(a)):
# 	for j in range(len(a)-i-1):
# 		if a[j]>a[j+1]:
# 			t=a[j]
# 			a[j]=a[j+1]
# 			a[j+1]=t
# print(a)

# a=[1000,10,35,65,23,98,0]
# largest=a[0]
# for i in range(len(a)):
# 	if a[i]>largest:
# 		largest=a[i]
# a.pop(a.index(largest))
# slarge=a[0]
# for i in range(len(a)):
# 	if a[i]>slarge:
# 		slarge=a[i]
# print(largest,slarge)


# Sample=[11, 33, 50]
# a=''
# for i in Sample:
# 	a+=str(i)
# print(a)

# l=['harsh','raghav','bipin','bhupendra','fxhf']
# Max=l[0]
# for i in l:
# 	if len(i)>len(Max):
# 		max=i
# print(max,len(max))

a=[1,1]
for i in range(10):
	a.append(a[i]+a[i+1])
print(a)