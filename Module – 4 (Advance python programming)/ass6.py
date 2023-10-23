
"""Write a Python program to append text to a file and display the text. 
"""

with open("my_file.txt", "a") as file:
    text_to_append = "This is some additional text that we're appending to the file."
    file.write(text_to_append)

with open("my_file.txt", "r") as file:
    file_content = file.read()
    print("File content:")
    print(file_content)