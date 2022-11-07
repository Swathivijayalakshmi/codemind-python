n=int(input())
t=n
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==t:
    print("True")
else:
    print("False")