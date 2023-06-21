list_of_prime = []
count = 0
for i in range(2,200):       
    for j in range(2,i):
        if i%j==0:
            #print(i,"not prime")
            break   

    else:
        #print(i, "is prime")
        list_of_prime.append(i)
        count += 1
        print(count)
        if count == 20:
            break

print(list_of_prime)