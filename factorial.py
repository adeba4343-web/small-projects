x=int(input("Enter the number you want the factorial of : "))
fact=1;
for i in range(1,x+1):
    fact=fact*i
print(f"The factorial of {x} is {fact}.")
