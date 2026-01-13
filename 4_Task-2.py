try:
    with open("output.txt", "w") as fh:
        a = input("Enter text to write to the file: ")
        fh.write(a + "\n")
        print("Data successfully written to output.txt.")
    with open("output.txt", "a") as fh:
        b = input("Enter additional text to append: ")
        fh.write(b + "\n")
        print("Data successfully appended.")
    print("\nFinal content of output.txt:\n")
    with open("output.txt", "r") as fh:
        file_content = fh.read()
        print(file_content)
except FileNotFoundError:
    print("No such file exists.")
