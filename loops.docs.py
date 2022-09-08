# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum_even=sum+i*i
#     else:
#         sum_odd=sum+i*i
# print(sum_even-sum_odd)
# i=i+1

# n=int(input("enter the number"))
# i=1
# sum=1
# while i<=n:
#     sum=sum*i
#     i=i+1
# print(sum)

 
# n=int(input("enter the number"))
# i=1
# sum=1
# while i<=n:
#     sum=i*i*i
#     i=i+1
# print(sum)

# i=1
# n=int(input("enter the number"))
# while i<=n:
#     print(i*i)
#     i=i+1





# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print
#     i=i+1

# i=1
# while i<=100:
#     print(i*"2",end=",")
#     i=i+1


# i=0
# while i<=10:
#     a=int(input("enter the num:"))
#     b=int(input("enter the num:"))
#     if a>b and b<a:
#         print(b,"is large")
#     else:
#         print(a,"is small")
#     i=i+1


# n=int(input("enter the num"))
# x=int(input("enter the num"))
# i=1
# sum=0
# f=1
# while i<=n:n=int(input("enter the num"))
#        f=f*i
#        sum=sum+(x**i/f)
#        i=i+1
# print(sum)


# n=int(input("enter the num"))
# i=0
# sum=0
# a=len(str(n))
# while i<=a:
#     r=n%10
#     b=r*2**i
#     sum=sum+r*2**i
#     n=n//10
#     i=i+1
# print(sum)


# n=int(input("enter no:"))
# total=0
# while n>0:
#     sum=n%10
#     total=sum+total
#     n=n//10
# print(total)    

# n=int(input("enter the num"))
# a=1
# while n>0:
#     p=n%10
#     a=a*p
#     n=n//10
#     print(a)
    
n=int(input("enter the number"))
r=1
j=0
while n>0:
    i=n%10
    j=j*10+i
    n=n//10
    print(i)