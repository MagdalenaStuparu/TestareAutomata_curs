numar= '12345'
# #print(len(numar))
# # cifra_unitatilor = 'e'
# # cifra_zecilor ="d"
# # cifra_sutelor='c'
# # Cifra_miilor='b'
# cifra_zecilor_de_mii='a'

numar_inversat=''
# for i in range(len(numar),0,-1):
#     numar_inversat= numar[i-1]
#     print(numar_inversat)
# else:
#     print('am terminat')

for i in range(len(numar)):
    if i==0:
        print(f'cifra zecilor de mii e {numar[i]}')
    elif i==1:
        print(f'cifra miilor este nr de e {numar[i]}')
    elif i==2:
        print(f'cifra sutelor este nr de e {numar[i]}')
    elif i == 3:
        print(f'cifra zecilor este nr de e {numar[i]}')
    else:
        print(f'cifra unitatilor este nr de e {numar[i]}')



#print('numarul inversat este:'+numar_inversat[0])






