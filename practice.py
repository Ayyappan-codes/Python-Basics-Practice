#program1
# a=int(input("enter a number:"))
# if a%2==0:
#     print(a**2)

#program 2
# a=input("enter a string:")
# if len(a)>6:
#     print(a)

#program 3
# a=input("Enter a string:")
# if len(a)%2==0 and len(a)<10:
#     print(a[0])

#program 4
# b=eval(input("enter a list:"))
# if type(b[0])==int:
#     print(b[0]**3)

#program 5
# x=input("Enter:")
# if 'A'<=x[-1]<='Z':
#     print(x[-1])

#program 6
# x=int(input("enter"))
# if x%2==0:
#     print('Even')
# else:
#     print('odd')

#program 7
# c=eval(input("enter:"))
# if type(c) in [list,set,dict]:
#     print("Mutable")
# else:
#     print("Immutable")

#program 8
# v=input("enter:")
# if '0'<=v[-1]<='9':
#     print(v[0])
# else:
#     print(v)

#program 9
# z=eval(input("Enter:"))
# if type(z) in [int,float,complex,bool]:
#     print("Single")
# else:
#     print("collection")

#program 10
# a=input("enter:")
# if len(a)%2!=0:
#     print(a)
# else:
#     print(a[::-1])

#pro 11
# a=eval(input("Enter:"))
# if type(a[-1])==str and len(a[-1])>3:
#     print('str')
# else:
#     print('no str')

#pro 12
# a=int(input("Enter:"))
# if a%8==0 and a%3==0:
#     print(a**2)
# else:
#     print(a**3)

#pro 13
# x=eval(input("Enter a lis:"))
# if type(x[0])==type(x[1]):
#     print("homogenous")
# else:
#     print("heterogenous")

#pro 14
# x=eval(input("Enter a dict:"))
# key=eval(input("Enter a key:"))
# if key in x:
#     print('ict')
# else:
#     print('not a dict')

#pro 14
# x=eval(input('enter:'))
# key=eval(input("enter:"))
# a=x.keys()
# if key in a:
#     print('yes')
# else:
#     print('no')

#pro 15
# a=eval(input("enter:"))
# if not ('A'<=a<='Z' or 'a'<= a<='z' or '0'<=a<='9'):
#     print('spcl')
# else:
#     print('not a spcl')

#pro 16
# a=input("enter:")
# if a in 'AEIOUaeiou':
#     print('vowel')
# else:
#     print('not a vowel')

#pro 17
# a=input("Enter:")
# if a[::-1]==a:
#     print('Palindrome')
# else:
#     print("not a palindrome")

#pro 18
# a=input("Enter:")
# if 'A'<=a<='Z':
#     print('UC')
# elif 'a'<=a<='z':
#     print('Lc')
# elif '0'<=a<='9':
#     print('digit')
# else:
#     print('spcl char')

#pro 19
# a=int(input("Enter:"))
# if 0<=a<=9:
#     print('single')
# elif 10<=a<=99:
#     print('double')
# elif 100<=a<=999:
#     print('triple')
# else:
#     print('more than that')

#pro 20
# a=eval(input("Enter:"))
# if type(a)==int:
#     print('Integer')
# elif type(a)==float:
#     print('Float')
# elif type(a)==complex:
#     print('Comp')
# elif type(a)==bool:
#     print('Boolean')
# elif type(a)==str:
#     print("String")
# elif type(a)==list:
#     print("List")
# elif type(a)==tuple:
#     print("Tuple")
# elif type(a)==set:
#     print("Set")

#program 21
# s=input("Enter a str:")
# if ord(s[-1])%2==0:
#     print("Even")
# else:
#     print("odd")

#program 22
# a=eval(input("enter l1:"))
# b=eval(input("enter l2:"))
# if a[0]!=b[-1]:
#     a.pop(0)
#     b.pop()
# print(a,b)

#program 23
# a=int(input("enter v1"))
# b=int(input("enter v2"))
# c=int(input("enter v3"))
# if b<a>c:
#     print("a is grater")
# elif a<b>c:
#     print("b is greater")
# else:
#     print("c is great")

#program 24
# x=int(input("enter int:"))
# if int(str(x)[0])%2==0:
#     print("it is even")
# else:
#     print("it is odd")

#program 25
# x=eval(input("Enter:"))
# if type(x[0])==str:
#     print(x[0])
# elif type(x[0])==int:
#     print(x[0]%5)
# elif type(x[0])==complex:
#     print(x[0]+2025)
# else:
#     print(x[::-1])

#program 26
# x=eval(input("Enter a list:"))
# if type(x[0])==int:
#     if x[0]%2==0:
#         if x[0]%18==0:
#             print(x[0]**2)
#         else:
#             print("no by 18")
#     else:
#         print("not an even int")
# else:
#     print("not an int")

#program 27
# x=input("Enter a string:")
# if x[::-1]:
#     if 'A'<= x[0]<='Z':
#         if x[-1] in 'AEIOUaeiou':
#             if len(x)>=3:
#                 print(x)
#             else:
#                 print("length less than 3")
#         else:
#             print("not a vowel")
#     else:
#         print("not UC")
# else:
#     print("not a palindrome") 

#program 28
# a=int(input("eneter m1:"))
# b=int(input("eneter m2:"))
# c=int(input("eneter m3:"))
# d=int(input("eneter m4:"))
# e=int(input("eneter m5:"))
# f=int(input("eneter m6:"))
# if a>=35 and b>=35 and c>=35 and d>=35 and e>=35:
#     per=(a+b+c+d+e)/6
#     print(per)
#     if per>=90:
#         print('Pass & Very Good')
#     elif per>=75:
#         print('Pass & Good')
#     elif per>=50:
#         print('Pass & OK')
#     else:
#         print('Fail')

#program 29
# a=int(input("Enter n1:"))
# b=int(input('Enter n2:'))
# c=int(input('Enter n3:'))
# d=int(input("enter n4:"))
# if a>b:
#     if a>c:
#         if a>d:
#             print("a is greater")
#         else:
#             print("d is greater")
#     elif c>d:
#         print("c is greater")
#     else:
#         print("d is greater")
# else:
#      if b>c:
#         if b>d:
#             print("b is greater")
#         else:
#             print('d is greater')
#     elif c>d:
#         print('c is greater')
#     else:
#         print('d is greater')

#program 30
# x=input("enter:")
# if 'A'<=x<='Z' or 'a'<=x<='z':
#     if x in 'AEIOUaeiou':
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('It is not alpha')

#program 31
# x=eval(input("Enter a value"))
# if type(x) in [str,list,tuple,]:
#     if len(x)%2==0:
#         print(x[::-1])
#     else:
#         print("len is not even")
# else:
#     print('it not support indexing')

#program 32
# x=eval(input("enter a list:"))
# if len(x)%2!=0:
#     mi=len(x)//2
#     mv=x[mi]
#     if type(mv)==int:
#         if mv%2==0:
#             print(mv)
#         else:
#             print('not even')
#     else:
#         print('it is not int')
# else:
#     print('no mv')

#program 33
# x=input("Enter:")
# if 'A'<= x[0] <='Z':
#     print(chr(ord(x[0])+32),'uc to lc')
# elif 'a'<=x[0]<='z':
#     print(chr(ord(x[0]-32)),'lc to uc')
# elif '0'<=x[0]<='9':
#     print(int(x[0])**3)
# else:
#     print(chr(ord(x[0])+5), 'spcl')

#program 34
# a=int(input("enter:"))
# if str(a)==((str(a)[::-1])):
#     print('Palindrome')
# else:
#     print('not a pali')

#program 35
# y=input("enter:")
# if ord(y[0])%2==0:
#     print("even")
# else:
#     print('odd')

#program 36
# x=eval(input("eneter a list:"))
# if len(x)%2==0:
#    print(x[1:len(x)+1:2])
# else:
#    print(x[0:len(x)+1:2])

#program 37
# a=eval(input("enter:"))
# b=eval(input('enter:'))
# if a is b:
#     print('same')
# else:
#     print('different')

#program 38
# a=eval(input("Enter:"))
# if len(a)==2:
#     if type(a[0])==type(a[1]):
#         print("Homogenous")
#     else:
#         print("hetero")
# else:
#     print('len is not 2')

#program 39
# a=int(input('enter:'))
# if a>0:
#     print('Positive')
# elif a<0:
#     print('negative')
# else:
#     print('Zero')

#program 40
# import keyword
# a=input("enter:")
# b= keyword.kwlist
# if a in b:
#    print('Keyword')
# else:
#    print('not a key')

#program 41
# a=input("Enter a char:")
# if 'A'<=a<='Z':
#     fav=str(ord(a))
#     print(int(fav[0]))
# elif 'a'<=a<='z':
#     lav=str(ord(a))
#     print(int(lav[-1]))
# elif '0'<=a<='9':
#     print(int(a)%3)
# else:
#     print(a[::-1])

#program 42
# i=0
# while i<10:
#     print('CSK')
#     i+=1

#program 43
# n=int(input('Enter:'))
# i=1
# while i<=n:
#     print(i)
#     i+=1

#program 44
# i=0
# while i<=10:
#     print(i)
#     i+=2    

#program 45
# n=int(input('Enter:'))
# i=1
# s=0
# while i<=n:
#     s=s+i
#     i+=1
# print(s)

#program 46
# s=input("enter:")
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1

#program 47
# i=1
# while i<=10000:
#     if str(i)==(str(i)[::-1]):
#         if 100<=i<=10000:
#             print(i)
#     i+=1

#program 48
# a=input('Enter a str:')
# i=0
# while i<len(a):
#     if i%2==0:
#         print(a[i])
#     i+=1

#program 49
# a=input("enter:")
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         print(a[i])
#     i=i+1

#program 50
# a=input('Enter:')
# UC=0
# LC=0
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         UC+=1
#     elif 'a'<=a[i]<='z':
#         LC+=1
#     i+=1
# print ("upper case=", UC,"lower case=" ,LC)

#program 51
# a=input("Enter:")
# ext=''
# i=0
# while i<len(a):
#     if i%2==0:
#         if 'a'<=a[i]<='z':
#             ext+=a[i]
#     i+=2
# print(ext)

#program 52
# a=input("Enter a string:")
# ei=''
# oi=''
# i=0
# while i<len(a):
#     if i%2==0:
#         ei+=a[i]
#     elif i%2!=0:
#         oi+=a[i]
#     i+=1
# print("odd=",oi,"even=",ei)

#program 53
# f=input('Enter:')
# uc=''
# lc=''
# no=''
# spc=''
# i=0
# while i<len(f):
#     if 'A'<=f[i]<='Z':
#         uc+=f[i]
#     elif 'a'<=f[i]<='z':
#         lc+=f[i]
#     elif '0'<=f[i]<='9':
#         no+=f[i]
#     else:
#         spc+=f[i]
#     i+=1
# print('upper=',uc,'lower=',lc,'number=',no,'spcl=',spc)

#program 54
# v=input("Enter:")
# res=''
# i=0
# while i<len(v):
#     res=v[i]+res
#     i+=1
# print(res)

#program 55
# v=input("Enter:")
# rev=''
# i=len(v)-1
# while i>=0:
#     rev+=v[i]
#     i-=1
# print(rev)

#program 56
# z=input('Enter:')
# rev=''
# i=len(z)-1
# while i>=0:
#     rev+=z[i]
#     i-=1
# if z==rev:
#     print('Palindrome')
# else:
#     print("not")

#program 57
# n=int(input("Enter:"))
# rev=0
# while n!=0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)

#program 58
# k=eval(input("Enter:"))
# i=0
# s=0
# while i<len(k):
#     if type(k[i])==int:
#         s+=k[i]
#     i+=1
# print(s) 

#program 59
# a=eval(input("enter:"))
# ext=[]
# i=0
# while i<len(a):
#     if type(a[i])==str:
#         if a[i][0] in 'AEIOUaeiou':
#             ext+=[a[i]]
#     i+=1
# print(ext)

#program 60
# a=int(input("Enter:"))
# count=0
# while a!=0:
#     count+=1
#     a=a//10
# print(count)

#program 61
# a=eval(input("enter:"))
# out=[]
# i=0
# while i<len(a):
#     if a[i] not in out:
#         out+=[a[i]]
#     i+=1
# print(out)

#program 62
# x=input("Enter:")
# vow=''
# con=''
# i=0
# while i<len(x):
#     if 'A'<=x[i]<='Z' or 'a'<=x[i]<='z':
#         if x[i] in 'AEIOUaeiou':
#             vow+=x[i]
#         else:
#             con+=x[i]
#     i+=1
# print("vowel=", vow,"con=", con)
