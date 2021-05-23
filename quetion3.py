banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for i in banks_list:
    a=open("file-question3.txt","a")
    a.write(i+"\n")
a.close()