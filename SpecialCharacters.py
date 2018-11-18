import os

# Load txt file and read line by line
filename = os.path.join(os.path.dirname(__file__), "samples", "data.txt")
with open(filename, "r") as file:
    for line in file:
        print(line)

# Outpu would be
# Lorem ipsum
# Lorem ipsum
# # Special Character for reading
# Ã¤Ã¼Ã¶ÃŸ <-- Why?
# ÅŸiÄŸÃ¼  <-- Why?

# For Fixing
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line)

# Output would be
# Lorem ipsum
# Lorem ipsum
# # Special Character for reading
# äüöß
# şiğü
