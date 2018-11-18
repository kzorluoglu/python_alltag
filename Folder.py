import os
# Print file path
print(__file__)

# print file directory
print(os.path.dirname(__file__))

# Load data.txt from same file location
with open(os.path.dirname(__file__) + "/samples/data.txt", "r") as file:
    print(file)

# Load data.txt with path join method
with open(os.path.join(os.path.dirname(__file__), "samples", "data.txt"), "r") as file:
    print(len(file.readlines()))


# Find directorys or file types
folder = os.path.join(os.path.dirname(__file__), "samples")
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        print("This is a directory :" + file)
    else:
        print("This is a file : " + file)


