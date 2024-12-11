# Error handling and exception

# try:
#     file = open("myDataer.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("Oops! This file does not exist")
# finally:
#     print("It's was nice seeing you")



try:
    file = open("Data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print(" Oops! This file does not exist! 🙅‍♂🎩")
finally:
    print("Thank you welcome again!🤗💯 \n It's was Nice seeing you")