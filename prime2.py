def prime_number():
  prime = True

  number = int(input("Enter the number: "))


  for i in range(2, number):
    
    if number % i == 0:
        prime = False
        break
        
  if prime:
      print(f"{number} is prime")
  else:
      print(f"{number} is not prime")


prime_number()