#sum of digits eg:123 
# n=int(input("enter three digits"))
# sum=0
# while n!=0:
#     sum=sum+n%10
#     n=n//10
# print(sum)

#print the reverse of  a number
# n=int(input("enter your digits"))
# rev=0
# while n!=0:
#     rev=rev*10+n%10
#     n=n//10
# print(rev)

#print the palindrome number
n=int(input("enter any number"))
rev=0
temp=n
while n!=0:
    rev=rev*10+n%10
    n=n//10
if rev==temp:
    print("number is palindrome")
else:
    print("number is not palindrome")
