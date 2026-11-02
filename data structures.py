# a=[34,12,89,45,67,12,78,23]
#list









# #loops on list:
# l=[10,20,31,42,51]
# #loop on values
# for i in l:
#     if i%2==0:
#         print(i)

# #loops on index:
# for i in range(len(l)):
#     print(f"{i} > {l[i]}")

#list methods
# a=[10,20,30,40]
# b=a.copy{whenevr yiu dont wanna change anything}
# b[0]=1000
# print(a)
# print(b)


# popped=a.pop
# print(pop)
# a.remove(){to remove any kind of values}


# a.reverse(){method   to apply on list and basically just to reversed}
# print(a)

#print list in reverse order
# a=[10,20,30,40,50]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)

# a=[10,20,30,40,50,60,70,80,90,100]
# temp=len(a)-1
# for i in range(0,len(a)-1//2):
#     a[i],a[temp]=a[temp],a[i]
#     temp=temp-1

# print the list in reverse order
# arr=[10,20,30,40,50]
# n=len(arr)
# for i in range(0,len(arr)//2):
#     arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
# print(arr)

#print positive elements of your list separately , ignore zero
# list=[10,-5,20,-3,0,8]
# print("positive")
# for element in list:
#     if element>0:
#         print(f"{element}")
# print("negative")
# for element in list:
#     if element<0:
#         print(f"{element}")

#mean of list elements
#calculate avg of all elements in a list
# list=[10,20,30,40]
# sum=0
# for elem in list:
#     sum+=elem
# print(f"mean->{sum/len(list)}")

#find the greatest element and its index
# arr=[2,96,69,77,145,20]
# max=arr[0]
# index=0
# for i in range(len(arr)):
#     elem=arr[i]
#     if elem>max:
#         max=elem
#         index=i
#         print(f"is {max} at index {index}")

#find the missing number 
#a list contains numbers from 1 to n , but one number is missing . wap to find the missing number
# arr=[1,2,4,5]
# n=len(arr)
# #og_sum = ((og_n)*(og+1)//2)
# # og_sum=0
# for i in range (1,og_n+1):
#     og_sum+=i
# real_sum=0
# for elem in arr :
#     real_sum+=elem
# missing = og_sum-real_sum
# print(missing)

#check whether a list is sorted or not
#check if list elements are arranged in ascending order
# arr=[10,20,30,40,50]
# n=len(arr)
# is_sorted=True
# for i in range(0,n-1):
#     if arr[i]>arr[i+1]:
#         is_sorted=(False)
#         break
# if is_sorted:
#     print("list is sorted")
# else:
#     print("list is not sorted")

#palindrome list
# arr=[2,3,15,15,3,2]
# n=len(arr)
# is_palindrome=True
# for i in range(n//2):
#     if arr[i]!=arr[n-i-1]:
#         is_palindrome=False
#         break
# if is_palindrome:
#     print("palindrome")
# else:
#     print("not palindrome")


#14/10/2026 (BUBBLE SORT : OPTIMIZED WALA {IMP FOR INTERVIEW})
# arr=[64,34,25,12,22,11,9]
# n=len(arr)
# iterations=0
# for i in range(n):
#     for j in range(n-1-i):
#         iterations +=1
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr,iterations)