try:
    fh=open("sample.txt","rt")
    print("Reading file content:\n")
    count = 1
    for i in fh.readlines():
        if i!='':
            print("line",count,":",i)
            count=count+1
except FileNotFoundError:
    print("The file 'sample.txt' was not found")
