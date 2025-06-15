#program 63
# s1=input("Enter:")
# s2=input("Enter:")
# out=0
# if len(s1)==len(s2):
#     i=0
#     while i<len(s1):
#         if s1[i]==s2[i]:
#             out+=1
#         i+=1
# print(out)

#program 64
# x=eval(input("Enter:"))
# out=[]
# i=0
# while i<len(x):
#     if type(x[i])==int:
#         import math
#         f=math.factorial(x[i])
#         out.append(f)
#     elif type(x[i]) in [str,list,tuple,set,dict]:
#         out.append(len(x[i]))
#     i+=1
# print(out)

#program 65
# x=input("Enter:")
# i=0
# sum=0
# while i<len(x):
#     sum+=ord(x[i])
#     i+=1
# print(sum)
# if sum%2==0:
#     print(x[1::2])
# elif sum%2!=0:
#     print(x[::2])

#program 66
# x=input("enter:")
# i=0
# out=''
# while i<len(x):
#     if 'A'<=x[i]<='Z':
#         out+=chr(ord(x[i])+32)
#     elif 'a'<=x[i]<='z':
#         out+=chr(ord(x[i])-32)
#     else:
#         out+=x[i]
#     i+=1
# print(out)

#program 67
# n=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=1

#program 68
# n=int(input("Enter:"))
# i=1
# fac=[]
# while i<=n:
#     if n%i==0:
#         fac+=[i]
#     i+=1
# print(fac)

#program 69
s=input("Enter:")
sum=0
i=0
while i<len(s):
    if not ('A'<=s[i]<='Z' or 'a'<=s[i]<='z' or '0'<=s[i]<'9'):
        sum+=ord(s[i])
    i+=2
print(sum)