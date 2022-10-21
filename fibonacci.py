a=int(input("No of terms\n"))
n1=0
n2=1
b=0
if a<=0:
 print("the given number is not valid")
elif a==1:
 print("the fibonacci sequence of the numbers upto",a)
 print(n1)
else:
 print("the fibonacci sequence is\n")
while b<=a:
 print(n1)
 nth=n1+n2
 n1=n2
 n2=nth
 b+=1