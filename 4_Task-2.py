try:
    fh=open("output.txt","w")
    a=input("Enter the text to write to the file: ")
    fh.write(a)
    fh.close()
    fh=open("output.txt","a")
    b=input("Enter additional text to append: ")
    fh.append(b)
    fh.close()
except FileNotFoundError :
    print("no such file exist")