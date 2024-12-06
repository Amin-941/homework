
#54

# n = int(input())
# if n>2 and n%2==0:
#     print(n-2)
# elif n>2 and n%2==0:
#     print(n-1)

#55

# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('bərabəryanlı')
# elif a!=b and b!=c and a!=c:
#     print('Muxtelifterefli')
# else:
#     print('beraberyanlı')

#56

# a = int(input())
# if a%6==0:
#     print('hə')
# else:
#     print('yox')

#57

# n = int(input())
# if n>0 and n<10:
#     print('bir rəqəmli')
# elif n>=10 and n<100:
#     print('iki reqemli')

#58

# n = int(input())
# if n%2==0:
#     print(n-1,n+1,'tek ədəddir')
# else:
#     print(n-1,n+1,'cüt ədəddir')

#59

# a = int(input())
# b = int(input())
# if a<b:
#     z = 3+b/abs(a+b)
# elif a>b:
#     z = a+a/abs(a+b)
# else:
#     z=(2*a*a +abs(b**3))**0.5
#     print(z)

#60

# n = int(input())
# m = int(input())
# p = int(input())
# if n==m==p:
#     print("3")
# elif n==m or n==p or m==p:
#     print("2")
# else:
#     print("0")

#61

# saatI = int(input("saatI",))
# deqiqeI = int(input("deqiqeI",))
# saniyeI = int(input("saniyeI",))
# saatII = int(input("saatII",))
# deqiqeII = int(input("deqiqeII",))
# saniyeII = int(input("saniyeII",))
# a2 =saatII * 3600 + deqiqeII * 60 + saniyeII
# a1 =saatI * 3600 + deqiqeI * 60 + saniyeI
# a = a2 - a1
# print(a)

#62

# a = int(input())
# b = int(input())
# c = int(input())
# if a<b and a>c or a>b and a<c:
#     print("qiymetce ortaolan=",a)
# elif b>a and b<c or b<a and b>c:
#     print('qiymetce ortaolan=',b)
# elif c>a and c<b or c<a and c>b:
#     print("qiymetce ortaolan=",c)


#dovr aciq suallar

#66

# n = int(input())
# n = str(n)
# for i in n:
#     print(i)

#67

# n = int(input())
# a = n//1000
# b = n//100%10
# c = n//10%10
# i = b*10+c
# if i%2==1:
#     e=b*c
# else:
#     e=b+c
# print(e)

#68 

# n = int(input())
# a = 0
# for i in range(1,n+1):
#     a = a+1/(i*i)
# print(a)

#69

# n = int(input())
# a = 0
# for i in range(1,n+1,2):
#     a = a+(1/i)**i
# print(a)

#70

# n = int(input())
# a = n
# b = 0
# while n >0:
#     e=n%10
#     b=b+e
#     n=n//10
# if a%b==0:
#     print("bolunur")
# else:
#     print("bolunmur")

#71 

# n = int(input())
# s = 0
# while n>0:
#     q = n%10
#     s = s + q
#     n = n//10
# print(s)





#80

# n = int(input())
# s = 0
# for i in range(2,n//2+1):
#     if n%i==0:
#         s = s +1
# if s > 0:
#     print("murekkeb eded")
# else:
#     print("sade eded")

#81

# n = int(input())
# s = 0
# i = 1
# while i<= n:
#     s= s+ ((-1)**(i+1))*i*(i+1)
#     i=i+1
# print(s)

#72 
# n = int(input())
# b = []
# print(b)
# for i in range(1,n+1):
#     a = int(input())
#     b.append(a)
# print(min(b))



#73
# n = int(input())
# a = []
# for i in range(1,n+1):
#     s = int(input())
#     a.append(s)
# print(max(a))



#elave sual min fuks. olmadan tapmaq
# a =[45,23,35,-4,5]
# b = a[0]
# for s in a:
#     if s < b:
#         b = s
# print(b)


#75
# n = [15,12,16,11,9]
# for i in n:
#     if i% 2==1:
#         s = i*i
#         print(s)


#94

# n = int(input())
# reqemler = "1234556789ABCDEF"
# m = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.find(i)*16**m
#     m=m-1
# print(onluq)

#99

# n = int(input())
# m = str(n)
# mini = min(m)




# n = int(input())
# n = str(n)
# s = 0
# f = 0
# for i in n:
#     if n.count(i) != 1:
#         f = 1
# if f==0:
#     for i in n:
#         if max(n) != i:
#             s = s+int(i)
#     print(s)
# else:
#     print("reqemleri muxtelif deyil")


# * lu sual

a = int(input())
b = int(input())
s = 0
if 1<a<b:
    for i in range(a+1,b):
        f = 0
        for j in range(2,i//2+1):
            if i % j==0:
                f = 1
        if f==0:
            s = s+1
    print(s)

##13 

n = int(input())
s = 0
b = []
for i in n:
    if i == 's':
        s = s + 1
    else:
        b.append(s)
        s = 0
print(max(b))


