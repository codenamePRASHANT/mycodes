
# list_of_radius = [7.5, 8.97, 20.39, 100, 129, 139, 600, 1000, 5.6, 8.9,12.7, 11.12, 12.13]



# for radius in list_of_radius:
#     def area_of_circle(radius):
#         return 3.14*(radius)**2
#     print(f"Area of cirle with {radius} is {area_of_circle(radius)}.")     


tuple1 = (1, 2, 3, 4)
for i in tuple1:
    print(i)



a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(a)

for i in range(3):
    for j in range(3):
        if j<i:
            a[i][j] = 0
print(a)  