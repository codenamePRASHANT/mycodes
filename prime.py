# def prime_number():
#     number = int(input("Enter a number: "))
#     for i in range(2,number):
#         if number%i == 0:
#             print(number, " is not prime number")
            
            
        
            
# prime_number()


def prime_check():
    val=0
    number =int(input("enter the number to be checked for: "))
    #print(type(number))
    for i in range(2,number):
        if number%i==0:
            #print("not prime")
            return val
    val=val+1
    return val
val=prime_check()
if val==0:
    print("not prime")
else:
    print("prime")