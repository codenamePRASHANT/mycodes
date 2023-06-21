# fname = input("Enter you first name: ").upper()

# splitted = fname.split(" ")
# print(splitted[-1], splitted[0])



sentence = input("Write a sentence: ")
print(sentence)
msg = input("Enter word to be replaced: ")
rep = input("Enter the word you want to replace with: ")
message = sentence.replace(msg, rep)
print(message)

