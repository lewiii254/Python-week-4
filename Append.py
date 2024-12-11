#this function changes/appends the content in the NewText.txt file
writeDoc = open("NewText.txt","a" )
writeDoc.write("\n Append() Allows Adding Text without Deleting \n write() overwrites the content \n Hello world")

#Below creates a new file  text file that i have created
newDoc = open("NewDoc.txt", "w")
newDoc.write("This is  a new document that we have created, Edited Text")
