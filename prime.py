#Made by Gautham Nair
print("Prime Number Calculator")
print('Gautham Nair')
lower_input = int(input("Enter a number to find prime number from : "))
upper_input = int(input("Enter a number to find prime number till : "))

lower = lower_input
upper = upper_input

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower , upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
print("Thank you for using Prime Number Calculator")
print("http://github.com/gauthamnair2005/prime-number-calculator")
print("Do support me!!!😁😁👍")
exit = input("Press any key to exit")
print(exit)
