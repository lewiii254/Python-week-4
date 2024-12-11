import os
file = open("Data.txt", "r")

print(file.read())

# Write a new file
newFile = open("NewText.txt", "w")
newFile.write("Python is real cool and Easy to learn")