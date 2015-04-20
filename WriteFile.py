file = input("Input filename")

openfile = open(file,'a')
openfile.writelines("hello world")
openfile.close()
