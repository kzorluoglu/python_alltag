# Sys.argv
# Variables and Values over Command Line sending
# Run on command : python Argv.py "Selam"

import sys

if len(sys.argv) >= 2:
    text = sys.argv[1]
    print(text)
else:
    print("Please Send minumum one Argument over Command Line")
