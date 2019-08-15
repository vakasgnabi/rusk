# condition
'''
num=input("Please enter a number: ")
num=int(num)
if num % 2==0:
    print("Even number")
    print("Thank you")
else:
    print("Odd Number")
    print("Come Again")
    '''
num=input("Please enter a number: ")
num=int(num)
if num==50:
    print("Half Century")
elif num==100:
    print("Century")
elif num>100:
    print("Century +")
else:
    print("Unknown number")