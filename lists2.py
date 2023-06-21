# my_lists = ["mango", "litchi", "tomato", "medicine"]
# print(my_lists[1:])

numbers = [1, 3, 5, 7, 9]
print(numbers[1])

numbers[2] = 10
numbers.append(12)
numbers.pop(2)

sliced_lists = numbers[1:5]

print(numbers)
print(sliced_lists)


combined_list = numbers + sliced_lists
print(combined_list)

print(8 in combined_list)

combined_list.sort()
print(combined_list)