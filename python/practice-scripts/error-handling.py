x=0

while True:
    try:
        filename = input("Enter file name: ")
        with open(filename, "r") as fh:
            file_data = fh.read()
    except FileNotFoundError:
        print(f"{filename} was not found. Check the filename spelling or if the file exists.")
    else:
        print(f'\nContents of {filename}:')
        print(file_data)
        x=0
        break
    finally: #runs regardless whether or not an error ocurred.
        x += 1
        if x == 3:
            print("File name input limit reached. Check name and re-run.")
            break

