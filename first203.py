lst = []
count = 0
for i in range(2,300):  #2,3,4,5,6,7,8,9,10.......
    prime = 1
    for j in range(2,i):   #2->   3->2   4->2,3      5->2,3,4
        if i%j==0:
            prime=0
            break
    if prime==1:
        lst.append(i)
        count += 1
        if count == 20:
            break
print(lst)   