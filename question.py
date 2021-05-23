my_file=open("question3.txt","r")
for i in range(18):
    c=my_file.readline()
    print(c)
    if "delhi" in c:
        delhi=open("delhi.txt","a")
        delhi.write(c)
    elif "shimla" in c:
        shimla=open("shimla.txt","a")
        shimla.write(c)
    else:
        other=open("other.txt","a")
        other.write(c)
