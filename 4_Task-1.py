try:
    fh=open("sample.txt","rt")
    print("Reading File content")
    count = 1
    for i in fh.readlines():
        if i!='':
            print("line",count,":",i)
            count=count+1
except FileNotFoundError:
    print("The file 'sample.txt' was not found")