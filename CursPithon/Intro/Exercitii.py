# n = int(input('n='))
# x = int(input('X='))
# d = 1
# b = 0
# a = 0
# while d <= x:
#     if x%d==0:
#         b = b+1
#     else:
#         print('nu este bun divizorul')
#     d = d+1
#
# if b==2:
#     while n%x==0:
#         n = n/x
#         a = a+1
#     print(a)
# else:
#     print('Nu este prim')

#se da un nr natural sa se adauge dupa fiecare cifra impara cifra 0
# x =int(input('x='))
#
# while x != 0:
#     c = x%10
#     if c%2!=0:
#
#
# print(x)

'''
Sa se determine toate numerele prime de 2 cifre care oglindite sunt tot prime.
'''

x = 10
while x <= 99:
    d = 1
    s = 0
    while d <= x:
        if x%d==0:
            s = s+1
        d = d+1
    c = x%10
    y = 0
    a = x
    y = y+c*10
    a = a/10
    dy = 1
    sy = 0
    while dy<= y:
        if y%dy== 0:
            sy = sy+1
        dy = dy+1
    if s == 2 and sy == 2:
        print(x)
    x = x+1


print("Am iesit din while")















