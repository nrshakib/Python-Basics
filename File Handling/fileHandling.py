# a file needs to be opened before performing any action(read, write, append, delete)

# To open the file, use the built-in open() function.
#The open() function takes two parameters; filename, and mode.

# syntax
# variable = open('file directory', 'mode')

# there are 4 basic modes:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("File Handling\demofile.txt")
print(f.read())
f.close()

# It is good practice to close the file after completing work.
# You should always close your files.
# In some cases, due to buffering, changes made to a file may not show until you close the file.

# by using the with keyword, the close function is not needed.
# it automatically closes the file
with open("File Handling\demofile.txt") as f:
  print(f.read())


# writing to an existing file

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# with open('File Handling\demofile.txt', 'a') as file:
#   file.write("\nThis is first line")

with open("File Handling\demofile.txt", "w") as file:
  file.write("This is added by write")

#open and read the file after the appending:
with open("File Handling\demofile.txt") as file:
  print(file.read())


# create a new file
# To create a new file in Python, use the open() method,
# with one of ['x', 'a', 'w'] parameters:
# f = open("File Handling\myfile.txt", "x")

# Result: a new empty file will be created.
# If the file already exists, an error will be raised.


# delete file
# To delete a file, import the OS module, and run it's os.remove() function:

# import os
# os.remove("File Handling\myfile.txt")

# To avoid getting an error, check if the file exists before trying to delete it:
import os
if os.path.exists("File Handling\myfile.txt"):
  os.remove("File Handling\myfile.txt")
else:
  print("The file does not exist")


# To delete an entire folder, use the os.rmdir() method:

# import os
# os.rmdir("myfolder")

# only the empty folders can be removed