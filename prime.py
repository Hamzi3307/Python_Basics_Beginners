#!/usr/bin/python

def isprime(n):
    if n==1:
        print('Special Case for 1\n')
        return
    a=True
    for i in range(2,n):
        if n%i==0:
            print('{} equals to {} x {}\n'.format(n, n//i, i))
            a=False
            break
    if a==True:
        print(n,' is Prime Number \n')
for n in range(1,20):
    isprime(n)
