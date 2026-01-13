num=int(input("Enter your number:  "))
temp=num
bin1=""
while temp>0:
    rem=temp%2
    bin1=str(rem)+bin1
    temp=temp//2
print(bin1, "is your number in binary")