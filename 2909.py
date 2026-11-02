# n=int(input("enter your digits"))
# sum=0
# temp=n
# while n!=0:+
#     z=n%10
#     fact=1
#     for i in range (1,z+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# if sum==temp:
#     print("strong number")
# else:
#     print("not a strong number")


#number guessing game(1-100)
import random
num=random.random(1,100)
tries=0
while True:
    tries +=1
    guess = int(input("guess your number 1-100"))
    if guess == num:
        print(f"congratulations you won in {tries} tries")
        break
    elif guess>num:
        print("go a bit lower")
    else:
        print("go a bit higher")





