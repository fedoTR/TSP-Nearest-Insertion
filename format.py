# Imports
import os.path

# currentPath = pathlib.Path(__file__).parent.absolute()
askname_File = input('Filename?: ')
file_exists = os.path.exists(askname_File)
print(file_exists)

if file_exists is True:
    currrent_Filename = askname_File
    print("Working with: ", currrent_Filename)
    # Delete first 3 lines of current txt file
    with open(currrent_Filename, 'r+') as openFile:
        # Read and store all lines
        lines = openFile.readlines()
        # Move file pointer to the beginning
        openFile.seek(0)
        # Truncate file
        openFile.truncate()

        # Start writing lines except the first 3
        openFile.writelines(lines[3:])
    pass
else:
    print("File does not exist!")
    pass
